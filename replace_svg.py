import os, re

files = ['index.html', 'services.html', 'portfolio.html', 'pricing.html', 'contact.html', 'industries.html', 'toolkit.html']
header_pattern = re.compile(r'<svg viewBox="0 0 160 120" width="40" height="30" fill="none" xmlns="http://www.w3.org/2000/svg">.*?</svg>', re.DOTALL)
footer_pattern = re.compile(r'<svg viewBox="0 0 160 120" width="36" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">.*?</svg>', re.DOTALL)

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header SVG
        content = header_pattern.sub('<img src="logo.png" alt="CybKart Logo" class="brand-logo-img" style="height: 40px; width: auto;">', content)
        
        # Replace footer SVG
        content = footer_pattern.sub('<img src="logo.png" alt="CybKart Logo" class="brand-logo-img" style="height: 28px; width: auto;">', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print('Replaced inline SVGs with image placeholders.')
