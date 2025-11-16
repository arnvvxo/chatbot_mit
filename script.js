const chatWindow = document.getElementById("chat-window");
const input = document.getElementById("user-input");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add(sender === "user" ? "user-bubble" : "bot-bubble");
    div.innerText = text;

    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.reply, "bot");
    })
    .catch(() => addMessage("Error: Unable to reach server.", "bot"));
}

/* ENTER sends message, Shift+Enter = new line */
input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        if (!e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    }
});
