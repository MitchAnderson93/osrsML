import numpy as np
import cv2
import pyautogui
import time
import os
import random
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('./models/sandcrab.pt')

# Define monitor region manually (full screen)
monitor = {
    "left": 0,
    "top": 0,
    "width": 3840,
    "height": 2160
}

def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame

def human_delay():
    """Add random delay to mimic human behavior"""
    base_delay = random.uniform(0.1, 0.3)
    micro_delay = random.uniform(0.001, 0.099)
    return base_delay + micro_delay

def detect_crab(frame):
    results = model.predict(frame, imgsz=640, conf=0.2)
    
    if results and results[0].boxes:
        # Get all detections with their class IDs
        boxes = results[0].boxes.xywh.cpu().numpy()
        class_ids = results[0].boxes.cls.cpu().numpy()
        
        # Split detections into crabs and ignores
        crabs = []
        ignores = []
        
        for box, class_id in zip(boxes, class_ids):
            if class_id == 0:  # Assuming 0 is crab class
                crabs.append(box)
            elif class_id == 1:  # Assuming 1 is ignore class
                ignores.append(box)
                
        return {
            'crabs': np.array(crabs) if crabs else None,
            'ignores': np.array(ignores) if ignores else None
        }
    return {'crabs': None, 'ignores': None}

def click(x, y):
    """Click with varied, human-like mouse movements"""
    absolute_x = monitor["left"] + x
    absolute_y = monitor["top"] + y
    
    # Randomize the approach angle and offset
    angle = random.uniform(0, 2 * np.pi)
    radius = random.uniform(1, 4)  # Varied offset distance
    
    # Calculate offset using polar coordinates
    offset_x = radius * np.cos(angle)
    offset_y = radius * np.sin(angle)
    
    # Move to target with dynamic offset
    pyautogui.moveTo(
        absolute_x + offset_x, 
        absolute_y + offset_y,
        duration=random.uniform(0.1, 0.2)  # Varied movement speed
    )
    
    # Slight pre-click wiggle (30% chance)
    if random.random() < 0.3:
        wiggle_x = random.uniform(-2, 2)
        wiggle_y = random.uniform(-2, 2)
        pyautogui.moveRel(wiggle_x, wiggle_y, duration=0.1)
    
    # Click with random duration
    pyautogui.click(duration=random.uniform(0.01, 0.05))
    
    # Post-click movement (varied distance and direction)
    if random.random() < 0.7:  # 70% chance of post-click movement
        drift_angle = random.uniform(0, 2 * np.pi)
        drift_distance = random.uniform(2, 8)
        drift_x = drift_distance * np.cos(drift_angle)
        drift_y = drift_distance * np.sin(drift_angle)
        pyautogui.moveRel(drift_x, drift_y, duration=random.uniform(0.1, 0.4))

def rotate_camera(direction):
    """Rotate camera using arrow keys"""
    key = {
        'left': 'left',
        'right': 'right',
        'up': 'up',
        'down': 'down'
    }
    pyautogui.keyDown(key[direction])
    time.sleep(0.5)  # Hold key for half second
    pyautogui.keyUp(key[direction])

def find_closest_to_center(detections, center_x, center_y):
    """Find detection closest to screen center"""
    if not len(detections):
        return None
    
    distances = []
    for det in detections:
        x, y = det[:2]  # Get center x,y of detection
        distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        distances.append((distance, det))
    
    return min(distances, key=lambda x: x[0])[1]

# Main loop
try:
    rotation_count = 0
    screen_center_x = monitor["width"] // 2
    screen_center_y = monitor["height"] // 2

    while True:
        frame = capture_screen()
        detections = detect_crab(frame)
        
        if detections['ignores'] is not None:
            print("Other player detected, rotating...")
            rotate_camera('right')
            time.sleep(human_delay())
            continue
            
        if detections['crabs'] is not None:
            crabs = detections['crabs']
            print(f"Detected {len(crabs)} crabs")
            
            # Find closest crab to center
            closest_crab = find_closest_to_center(crabs, screen_center_x, screen_center_y)
            
            if closest_crab is not None:
                center_x, center_y = closest_crab[:2]
                
                # Add human-like delay before clicking
                time.sleep(human_delay())
                click(int(center_x), int(center_y))
                
                # Random post-click delay
                time.sleep(random.uniform(5.8, 6.2))
                rotation_count = 0
        else:
            print("No crabs found, rotating camera...")
            rotation_count += 1
            
            # Rotate with random timing
            rotate_camera('right')
            time.sleep(human_delay())
            
            if rotation_count >= 4:
                rotation_count = 0
                time.sleep(random.uniform(0.8, 1.2))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    cv2.destroyAllWindows()
