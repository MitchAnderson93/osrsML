# Applied ML using OSRS

## Overview
This repository contains a collection of machine learning projects that I have built for task automation (academic use, see disclaimer at the bottom). 

## Dependencies

| Library | Purpose |
|---------|---------|
| mss | Fast screen grabbing |
| opencv-python | Image processing |
| pillow | For image manipulation |
| pyautogui | Move mouse & click |
| ultralytics | YOLOv8 detection |

## Setup:
```
# Create a virtual environment inside
python3 -m venv venv

# Activate it:
# MacOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install project requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run CLI menu
python processes/task-1.py

# Utilities:
python utils/rename.py
python utils/censor_images.py
```

## Projects

### 1. Image recognition (see Docs/)
A computer vision-based script that performs real-time image analysis and pattern recognition (using OSRS as example)

## DISCLAIMER

This toolkit is developed for academic and educational purposes only. While the examples use OSRS as a case study, using this software to automate gameplay in OSRS is:
- Against Jagex's Terms of Service
- May result in account penalties
- Not recommended or supported

The underlying processes are designed to be generic and adaptable to various real-world applications such as:

- Simple task automation (clicking)
- Text identification/extraction 
- Functions like writing and sending emails
- Many others (see Contributions)

and I can develop any of the above on request. 
