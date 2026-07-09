import zipfile
import os
import xml.etree.ElementTree as ET

docx_file = "TEXT_BILD Inhalte Webseite.docx"
output_dir = "extracted_content"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(docx_file, 'r') as z:
    # Extract media
    for item in z.namelist():
        if item.startswith('word/media/'):
            z.extract(item, output_dir)
            
    # Extract text
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    
    # Namespaces
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    texts = []
    for paragraph in tree.findall('.//w:p', ns):
        p_text = []
        for run in paragraph.findall('.//w:r', ns):
            for t in run.findall('.//w:t', ns):
                if t.text:
                    p_text.append(t.text)
        text = ''.join(p_text)
        texts.append(text)
            
    with open(os.path.join(output_dir, 'extracted_text.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(texts))
    print("Extraction complete. Media and text saved to", output_dir)
