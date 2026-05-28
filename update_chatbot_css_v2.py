import os

with open('css/combined.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the AI Chatbot CSS section
start_marker = "/* ==========================================================================\n   AI ASSISTANT CHATBOT UI\n   ========================================================================== */"
if start_marker in content:
    idx = content.find(start_marker)
    content = content[:idx]

new_css = """
/* ==========================================================================
   AI ASSISTANT CHATBOT UI (DARK LUXURY)
   ========================================================================== */
.ai-chatbot-interface {
  position: fixed;
  bottom: 100px;
  right: 2rem;
  width: 380px;
  height: 600px;
  max-height: calc(100vh - 120px);
  background: rgba(9, 11, 20, 0.85);
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 28px;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), 0 0 40px rgba(0, 85, 255, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 1000;
  opacity: 0;
  visibility: hidden;
  transform: translateY(30px) scale(0.95);
  transform-origin: bottom right;
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}

.ai-chatbot-interface.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
}

.chatbot-header {
  padding: 1.2rem 1.5rem;
  background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  position: relative;
}

.chatbot-header::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0, 140, 255, 0.5), transparent);
}

.chatbot-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.bot-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #090b14, #1a1f35);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 20px rgba(0, 140, 255, 0.4);
}

.bot-avatar img {
  max-width: 100%;
  height: auto;
  filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
}

.bot-info h4 {
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 800;
  margin: 0 0 0.15rem 0;
  letter-spacing: 0.02em;
}

.bot-info .status {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-dot {
  width: 6px;
  height: 6px;
  background: #00ff88;
  border-radius: 50%;
  box-shadow: 0 0 10px #00ff88;
  animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
  0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(0, 255, 136, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
}

.chatbot-close {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.4rem;
  border-radius: 50%;
  transition: var(--transition-fast);
}

.chatbot-close:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  transform: rotate(90deg);
}

.chatbot-body {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  background: transparent;
  scroll-behavior: smooth;
}

.chatbot-body::-webkit-scrollbar {
  width: 4px;
}
.chatbot-body::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 4px;
}

.chat-message {
  display: flex;
  flex-direction: column;
  max-width: 88%;
  animation: message-slide-up 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes message-slide-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.bot-message {
  align-self: flex-start;
}

.user-message {
  align-self: flex-end;
}

.message-content {
  padding: 0.9rem 1.2rem;
  font-size: 0.9rem;
  line-height: 1.6;
  position: relative;
}

.bot-message .message-content {
  background: rgba(255, 255, 255, 0.05);
  color: #e0e0e0;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 4px 18px 18px 18px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.user-message .message-content {
  background: linear-gradient(135deg, #0055ff, #00bfff);
  color: #ffffff;
  border-radius: 18px 18px 4px 18px;
  box-shadow: 0 4px 15px rgba(0, 85, 255, 0.2);
}

.message-time {
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.4);
  margin-top: 0.4rem;
  align-self: flex-end;
}

.bot-message .message-time {
  align-self: flex-start;
}

/* Quick Action Buttons */
.chat-quick-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
  animation: message-slide-up 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  animation-delay: 0.3s;
  opacity: 0;
}

.quick-action-btn {
  background: rgba(0, 140, 255, 0.1);
  border: 1px solid rgba(0, 140, 255, 0.3);
  color: #00bfff;
  padding: 0.5rem 1rem;
  border-radius: 100px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.quick-action-btn:hover {
  background: rgba(0, 140, 255, 0.2);
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 140, 255, 0.2);
}

.chatbot-footer {
  padding: 1.2rem 1.5rem;
  background: rgba(255, 255, 255, 0.02);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

#chatbot-form {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 100px;
  padding: 0.4rem 0.4rem 0.4rem 1.2rem;
  transition: var(--transition-fast);
}

#chatbot-form:focus-within {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(0, 140, 255, 0.5);
  box-shadow: 0 0 0 3px rgba(0, 140, 255, 0.15);
}

#chatbot-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 0.9rem;
  color: #ffffff;
}

#chatbot-input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.chatbot-send {
  background: linear-gradient(135deg, #0055ff, #00bfff);
  color: #ffffff;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition-fast);
  box-shadow: 0 4px 10px rgba(0, 85, 255, 0.3);
}

.chatbot-send:hover {
  transform: scale(1.05) rotate(-10deg);
  box-shadow: 0 6px 15px rgba(0, 85, 255, 0.4);
}

.chatbot-send svg {
  transform: translateX(-1px) translateY(1px);
}

/* Typing Indicator */
.typing-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 0.5rem 0.2rem;
}

.typing-dot {
  width: 5px;
  height: 5px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 50%;
  animation: typing 1.4s infinite ease-in-out both;
}

.typing-dot:nth-child(1) { animation-delay: -0.32s; }
.typing-dot:nth-child(2) { animation-delay: -0.16s; }

@keyframes typing {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

@media (max-width: 480px) {
  .ai-chatbot-interface {
    width: calc(100vw - 2rem);
    height: 85vh;
    right: 1rem;
    bottom: 85px;
  }
}
"""

content += new_css

with open('css/combined.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CSS for Dark Luxury UI.")
