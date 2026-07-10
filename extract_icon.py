from PIL import Image

def extract_icon(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Crop the top portion, assuming the text is at the bottom
    # Usually the icon is vertically centered in the top 75%
    # Let's crop a square around the center of the top 75%
    left = width * 0.1
    top = height * 0.1
    right = width * 0.9
    bottom = height * 0.75
    
    img_cropped = img.crop((left, top, right, bottom))
    
    # Make near-white transparent
    datas = img_cropped.getdata()
    newData = []
    for item in datas:
        # Check if the pixel is near white
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img_cropped.putdata(newData)
    
    # Resize to a reasonable icon size, e.g., 100px height
    aspect = img_cropped.width / img_cropped.height
    new_h = 100
    new_w = int(new_h * aspect)
    img_cropped = img_cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    img_cropped.save(output_path, "PNG")

if __name__ == '__main__':
    input_file = r'C:\Users\DonTillo\.gemini\antigravity\brain\ab24b32a-ee49-40dd-875b-424778b7014e\logo_proposal_1_1783664254442.png'
    output_file = r'c:\data\code\github\megadur\CBAT\assets\img\logo_icon.png'
    extract_icon(input_file, output_file)
