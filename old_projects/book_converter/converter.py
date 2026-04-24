import fitz
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2


def pdf_to_images(pdf_path):
    """Convert PDF pages to images."""
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images


def preprocess_image(image):
    """Preprocess an image to improve OCR accuracy."""
    # Convert to grayscale
    img_gray = image.convert('L')

    # Apply Gaussian blur to reduce noise
    img_blur = img_gray.filter(ImageFilter.GaussianBlur(radius=1))

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img_blur)
    img_enhanced = enhancer.enhance(2)

    # Apply adaptive thresholding to handle varying lighting
    img_array = np.array(img_enhanced)
    img_thresh = cv2.adaptiveThreshold(
        img_array, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # Apply morphological operations to remove noise and improve text areas
    kernel = np.ones((3, 3), np.uint8)
    img_morph = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

    # Apply additional image processing techniques
    # Sharpen the image to enhance text edges
    img_sharp = cv2.filter2D(
        img_morph, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    )

    # Convert back to PIL image
    img_sharp = Image.fromarray(img_sharp)

    return img_sharp


def save_text_to_markdown(texts, markdown_path):
    """Save extracted text to a Markdown file."""
    with open(markdown_path, 'w', encoding='utf-8') as f:
        for text in texts:
            f.write(text + '\n\n')


def save_image(image, image_path):
    """Save a single image to a file."""
    image.save(image_path)


def recognize_text(image):
    """Recognize text in a single image using Tesseract."""
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Experiment with different OCR settings
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(
        image, lang='rus+eng', config=custom_config
    )
    return text


def process_pdf(pdf_path, markdown_path):
    """Extract images from PDF, preprocess them, recognize text, and save to Markdown."""
    images = pdf_to_images(pdf_path)
    texts = []
    for i, image in enumerate(images):
        try:
            # Preprocess the image
            preprocessed_image = preprocess_image(image)

            # Save the preprocessed image (optional, for debugging)
            # save_image(preprocessed_image, f"preprocessed_{i}.png")

            # Recognize text in the preprocessed image
            text = recognize_text(preprocessed_image)
            if text.strip():  # Only add non-empty text
                texts.append(text)
        except Exception as e:
            print(f"Failed to process image {i}: {e}")
            continue

    # Save the recognized text to a Markdown file
    save_text_to_markdown(texts, markdown_path)
