import mss
import numpy as np
import cv2
import pyautogui
import time
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('models/crab.pt') 

# Set screen capture area (entire screen for now)
# Assumes the client is running on a 1920x1080 monitor as first screen.
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

# Initialize mss for screen capture
sct = mss.mss()

def capture_screen():
    sct_img = sct.grab(monitor)
    frame = np.array(sct_img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

def detect_crab(frame):
    # Predict with YOLO
    results = model.predict(frame, imgsz=640, conf=0.5)
    detections = results[0].boxes.xywh.cpu().numpy()  # center_x, center_y, width, height

    if len(detections) == 0:
        return None
    
    # Return center of first detection (you can improve this later)
    center_x, center_y, w, h = detections[0][:4]
    return int(center_x), int(center_y)

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Main loop
try:
    while True:
        frame = capture_screen()

        target = detect_crab(frame)

        if target:
            x, y = target
            print(f"Crab found at ({x}, {y}), attacking!")
            click(x, y)
            time.sleep(6)  # Wait during combat
        else:
            print("No crab found, scanning...")
            time.sleep(1)  # Try again faster

except KeyboardInterrupt:
    print("Stopped.")
