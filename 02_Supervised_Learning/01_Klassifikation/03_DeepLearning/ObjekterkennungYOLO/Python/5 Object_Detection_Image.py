from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n_ncnn_model")

# Perform object detection on an image
results = model("Bilder/test3.jpg")

# Visualize the results
for result in results:
    result.show()
