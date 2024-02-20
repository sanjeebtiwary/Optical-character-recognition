from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\KIIT\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytesseract'

def ocr(image_path):
    try:
        # Open an image file
        img = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(img)

        # Print the extracted text
        print("Extracted Text:")
        print(text)

    except Exception as e:
        print(f"Error: {e}")

# Replace 'your_image_path.png' with the path to your image file
image_path = 'image_01.png'
ocr(image_path)

