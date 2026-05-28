import os

js_content = """

document.addEventListener('DOMContentLoaded', () => {
  // Chatbot Initialization
  const chatWidget = document.querySelector('.floating-chat-widget');
  const chatBotUI = document.getElementById('ai-chatbot');
  const chatCloseBtn = document.getElementById('chatbot-close-btn');
  const chatForm = document.getElementById('chatbot-form');
  const chatInput = document.getElementById('chatbot-input');
  const chatMessages = document.getElementById('chatbot-messages');

  if (chatWidget && chatBotUI) {
    chatWidget.addEventListener('click', () => {
      chatBotUI.classList.add('active');
    });

    chatCloseBtn.addEventListener('click', () => {
      chatBotUI.classList.remove('active');
    });

    chatForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if (!text) return;

      // Add user message
      const userMsg = document.createElement('div');
      userMsg.className = 'chat-message user-message';
      userMsg.innerHTML = `<div class="message-content">${text}</div>`;
      chatMessages.appendChild(userMsg);
      
      chatInput.value = '';
      chatMessages.scrollTop = chatMessages.scrollHeight;

      // Mock AI response
      setTimeout(() => {
        const botMsg = document.createElement('div');
        botMsg.className = 'chat-message bot-message';
        botMsg.innerHTML = `<div class="message-content">I'm currently running in limited access mode. To speak directly with our systems architect, please book a strategy call or leave your email.</div>`;
        chatMessages.appendChild(botMsg);
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }, 1000);
    });
  }
});
"""

with open('js/app.js', 'a', encoding='utf-8') as f:
    f.write(js_content)

print("Appended Chatbot JS to app.js")
