import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo11n_ncnn_model")

# Open the video streamq
cam = cv2.VideoCapture(0)

# Loop through the video frames
while cam.isOpened():
    # Read a frame from the video
    success, frame = cam.read()

    if success:
        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord(" "):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cam.release()
cv2.destroyAllWindows