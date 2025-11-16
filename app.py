from flask import Flask, render_template, request, jsonify
import json
import nltk
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

class CampusChatbot:
    def __init__(self):
        self.load_data()
        self.prepare_dataset()
        self.setup_nlp()
        print("🤖 Chatbot ready with complete college information!")
    
    def load_data(self):
        with open('data/mit_data.json', 'r', encoding='utf-8') as f:
            self.mit_data = json.load(f)
    
    def prepare_dataset(self):
        self.questions = []
        self.answers = []
                qa_pairs = [
            # COLLEGE INFORMATION & HISTORY 
            ("tell me about college", self.get_college_overview()),
            ("about mit muzaffarpur", self.get_college_overview()),
            ("college information", self.get_college_overview()),
            ("history of college", "🏛️ MIT Muzaffarpur was established in 1954 as one of Bihar's premier engineering institutions with over 65 years of legacy in technical education."),
            ("college history", "📜 College History:\n• Established: 1954\n• Over 65 years of excellence\n• Government engineering college\n• Rich legacy in technical education"),
            ("when was college established", "🏛️ MIT Muzaffarpur was established in 1954 - that's over 65 years of excellence in engineering education!"),
            
            ("vision mission", "🎯 Vision & Mission:\n\nVision: To be a center of excellence in technical education and research.\n\nMission: To provide quality technical education through innovative teaching methods and state-of-the-art infrastructure."),
            ("college vision", "🎯 College Vision:\nTo be a center of excellence in technical education and research, producing competent engineers capable of meeting global challenges."),
            
            ("college features", "🌟 Key Features:\n• Government institution with subsidized fees\n• 65+ years of legacy\n• 50-acre campus\n• Experienced faculty\n• Strong industry connections\n• Well-equipped laboratories"),
            ("why choose mit", "✅ Why Choose MIT?\n• Affordable government education\n• Rich legacy since 1954\n• Excellent infrastructure\n• Good placement record\n• Experienced faculty"),
            
            ("college infrastructure", "🏗️ Campus Infrastructure:\n• 50-acre campus\n• 4 academic blocks\n• 15+ laboratories\n• Central library\n• 7 hostels\n• Sports facilities"),
            ("campus facilities", "🏛️ Campus Facilities:\n• Well-equipped labs\n• Library with 15,000+ books\n• Hostels for boys and girls\n• Sports complex\n• Auditorium\n• Cafeteria"),
            
            ("contact information", "📞 Contact Information:\n• Phone: 0621-2242441\n• Email: info@mitmuzaffarpur.org\n• Website: https://mitmuzaffarpur.org\n• Location: Muzaffarpur, Bihar"),

            ("tuition fee btech", "💰 B.Tech Tuition Fees:\n• Total 4-year program: ₹22,120\n• Annual: ₹5,530 per year\n• Note: Heavily subsidized as a government institution"),
            ("btech fee", "🎓 B.Tech Fee Structure:\n• Academic Fee (4 years): ₹22,120\n• This is highly subsidized - Government institution"),
            
            ("hostel mess charge", "🏠 Hostel & Mess Fees:\n• Annual: ₹38,684 (compulsory for male students)\n• Hostel: ₹16,700/year\n• Mess: ₹21,984/6 months"),

            ("cutoff rank it", "📊 IT Branch Cutoff:\n• UGEAC Rank: 200-300\n• Through UGEAC Counselling\n• Based on JEE Main Rank"),
            ("admission process", "📝 Admission Process:\n1. Appear for JEE Main\n2. Register for UGEAC Counselling\n3. Choice filling\n4. Seat allotment\n5. Document verification\n6. Fee payment"),

            ("what courses", "🎓 Available Courses:\n• B.Tech: CSE, IT, ECE, Mechanical\n• M.Tech: Computer Science\n• All B.Tech: 4 years duration"),

            ("hello", "👋 Hello! Welcome to MIT Muzaffarpur!\nI can help with college information, fees, admissions, and courses!"),
            ("hi", "👋 Hi! Ask me about MIT Muzaffarpur - established in 1954!"),
            ("thank you", "😊 You're welcome!"),
            ("help", "🆘 I can help with:\n• College information\n• Fee structure\n• Admission process\n• Courses\n• Contact details"),
        ]
        
        for question, answer in qa_pairs:
            self.questions.append(question)
            self.answers.append(answer)
    
    def get_college_overview(self):
        return """🏛️ MIT Muzaffarpur - Overview

• Established: 1954 (65+ years of excellence)
• Type: Government Engineering College
• Affiliation: Aryabhatta Knowledge University
• Approval: AICTE, New Delhi
• Campus: 50 acres in Muzaffarpur, Bihar

Key Highlights:
🎓 Government institution with subsidized fees
🏛️ Rich legacy since 1954
🔬 Excellent infrastructure
👨‍🏫 Experienced faculty
🤝 Strong industry connections"""

    def setup_nlp(self):
        self.stop_words = set(nltk.corpus.stopwords.words('english'))
        self.stemmer = nltk.stem.PorterStemmer()
        
        self.vectorizer = TfidfVectorizer()
        processed_questions = [self.preprocess_text(q) for q in self.questions]
        self.question_vectors = self.vectorizer.fit_transform(processed_questions)
    
    def preprocess_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        tokens = [self.stemmer.stem(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)
    
    def get_response(self, user_input):
        processed_input = self.preprocess_text(user_input)
        input_vector = self.vectorizer.transform([processed_input])
        
        similarities = cosine_similarity(input_vector, self.question_vectors)
        best_match_idx = np.argmax(similarities)
        best_score = similarities[0, best_match_idx]
        
        print(f"User: '{user_input}' -> Match: '{self.questions[best_match_idx]}' (score: {best_score:.2f})")
        
        if best_score > 0.15:
            return self.answers[best_match_idx]
        else:
            return "I can help with:\n• College information\n• Fee structure\n• Admission process\n• Courses\n\nTry: 'Tell me about college' or 'B.Tech fees'"

chatbot = CampusChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    user_message = request.json.get('message', '')
    response = chatbot.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    print("🚀 CHATBOT RUNNING at http://localhost:5000")

    app.run(debug=True, port=5000)
