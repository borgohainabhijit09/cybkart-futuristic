import os

css_content = """

/* ==========================================================================
   AI ASSISTANT CHATBOT UI
   ========================================================================== */
.ai-chatbot-interface {
  position: fixed;
  bottom: 100px;
  right: 2rem;
  width: 360px;
  height: 500px;
  max-height: calc(100vh - 120px);
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(9, 11, 20, 0.08);
  border-radius: 24px;
  box-shadow: 0 20px 50px rgba(9, 11, 20, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px) scale(0.95);
  transform-origin: bottom right;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}

.ai-chatbot-interface.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
}

.chatbot-header {
  padding: 1.2rem 1.5rem;
  background: linear-gradient(135deg, #090b14, #1a1f35);
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.chatbot-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.bot-avatar {
  width: 36px;
  height: 36px;
  background: #ffffff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  box-shadow: 0 0 15px rgba(0, 140, 255, 0.3);
}

.bot-avatar img {
  max-width: 100%;
  height: auto;
}

.bot-info h4 {
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0 0 0.1rem 0;
}

.bot-info .status {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-dot {
  width: 6px;
  height: 6px;
  background: #00ff88;
  border-radius: 50%;
  box-shadow: 0 0 8px #00ff88;
  animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
  0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(0, 255, 136, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
}

.chatbot-close {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.4rem;
  border-radius: 50%;
  transition: var(--transition-fast);
}

.chatbot-close:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
}

.chatbot-body {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  background: rgba(250, 250, 252, 0.5);
}

.chatbot-body::-webkit-scrollbar {
  width: 4px;
}
.chatbot-body::-webkit-scrollbar-thumb {
  background: rgba(9, 11, 20, 0.1);
  border-radius: 4px;
}

.chat-message {
  display: flex;
  max-width: 85%;
  animation: message-slide-up 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes message-slide-up {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.bot-message {
  align-self: flex-start;
}

.user-message {
  align-self: flex-end;
}

.bot-message .message-content {
  background: #ffffff;
  color: #090b14;
  border: 1px solid rgba(9, 11, 20, 0.05);
  border-radius: 4px 16px 16px 16px;
  padding: 0.8rem 1.2rem;
  font-size: 0.85rem;
  line-height: 1.5;
  box-shadow: 0 4px 15px rgba(9, 11, 20, 0.02);
}

.user-message .message-content {
  background: linear-gradient(135deg, #0055ff, #00bfff);
  color: #ffffff;
  border-radius: 16px 16px 4px 16px;
  padding: 0.8rem 1.2rem;
  font-size: 0.85rem;
  line-height: 1.5;
  box-shadow: 0 4px 15px rgba(0, 85, 255, 0.2);
}

.chatbot-footer {
  padding: 1rem 1.5rem;
  background: #ffffff;
  border-top: 1px solid rgba(9, 11, 20, 0.05);
}

#chatbot-form {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(9, 11, 20, 0.02);
  border: 1px solid rgba(9, 11, 20, 0.05);
  border-radius: 100px;
  padding: 0.3rem 0.3rem 0.3rem 1.2rem;
  transition: var(--transition-fast);
}

#chatbot-form:focus-within {
  background: #ffffff;
  border-color: var(--color-purple);
  box-shadow: 0 0 0 3px rgba(0, 140, 255, 0.1);
}

#chatbot-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 0.85rem;
  color: #090b14;
}

#chatbot-input::placeholder {
  color: var(--color-text-muted);
}

.chatbot-send {
  background: var(--color-purple);
  color: #ffffff;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition-fast);
}

.chatbot-send:hover {
  background: #0044cc;
  transform: scale(1.05);
}

@media (max-width: 480px) {
  .ai-chatbot-interface {
    width: calc(100vw - 2rem);
    right: 1rem;
    bottom: 85px;
  }
}
"""

with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Appended Chatbot CSS to combined.css")
