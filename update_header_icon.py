import os

header_old = '''<a href="index.html" class="logo">
                Charlotte Blickensdorf
                <span>Alexander-Technik</span>
            </a>'''

header_new = '''<a href="index.html" class="logo-wrapper">
                <img src="assets/img/logo_icon.png" alt="Icon" class="logo-icon">
                <div class="logo">
                    Charlotte Blickensdorf
                    <span>Alexander-Technik</span>
                </div>
            </a>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(header_old, header_new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
