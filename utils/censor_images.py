import cv2
import numpy as np
from pathlib import Path

def censor_images(directory='res'):
    path = Path(directory)
    
    if not path.exists():
        print(f"Directory {directory} not found")
        return
    
    # Get all PNG files
    png_files = list(path.glob('*.png'))
    
    for file in png_files:
        # Read image
        img = cv2.imread(str(file))
        
        # Get image dimensions
        height, width = img.shape[:2]
        
        # Define region to censor
        box_width = 1000  # Doubled from 500
        box_height = 300  # Increased by 25% from 200
        # Position at bottom left
        x1 = 0
        x2 = box_width
        y1 = height - box_height
        y2 = height
        
        # Draw black rectangle
        cv2.rectangle(img, 
                     (x1, y1),   # Top left corner
                     (x2, y2),   # Bottom right corner
                     (0, 0, 0),  # Black color
                     -1)         # Filled rectangle
        
        # Save censored image
        cv2.imwrite(str(file), img)
        print(f'Censored: {file.name}')

if __name__ == '__main__':
    censor_images()