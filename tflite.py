from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Export the model to TensorFlow Lite format
model.export(format="tflite")
