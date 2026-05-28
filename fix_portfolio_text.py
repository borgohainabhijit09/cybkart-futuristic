import os
import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the nuclear option style block
pattern = r'<style>\s*/\*\s*NUCLEAR OPTION TO FIX INVISIBLE TEXT.*?</style>\s*'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

# To be absolutely sure the text is white in bento boxes, let's append a strict rule to combined.css
with open('css/combined.css', 'a', encoding='utf-8') as f:
    f.write("\n.bento-content h3, .bento-content p, .bento-content .stat-val, .bento-content .stat-lbl, .bento-meta .meta-tag, .bento-meta .meta-year { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }\n")

print("Fixed text color in portfolio.html")
