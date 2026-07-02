from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")

# Run inference
results = model("https://ultralytics.com/images/bus.jpg")


# Visualize the results
for result in results:
    result.show()