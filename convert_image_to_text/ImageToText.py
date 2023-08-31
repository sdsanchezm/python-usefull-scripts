# pip install pytesseract Pillow

from PIL import Image
import pytesseract

def save_image_text_to_file(image_path, output_file):
    try:
        image = Image.open(image_path)
        
        extracted_text = pytesseract.image_to_string(image)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        
        print("Text extracted and saved to", output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_image_path = "img2.png"
    output_text_file = "img2.txt"
    
    save_image_text_to_file(input_image_path, output_text_file)
