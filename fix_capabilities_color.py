import re

with open('css/combined.css', 'r', encoding='utf-8') as f:
    content = f.read()

override_css = """
/* Fix for Capabilities Text (Overriding the Portfolio White Text rule) */
.bento-capabilities-section .bento-title,
.bento-capabilities-section .bento-text,
.bento-capabilities-section .bento-content h3,
.bento-capabilities-section .bento-content p {
  color: #0b0f19 !important;
  -webkit-text-fill-color: #0b0f19 !important;
}

.bento-capabilities-section .bento-pillar {
  color: #0055ff !important;
  -webkit-text-fill-color: #0055ff !important;
}
"""

with open('css/combined.css', 'w', encoding='utf-8') as f:
    f.write(content + "\n" + override_css)

print("Applied CSS fix for Core Capabilities font color.")
