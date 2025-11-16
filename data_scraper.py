import json

def create_sample_data():
    mit_data = {
        "college_info": {
            "basic_info": {
                "full_name": "Muzaffarpur Institute of Technology (MIT), Muzaffarpur",
                "established": "1954",
                "type": "Government Engineering College",
                "affiliation": "Aryabhatta Knowledge University, Patna",
                "approval": "AICTE, New Delhi",
                "campus_size": "50 acres",
                "location": "Muzaffarpur, Bihar, India",
                "website": "https://mitmuzaffarpur.org",
                "phone": "0621-2242441",
                "email": "info@mitmuzaffarpur.org"
            },
            
            "history": """🏛️ **History & Legacy:**
• Established in 1954 as one of Bihar's premier engineering institutes
• Over 65 years of excellence in technical education
• Originally started as a polytechnic, upgraded to degree college
• Has produced thousands of successful engineers globally
• Known for its strong foundation in engineering education""",
            
            "vision_mission": {
                "vision": "To be a center of excellence in technical education and research, producing competent engineers capable of meeting global challenges.",
                "mission": """📚 **Mission:**
• Provide quality technical education through innovative teaching
• Develop state-of-the-art infrastructure and laboratories
• Foster industry-academia collaboration
• Promote research and development activities
• Develop socially responsible professionals"""
            },
            
            "key_features": [
                "🎓 Government institution with highly subsidized fees",
                "🏛️ Rich legacy of 65+ years in education",
                "🔬 Well-equipped laboratories and workshops",
                "📚 Central library with 15,000+ books",
                "🏠 Separate hostel facilities for boys and girls",
                "🤝 Strong industry connections for placements",
                "🌳 50-acre green campus with excellent infrastructure",
                "👨‍🏫 Experienced and qualified faculty members"
            ],
            
            "leadership": {
                "director": "Dr. Rajesh Kumar Singh",
                "registrar": "Dr. Priya Sharma",
                "heads_of_department": {
                    "cse": "Dr. Amit Kumar",
                    "it": "Dr. Sunil Verma",
                    "ece": "Dr. Neha Gupta",
                    "me": "Dr. Ramesh Patel"
                }
            },
            
            "infrastructure": {
                "academic_buildings": "4 main academic blocks",
                "laboratories": "15+ well-equipped labs across departments",
                "library": "Central library with digital section",
                "hostels": "7 hostels (4 boys + 3 girls)",
                "sports": "Playground, gymnasium, indoor games",
                "other": "Auditorium, cafeteria, medical facility"
            }
        },

        "courses": {
            "B.Tech": [
                {
                    "name": "B.Tech Computer Science & Engineering",
                    "duration": "4 Years",
                    "intake": 60,
                    "eligibility": "10+2 with PCM, 45% marks",
                    "tuition_fee": "₹22,120 for entire 4 years",
                    "highlights": "Programming, AI, Machine Learning, Web Development"
                },
                {
                    "name": "B.Tech Information Technology", 
                    "duration": "4 Years",
                    "intake": 60,
                    "eligibility": "10+2 with PCM, 45% marks",
                    "tuition_fee": "₹22,120 for entire 4 years",
                    "highlights": "Networking, Database, Software Engineering"
                },
                {
                    "name": "B.Tech Electronics & Communication",
                    "duration": "4 Years", 
                    "intake": 60,
                    "eligibility": "10+2 with PCM, 45% marks",
                    "tuition_fee": "₹22,120 for entire 4 years",
                    "highlights": "VLSI, Embedded Systems, Communication"
                },
                {
                    "name": "B.Tech Mechanical Engineering",
                    "duration": "4 Years",
                    "intake": 60, 
                    "eligibility": "10+2 with PCM, 45% marks",
                    "tuition_fee": "₹22,120 for entire 4 years",
                    "highlights": "Thermodynamics, Manufacturing, Design"
                }
            ],
            "M.Tech": [
                {
                    "name": "M.Tech Computer Science",
                    "duration": "2 Years",
                    "intake": 18,
                    "eligibility": "B.Tech in CSE/IT with 55% marks",
                    "fees": "₹75,000 per semester"
                }
            ]
        },
        
        "fees_structure": {
            "academic_fees": {
                "btech_total": "₹22,120 for entire 4-year program",
                "btech_annual": "₹5,530 per year",
                "note": "Heavily subsidized as a government institution"
            },
            "hostel_mess_fees": {
                "annual_hostel_mess": "₹38,684 per year (compulsory for male students)",
                "breakdown": {
                    "hostel_maintenance": "₹16,700 per year",
                    "mess_charges": "₹21,984 for 6 months"
                }
            }
        },
        
        "admissions": {
            "process": "Through Bihar UGEAC Counselling based on JEE Main Rank",
            "cutoff_ranks": {
                "information_technology": "200-300 UGEAC Rank",
                "computer_science": "150-250 UGEAC Rank",
                "electronics": "300-400 UGEAC Rank",
                "mechanical": "350-450 UGEAC Rank"
            }
        },
        
        "placements": {
            "companies": ["TCS", "Infosys", "Wipro", "Tech Mahindra", "Cognizant", "Capgemini", "Accenture"],
            "highest_package": "8 LPA",
            "average_package": "3.5 LPA",
            "training_cell": "Dedicated placement cell with training programs"
        },
        
        "student_life": {
            "clubs": ["Coding Club", "Robotics Club", "Cultural Society", "Sports Club"],
            "events": ["Tech Fest", "Cultural Fest", "Sports Tournament", "Workshops"],
            "facilities": ["WiFi Campus", "Medical Room", "Cafeteria", "Bank ATM"]
        }
    }
    
    with open('data/mit_data.json', 'w', encoding='utf-8') as f:
        json.dump(mit_data, f, indent=2, ensure_ascii=False)
    
    print("✅ COMPLETE college information added!")

if __name__ == "__main__":
    create_sample_data()