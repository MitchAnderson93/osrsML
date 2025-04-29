import os
import random
from pathlib import Path

def rename_images(directory='res'):
    path = Path(directory)
    
    if not path.exists():
        print(f"Directory {directory} not found")
        return
    
    # Get all PNG files
    png_files = list(path.glob('*.png'))
    
    # Generate random numbers without duplicates
    random_numbers = random.sample(range(1, len(png_files) + 1), len(png_files))
    
    # Create backup of original names
    original_names = {}
    
    # Rename files with temporary names first (to avoid conflicts)
    for file in png_files:
        temp_name = path / f'TEMP_{file.name}'
        file.rename(temp_name)
        original_names[temp_name] = file
    
    # Rename to final random numbers
    for temp_file, i in zip(original_names.keys(), random_numbers):
        new_name = path / f'crab_{i:03d}.png'
        Path(temp_file).rename(new_name)
        print(f'Renamed: {original_names[temp_file].name} → {new_name.name}')

if __name__ == '__main__':
    rename_images()