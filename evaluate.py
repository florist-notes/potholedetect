from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Evaluate the model on the validation set
metrics = model.val()
print(f"mAP50-95: {metrics.box.map}")  # mAP score