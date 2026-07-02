from ultralytics import YOLO
import cv2

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")
print(model.model_name)

print("OpenCV-Version:", cv2.__version__)