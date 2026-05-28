import os

js_content = """
// ==========================================================================
// CYBKART ADVANCED AI ASSISTANT (HYBRID ENGINE)
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  const chatWidget = document.querySelector('.floating-chat-widget');
  const chatBotUI = document.getElementById('ai-chatbot');
  const chatCloseBtn = document.getElementById('chatbot-close-btn');
  const chatForm = document.getElementById('chatbot-form');
  const chatInput = document.getElementById('chatbot-input');
  const chatMessages = document.getElementById('chatbot-messages');

  // Insert your OpenAI API Key here for true AI capabilities
  // Note: In production, route this through your backend to protect the key.
  const OPENAI_API_KEY = ""; 

  // Conversation Memory System
  let conversationHistory = [];
  let userContext = {
    industry: null,
    servicesDiscussed: [],
    pricingDiscussed: false,
    objectionsHandled: []
  };

  if (chatWidget && chatBotUI) {
    chatWidget.addEventListener('click', () => {
      chatBotUI.classList.add('active');
      if (conversationHistory.length === 0) {
        initiateGreeting();
      }
    });

    chatCloseBtn.addEventListener('click', () => {
      chatBotUI.classList.remove('active');
    });

    const formatTime = () => {
      const now = new Date();
      return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    };

    const addMessageToUI = (text, sender, isHTML = false) => {
      const msgDiv = document.createElement('div');
      msgDiv.className = `chat-message ${sender}-message`;
      
      const contentDiv = document.createElement('div');
      contentDiv.className = 'message-content';
      if (isHTML) {
        contentDiv.innerHTML = text;
      } else {
        contentDiv.textContent = text;
      }

      const timeDiv = document.createElement('div');
      timeDiv.className = 'message-time';
      timeDiv.textContent = formatTime();

      msgDiv.appendChild(contentDiv);
      msgDiv.appendChild(timeDiv);
      chatMessages.appendChild(msgDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      
      return contentDiv;
    };

    const showTypingIndicator = () => {
      const typingDiv = document.createElement('div');
      typingDiv.className = 'chat-message bot-message typing-indicator-msg';
      typingDiv.innerHTML = `
        <div class="message-content" style="padding: 0.6rem 1rem;">
          <div class="typing-indicator">
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
          </div>
        </div>
      `;
      chatMessages.appendChild(typingDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      return typingDiv;
    };

    const initiateGreeting = () => {
      const typing = showTypingIndicator();
      setTimeout(() => {
        typing.remove();
        addMessageToUI("Hello! I'm the CybKart digital growth consultant. Are you looking to upgrade your current digital presence, or building something entirely new today?", 'bot');
        conversationHistory.push({ role: 'assistant', content: "Hello! I'm the CybKart digital growth consultant. Are you looking to upgrade your current digital presence, or building something entirely new today?" });
      }, 1000);
    };

    const simulateStreamingText = (element, text, speed = 15, onComplete) => {
      element.innerHTML = '';
      let i = 0;
      // Handle HTML tags properly during streaming
      const isHTML = text.includes('<');
      if (isHTML) {
        // If it's HTML, we just fade it in smoothly instead of typing letter by letter to prevent broken tags
        element.style.opacity = 0;
        element.innerHTML = text;
        let op = 0;
        const fade = setInterval(() => {
          op += 0.1;
          element.style.opacity = op;
          if (op >= 1) {
            clearInterval(fade);
            if (onComplete) onComplete();
          }
        }, 30);
      } else {
        const interval = setInterval(() => {
          element.textContent += text.charAt(i);
          chatMessages.scrollTop = chatMessages.scrollHeight;
          i++;
          if (i >= text.length) {
            clearInterval(interval);
            if (onComplete) onComplete();
          }
        }, speed);
      }
    };

    const getOpenAIResponse = async (userMessage) => {
      try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${OPENAI_API_KEY}`
          },
          body: JSON.stringify({
            model: 'gpt-4o', // Or gpt-3.5-turbo
            messages: [
              {
                role: 'system',
                content: `You are the CybKart Global AI Architect, a premium digital growth advisor and smart business consultant. You speak confidently, naturally, and proactively. You never sound robotic or use generic phrases like 'How can I help you?'. Your goal is to guide visitors, recommend services, and eventually help them book a consultation via Calendly. You understand CybKart's services (Premium websites, AI chatbots, Lead gen, Automations, SEO) and pricing (Starter, Professional, Premium). Infer context naturally, don't ask repetitive questions. Suggest solutions based on the user's industry. Handle objections gracefully. Keep responses concise, engaging, and premium.`
              },
              ...conversationHistory,
              { role: 'user', content: userMessage }
            ],
            temperature: 0.7,
            max_tokens: 150
          })
        });

        if (!response.ok) throw new Error('API Error');
        const data = await response.json();
        return data.choices[0].message.content;
      } catch (error) {
        // Fallback to advanced local mock engine
        return getSmartMockResponse(userMessage);
      }
    };

    const getSmartMockResponse = (text) => {
      const lowerText = text.toLowerCase();
      
      // Update Context
      if (lowerText.match(/(detailing|roofing|landscaping|hvac|cleaning|dental|restaurant)/)) {
        const match = lowerText.match(/(detailing|roofing|landscaping|hvac|cleaning|dental|restaurant)/);
        userContext.industry = match[0];
      }

      // Memory & Intent Logic
      
      // Intent: Booking / Consultation
      if (lowerText.match(/(book|appointment|call|meeting|calendly|talk|strategy|schedule)/)) {
        return `Excellent move. Let's get you on a quick strategy call with our lead systems architect so we can map out a specific growth plan for your business.<br><br><a href="https://calendly.com/" target="_blank" class="quick-action-btn" style="display:inline-block; margin-top:10px; background:#0055ff; color:#fff; text-decoration:none; border:none;">Select a Time ↗</a>`;
      }
      
      // Intent: Services / Features
      if (lowerText.match(/(service|web|design|seo|automation|build|create|offer|do you do)/)) {
        userContext.servicesDiscussed.push('general');
        if (userContext.industry) {
          return `For ${userContext.industry} businesses, we typically implement high-converting landing pages tied directly into automated lead-capture and booking systems. It stops leads from falling through the cracks. Are you currently running any specific software to handle bookings?`;
        }
        return `We engineer premium digital systems—not just basic websites. We build conversion-focused web layouts, integrate AI chatbots for 24/7 lead capture, and set up automated review generation. What's the main bottleneck in your current digital setup?`;
      }
      
      // Intent: Pricing
      if (lowerText.match(/(price|pricing|cost|how much|fee|charge|budget|package)/)) {
        userContext.pricingDiscussed = true;
        return `We scale our systems based on what your operations actually need. We have a Starter tier for essential digital presence, a Professional tier optimized for active lead generation, and our Premium tier which fully integrates AI, CRM, and advanced automations.<br><br>The best way to get an exact quote is a quick 15-minute discovery audit. Shall I drop the link to schedule that?`;
      }

      // Intent: Objection - Expensive
      if (lowerText.match(/(expensive|too much|high|not in budget)/)) {
        if (userContext.objectionsHandled.includes('price')) {
          return `I completely understand. We always advise starting where it makes financial sense and scaling up as the new system generates ROI.`;
        }
        userContext.objectionsHandled.push('price');
        return `Totally understandable. Most businesses we work with usually see this as a long-term lead generation investment rather than just a website expense. The automation alone often saves enough administrative hours to pay for itself.`;
      }

      // Intent: Objection - Already have a website
      if (lowerText.match(/(already have|existing site|got a website)/)) {
        return `That actually puts you in a great position. Many of our clients come to us because their existing site looks a bit outdated, loads slowly, or simply isn't generating enough qualified leads. We can audit your current site on a quick call if you'd like?`;
      }

      // Smart Context Inference based on Industry
      if (userContext.industry && !userContext.servicesDiscussed.includes('industry_pitch')) {
        userContext.servicesDiscussed.push('industry_pitch');
        return `Nice — ${userContext.industry} businesses usually benefit a lot from visual-focused websites with before/after galleries, mobile booking, and automated lead capture. Is your current setup capturing leads automatically, or is it mostly a manual process?`;
      }

      // Fallback Conversational Response
      return `I see. To give you the most accurate roadmap for your specific growth targets, it's best we run a quick strategic audit on a brief call. <br><br><a href="https://calendly.com/" target="_blank" class="quick-action-btn" style="display:inline-block; margin-top:10px; background:#0055ff; color:#fff; text-decoration:none; border:none;">Book Strategy Call ↗</a>`;
    };

    chatForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if (!text) return;

      // Add user message
      addMessageToUI(text, 'user');
      chatInput.value = '';
      
      // Add to history
      conversationHistory.push({ role: 'user', content: text });
      
      // Limit history to last 10 messages for context window
      if (conversationHistory.length > 10) {
        conversationHistory = conversationHistory.slice(conversationHistory.length - 10);
      }

      // Show typing indicator
      const typingMsg = showTypingIndicator();

      // Process response
      let responseContent;
      if (OPENAI_API_KEY) {
        responseContent = await getOpenAIResponse(text);
      } else {
        // Simulate network delay for mock engine
        await new Promise(resolve => setTimeout(resolve, 800 + Math.random() * 600));
        responseContent = getSmartMockResponse(text);
      }

      typingMsg.remove();
      
      // Add Bot Message container
      const contentDiv = addMessageToUI('', 'bot', true);
      
      // Simulate Streaming Effect
      simulateStreamingText(contentDiv, responseContent, 15, () => {
        // Save to history once streamed
        conversationHistory.push({ role: 'assistant', content: responseContent });
      });
    });
  }
});
"""

import re

# Read app.js and replace the old chatbot logic
with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to remove the old chatbot logic. It starts at "// CybKart Advanced AI Chatbot Logic" or similar.
idx = content.find("// CybKart Advanced AI Chatbot Logic")
if idx == -1:
    idx = content.find("document.addEventListener('DOMContentLoaded', () => {\n  // Chatbot Initialization")

if idx != -1:
    content = content[:idx]

content += js_content

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js with Ultra-Premium AI Chatbot Logic.")
