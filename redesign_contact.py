import re
import os

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Nuclear option
pattern = r'<style>\s*/\*\s*NUCLEAR OPTION TO FIX INVISIBLE TEXT.*?</style>\s*'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# 2. Update the contact details stack
new_details_stack = """
            <div class="contact-details-stack">
              <div class="contact-detail-item">
                <span class="detail-icon">✉️</span>
                <div>
                  <div class="detail-lbl">Email</div>
                  <a href="mailto:info@cybkartglobal.com" class="detail-val" style="color: #0055ff; text-decoration: none;">info@cybkartglobal.com</a>
                </div>
              </div>
              <div class="contact-detail-item">
                <span class="detail-icon">📞</span>
                <div>
                  <div class="detail-lbl">Phone</div>
                  <a href="tel:8446991255" class="detail-val" style="color: #0b0f19; text-decoration: none; font-weight: 600;">844-699-1255</a>
                </div>
              </div>
              <div class="contact-detail-item">
                <span class="detail-icon">🏢</span>
                <div>
                  <div class="detail-lbl">Headquarters</div>
                  <div class="detail-val" style="color: #475569; line-height: 1.5;">1309 Coffeen Ave, Sheridan,<br>Wyoming 82801, USA</div>
                </div>
              </div>
            </div>
"""

# Replace the existing stack
start_marker = '<div class="contact-details-stack">'
start_idx = content.find(start_marker)

end_marker = '            <!-- Virtual floating booking calendar card inside contact -->'
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_details_stack + content[end_idx:]
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Contact page details updated.")
else:
    print("Could not find the contact details stack.")
