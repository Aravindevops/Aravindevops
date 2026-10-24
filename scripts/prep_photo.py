import cv2
import numpy as np
from rembg import remove
from PIL import Image
import sys
import os

def prep_photo(input_path, output_path="source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return

    print("1. Removing background...")
    input_image = Image.open(input_path)
    subject_only = remove(input_image)
    
    print("2. Applying OpenCV CLAHE contrast boost...")
    open_cv_image = np.array(subject_only)
    
    # Extract RGB and Alpha channels
    if open_cv_image.shape[2] == 4:
        b, g, r, a = cv2.split(open_cv_image)
        rgb_img = cv2.merge([b, g, r])
    else:
        rgb_img = open_cv_image
        a = np.ones(rgb_img.shape[:2], dtype=np.uint8) * 255

    gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
    
    # Boost local contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrasted = clahe.apply(gray)
    
    print("3. Compositing onto pure white background...")
    white_bg = np.ones_like(contrasted) * 255
    alpha_mask = a / 255.0
    
    final_img = (contrasted * alpha_mask + white_bg * (1 - alpha_mask)).astype(np.uint8)
    
    cv2.imwrite(output_path, final_img)
    print(f"Done! Saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py <source-photo.jpg>")
    else:
        prep_photo(sys.argv[1])