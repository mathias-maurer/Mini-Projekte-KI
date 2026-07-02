from ultralytics import YOLO
# Load the NCNN model
ncnn_model = YOLO("yolo11n_ncnn_model")

# Run inference
results = ncnn_model("https://ultralytics.com/images/bus.jpg")

# Visualize the results
for result in results:
    result.show()