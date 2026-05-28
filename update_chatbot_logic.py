import os

js_content = """
// CybKart Advanced AI Chatbot Logic
document.addEventListener('DOMContentLoaded', () => {
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

    const addBotMessage = (htmlContent) => {
      const botMsg = document.createElement('div');
      botMsg.className = 'chat-message bot-message';
      botMsg.innerHTML = `<div class="message-content">${htmlContent}</div>`;
      chatMessages.appendChild(botMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    const analyzeIntent = (text) => {
      const lowerText = text.toLowerCase();
      
      // Intent: Booking / Calendly
      if (lowerText.match(/(book|appointment|call|meeting|calendly|talk|strategy|schedule)/)) {
        return `Excellent! I can help you set up a Strategy Call with our lead systems architect. <br><br>Please select a time that works for you by clicking here: <br><a href="https://calendly.com/" target="_blank" style="display:inline-block; margin-top:10px; background:#0055ff; color:#fff; padding:8px 15px; border-radius:100px; text-decoration:none; font-weight:bold;">Book via Calendly ↗</a>`;
      }
      
      // Intent: Services / Web Design / SEO
      if (lowerText.match(/(service|web|design|seo|automation|build|create|offer|do you do)/)) {
        return `At CybKart Global, we engineer high-performance systems for local service businesses. Our core services include:
        <ul style="margin-top:10px; padding-left:20px;">
          <li><b>Web Solutions:</b> Premium mobile-first layouts and geo-optimized landing pages.</li>
          <li><b>Visibility:</b> Google Maps dominance and automated 5-star review systems.</li>
          <li><b>Automations:</b> Missed call text-back and automated booking engines.</li>
        </ul>
        <br>Which of these are you most interested in scaling?`;
      }
      
      // Intent: Pricing
      if (lowerText.match(/(price|pricing|cost|how much|fee|charge)/)) {
        return `Our systems are custom-engineered for your specific operational needs, so pricing scales with complexity. We offer transparent blueprint audits. <br><br>Would you like to book a quick discovery call to get an exact quote for your business?`;
      }
      
      // Intent: Greeting
      if (lowerText.match(/(hi|hello|hey|greetings|morning|afternoon)/)) {
        return `Hello there! I'm the CybKart AI Architect. I can help you understand our services, review our automations, or book a strategy call. What brings you here today?`;
      }

      // Default Response
      return `I see. To give you the most accurate roadmap for your digital growth, it's best we get on a quick Strategy Call. <br><br><a href="https://calendly.com/" target="_blank" style="display:inline-block; margin-top:10px; background:#0055ff; color:#fff; padding:8px 15px; border-radius:100px; text-decoration:none; font-weight:bold;">Book a Strategy Call ↗</a>`;
    };

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

      // Show typing indicator
      const typingMsg = document.createElement('div');
      typingMsg.className = 'chat-message bot-message typing-indicator-msg';
      typingMsg.innerHTML = `<div class="message-content" style="font-style: italic; color: #888;">AI is typing...</div>`;
      chatMessages.appendChild(typingMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;

      // Process response with slight delay
      setTimeout(() => {
        typingMsg.remove();
        const responseHTML = analyzeIntent(text);
        addBotMessage(responseHTML);
      }, 1200);
    });
  }
});
"""

# Read app.js and replace the old chatbot logic
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to remove the old chatbot logic. It starts at "  // Chatbot Initialization"
import re
new_content = re.sub(r'  // Chatbot Initialization.*', '', content, flags=re.DOTALL)
new_content = re.sub(r'document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\n  // Chatbot Initialization.*', '', content, flags=re.DOTALL)

# Since my previous script appended it at the end, I can just find "// Chatbot Initialization" and strip everything after
idx = content.find("document.addEventListener('DOMContentLoaded', () => {\n  // Chatbot Initialization")
if idx == -1:
    idx = content.find("  // Chatbot Initialization")

if idx != -1:
    content = content[:idx]

content += js_content

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js with robust chatbot logic.")
