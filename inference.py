from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO("best.pt")

# Perform inference on a test image
results = model("test/ima.jpg")

# Display the results
for result in results:
    result.show()  # Show the image with bounding boxes
    result.save("result.jpg")  # Save the result