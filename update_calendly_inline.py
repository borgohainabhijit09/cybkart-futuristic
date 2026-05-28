import os
import re

calendly_url = "https://calendly.com/borgohainabhijit09/book-free-strategy-call"

calendly_iframe_html = f"""<div style="border-radius:12px; overflow:hidden; margin-top:10px; background:#fff;"><iframe src="{calendly_url}?hide_gdpr_banner=1&hide_landing_page_details=1&background_color=ffffff&text_color=090b14&primary_color=0055ff" width="100%" height="400" frameborder="0"></iframe></div>"""

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We have three places where calendly links are referenced in the mock logic:
# 1. "Select a Time ↗"
# 2. "Book Strategy Call ↗"
# Also inside the System prompt for OpenAI, we should add instructions to output the iframe.

# For the Mock Engine:
# Replace the Calendly anchor tags with the iframe HTML.
# But wait, we can just replace `<a href="https://calendly.com/" target="_blank" class="quick-action-btn" style="display:inline-block; margin-top:10px; background:#0055ff; color:#fff; text-decoration:none; border:none;">Select a Time ↗</a>`
# with the iframe string.

content = re.sub(r'<a href="https://calendly.com/".*?Select a Time ↗</a>', calendly_iframe_html, content)
content = re.sub(r'<a href="https://calendly.com/".*?Book Strategy Call ↗</a>', calendly_iframe_html, content)

# Update OpenAI System Prompt
sys_prompt_old = "You are the CybKart Global AI Architect, a premium digital growth advisor and smart business consultant. You speak confidently, naturally, and proactively. You never sound robotic or use generic phrases like 'How can I help you?'. Your goal is to guide visitors, recommend services, and eventually help them book a consultation via Calendly. You understand CybKart's services (Premium websites, AI chatbots, Lead gen, Automations, SEO) and pricing (Starter, Professional, Premium). Infer context naturally, don't ask repetitive questions. Suggest solutions based on the user's industry. Handle objections gracefully. Keep responses concise, engaging, and premium."

sys_prompt_new = f"""You are the CybKart Global AI Architect, a premium digital growth advisor and smart business consultant. You speak confidently, naturally, and proactively. You never sound robotic or use generic phrases like 'How can I help you?'. Your goal is to guide visitors, recommend services, and eventually help them book a consultation via Calendly. When a user is ready to book or asks for a meeting, YOU MUST output EXACTLY this HTML block so they can book inline in the chat: {calendly_iframe_html} . Do not use standard links for booking. You understand CybKart's services (Premium websites, AI chatbots, Lead gen, Automations, SEO) and pricing (Starter, Professional, Premium). Infer context naturally, don't ask repetitive questions. Suggest solutions based on the user's industry. Handle objections gracefully. Keep responses concise, engaging, and premium."""

content = content.replace(sys_prompt_old, sys_prompt_new)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js with inline Calendly booking.")
