import os

footer_old = '''<div class="footer-col">
                <img src="assets/img/logo.png" alt="Charlotte Blickensdorf Logo" style="width: 80px; height: 80px; margin-bottom: 15px; border-radius: 4px;">
                <h4>Charlotte Blickensdorf</h4>
                <p>Alexander-Technik<br>Berlin & Hohenbüssow</p>
            </div>'''

footer_new = '''<div class="footer-col" style="max-width: 120px;">
                <img src="assets/img/logo.png" alt="Charlotte Blickensdorf Logo" style="width: 100px; height: 100px; border-radius: 8px;">
            </div>
            <div class="footer-col">
                <h4>Charlotte Blickensdorf</h4>
                <p>Alexander-Technik<br>Berlin & Hohenbüssow</p>
            </div>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(footer_old, footer_new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
