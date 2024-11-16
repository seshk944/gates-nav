import cv2
import numpy as np 


import cv2
import os

def image_to_map(file_path, threshold=200, scale=10):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return None
    
    # Step 1: Load the image
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could not read the image. Check the file format or path.")
        return None

    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Step 3: Apply threshold to distinguish walls from hallways
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    
    # Step 4: Resize the image to reduce complexity (optional)
    height, width = binary.shape
    binary_resized = cv2.resize(binary, (width // scale, height // scale), interpolation=cv2.INTER_NEAREST)
    
    # Step 5: Convert to ASCII representation
    map_representation = []
    for row in binary_resized:
        line = ''
        for pixel in row:
            if pixel == 0:  # Black areas (walls/rooms)
                line += 'X'
            else:  # White areas (hallways)
                line += '.'
        map_representation.append(line)
    
    return "\n".join(map_representation)

# Usage example
# this is not working bruh
file_path = 'C:\Users\saish\OneDrive\Desktop\sample-image.jpeg'
map_string = image_to_map(file_path)
if map_string:
    print(map_string)
