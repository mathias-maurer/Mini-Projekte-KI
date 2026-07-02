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
        # Look for bottles only, in YOLO class 39 stands for bottles
        results = model.predict(frame)
        for box in results[0].boxes.data.tolist():
            print(box)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Check all boxes ->
        for box in results[0].boxes.data.tolist():
            xmin, ymin, xmax, ymax, conf, id = box
            # in case that a person got detected: Display directional information
            if id == 41:
                if xmax < 250:
                    cv2.putText(annotated_frame, "<----left>", (400, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if xmin > 400:
                    cv2.putText(annotated_frame, "right--->", (40, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
                # Display the annotated frame
                cv2.imshow("YOLO", annotated_frame)


        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cam.release()
cv2.destroyAllWindows