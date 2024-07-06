# Detect Crosswalks

The following mentioned functional requirements are addressed in this directory.

1. **Detect Crosswalks**: Utilizes a YOLOv5 model to detect crosswalks using satellite images and a camera module.

## Structure

- `crosswalk_detection_model_training/`: Powershell containing the codes for training the YOLOv5 model for detecting crosswalks.
- `Crosswalk_YOLOv5_model_testing/`: Jupyter source file (notebook) containing the codes testing the trained model for one image and set of images.
- `performance evaluation of YOLOv5 model for crosswalk detection using validation dataset/`:  Powershell containing the codes for validating the trained model.
