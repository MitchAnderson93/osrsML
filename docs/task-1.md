### Image Recognition System
A computer vision-based system that performs real-time image analysis and pattern recognition. 

This module can:
- Detect and classify specific UI elements
- Process screen captures for pattern matching
- Perform automated visual analysis

![Training Process](./training.png)
![Training Process 2](./training-2.png)

### FILES

| File | Purpose |
|---------|---------|
| processes/task-1.py | Terminal script |
| models/crab_model.pt | Identify sandcrabs |
| training/crab/ | Image training data |

### Commands for training model (requires exported dataset):
```
# dataset exported from roboflow in our uncommited /res folder (unzipped):
yolo detect train data=/Users/X/osrs/imgidentifier/res/sand_crabs.v3-sand_crabs_dataset_2.0-640-.yolov8/data.yaml model=yolov8n.pt epochs=100 imgsz=640

```
