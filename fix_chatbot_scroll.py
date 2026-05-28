import os

files = ['index.html', 'services.html', 'portfolio.html', 'pricing.html', 'contact.html', 'industries.html', 'toolkit.html']

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the chatbot body div to add data-lenis-prevent
        content = content.replace('<div class="chatbot-body" id="chatbot-messages">', '<div class="chatbot-body" id="chatbot-messages" data-lenis-prevent>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added data-lenis-prevent to chatbot-messages div.")
