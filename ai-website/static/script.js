function sendMessage() {
  const input = document.getElementById("user-input");
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  setTimeout(() => {
    addMessage(botReply(text), "bot");
  }, 500);
}

function addMessage(text, type) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.className = "message " + type;
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function botReply(message) {
  message = message.toLowerCase();

  if (message.includes("hi") || message.includes("hello")) {
    return "Hello 👋 I am KANHA’S AI EVERYWHERE.";
  }

  if (message.includes("who are you")) {
    return "A premium AI interface with a luxury dark design 😎";
  }

  return "Interesting… tell me more 🤔";
}

