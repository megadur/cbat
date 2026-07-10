import os
import re

header_old = '''<a href="index.html" class="logo-link">
                <img src="assets/img/logo.png" alt="Charlotte Blickensdorf - Alexander-Technik Logo" class="logo-img">
            </a>'''
            
header_new = '''<a href="index.html" class="logo">
                Charlotte Blickensdorf
                <span>Alexander-Technik</span>
            </a>'''

footer_old = '''<div class="footer-col">
                <h4>Charlotte Blickensdorf</h4>
                <p>Alexander-Technik<br>Berlin & Hohenbüssow</p>
            </div>'''

footer_new = '''<div class="footer-col">
                <img src="assets/img/logo.png" alt="Charlotte Blickensdorf Logo" style="width: 80px; height: 80px; margin-bottom: 15px; border-radius: 4px;">
                <h4>Charlotte Blickensdorf</h4>
                <p>Alexander-Technik<br>Berlin & Hohenbüssow</p>
            </div>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(header_old, header_new)
        content = content.replace(footer_old, footer_new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
