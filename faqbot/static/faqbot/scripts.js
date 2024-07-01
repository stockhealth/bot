// faqbot/static/faqbot/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");

    chatForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const query = document.getElementById("query").value;
        if (query.trim() === "") return;

        // Create the user message element
        const userMessage = document.createElement("div");
        userMessage.className = "chat-message user";
        userMessage.innerHTML = `<p><strong>You:</strong> ${query}</p>`;
        chatBox.appendChild(userMessage);

        // Clear the input field
        document.getElementById("query").value = "";

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;

        // Fetch the bot response
        fetch(`/get_answer/?query=${encodeURIComponent(query)}`)
            .then(response => response.text())
            .then(html => {
                // Parse the returned HTML and extract the bot's message
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, "text/html");
                const botMessage = doc.querySelector(".chat-message.bot");
                
                if (botMessage) {
                    chatBox.appendChild(botMessage);
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            });
    });
});
