from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # You can use "yolov8s.pt", "yolov8m.pt", etc.

# Train the model
results = model.train(
    data="data.yaml",  # Path to your data.yaml file
    epochs=100,             # Number of training epochs
    imgsz=640,              # Image size
    batch=16,               # Batch size (adjust based on your GPU memory)
    name="pothole_detection"  # Name of the training run
)