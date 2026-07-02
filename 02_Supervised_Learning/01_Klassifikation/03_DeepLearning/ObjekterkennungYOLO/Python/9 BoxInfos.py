from ultralytics import YOLO

# Load the exported NCNN model
ncnn_model = YOLO("yolo11n_ncnn_model")

# Run inference
results = ncnn_model("https://ultralytics.com/images/bus.jpg")

# Visualize the results
for box in results[0].boxes.data.tolist():
    print(box)