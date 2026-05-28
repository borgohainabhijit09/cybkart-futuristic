import os

files = ['index.html', 'services.html', 'portfolio.html', 'pricing.html', 'contact.html', 'industries.html', 'toolkit.html']

chatbot_html = """  <!-- AI Assistant Chatbot UI -->
  <div class="ai-chatbot-interface" id="ai-chatbot">
    <div class="chatbot-header">
      <div class="chatbot-header-left">
        <div class="bot-avatar">
          <img src="logo.png" alt="CybKart AI">
        </div>
        <div class="bot-info">
          <h4>CybKart AI</h4>
          <span class="status"><span class="status-dot"></span> Online</span>
        </div>
      </div>
      <button class="chatbot-close" id="chatbot-close-btn" aria-label="Close Chat">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>
    
    <div class="chatbot-body" id="chatbot-messages">
      <div class="chat-message bot-message">
        <div class="message-content">
          Hello! I am CybKart's AI Architect. How can I help you design your next digital system today?
        </div>
      </div>
    </div>
    
    <div class="chatbot-footer">
      <form id="chatbot-form">
        <input type="text" id="chatbot-input" placeholder="Type your message..." autocomplete="off">
        <button type="submit" class="chatbot-send" aria-label="Send Message">
          <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        </button>
      </form>
    </div>
  </div>

</body>"""

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace </body> with the chatbot html + </body>
        if "<!-- AI Assistant Chatbot UI -->" not in content:
            content = content.replace("</body>", chatbot_html)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
        
print("Appended Chatbot HTML to files.")
