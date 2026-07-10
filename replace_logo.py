import os
import re

old_pattern = re.compile(r'<a href="index\.html" class="logo">\s*Charlotte Blickensdorf\s*<span>Alexander-Technik</span>\s*</a>', re.DOTALL)
new_content = '''<a href="index.html" class="logo-link">
                <img src="assets/img/logo.png" alt="Charlotte Blickensdorf - Alexander-Technik Logo" class="logo-img">
            </a>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = old_pattern.sub(new_content, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
