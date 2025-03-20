from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Perform inference on a test image
results = model("test/poth2.jpg")

# Set confidence threshold
confidence_threshold = 0.5

# Check if any potholes are detected
pothole_detected = False

# Loop through the results
for result in results:
    # Check if there are any detections above the confidence threshold
    for box in result.boxes:
        if box.conf > confidence_threshold:  # Check confidence score
            pothole_detected = True
            break  # Exit the loop as soon as a pothole is detected
    if pothole_detected:
        break  # Exit the outer loop

# Print the result
if pothole_detected:
    print("Yes")  # At least one pothole is detected
else:
    print("No")   # No potholes are detected