import cv2
from ultralytics import YOLO

# Open the video streamq
cam = cv2.VideoCapture(0)

# Loop through the video frames
while cam.isOpened():
    # Read a frame from the video
    success, frame = cam.read()

    if success:
        # Display the annotated frame
        cv2.imshow("TEST", frame)

        # Break the loop if SPACE is pressed
        if cv2.waitKey(1) == ord(" "):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cam.release()
cv2.destroyAllWindows