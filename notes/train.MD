## Train YOLOv8 for Pothole Detection:

+ Create a data.yaml file to define the dataset paths and classes:

```yaml
    train: dataset/images/train
    val: dataset/images/val
    nc: 1  # Number of classes (only "pothole")
    names: ['pothole']
```

+ Train the model:

```python
from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # Use "yolov8s.pt" or "yolov8m.pt" for larger models

# Train the model
results = model.train(data="data.yaml", epochs=50, imgsz=640, batch=16)
```

+ Monitor training:

Training logs and metrics (e.g., mAP, loss) will be saved in the `runs/detect/train` folder.

Use `TensorBoard` to visualize training progress:

```bash
tensorboard --logdir runs/detect/train
```

+ Evaluate the Model:

Test the trained model on validation images:

```python
results = model.val()
```

Check metrics like mAP (mean Average Precision) to evaluate performance.

### Convert YOLOv8 to TensorFlow Lite :

+ Export the model to TensorFlow format:

```python
model.export(format="tflite")
```

This will save the model as `yolov8n_float32.tflite` in the `runs/detect/train/weights` folder.


+ (Optional) Quantize the model for smaller size and faster inference:

    + Use TensorFlow's post-training quantization tools:

    ```python
    import tensorflow as tf

    converter = tf.lite.TFLiteConverter.from_saved_model("path_to_exported_model")
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_quant_model = converter.convert()

    with open("yolov8n_quantized.tflite", "wb") as f:
        f.write(tflite_quant_model)
    ```

### Integrate the Model into the Mobile App :

+ Add the .tflite model to your mobile app's assets folder.

+ Use TensorFlow Lite Interpreter to run inference:

    + For Flutter: Use the tflite_flutter package.

    + For Android: Use TensorFlow Lite Android Support Library.

    + For iOS: Use TensorFlow Lite Swift API.

+ Implement the inference logic:

    + Preprocess the input image (resize to 640x640, normalize pixel values).

    + Run inference using the TensorFlow Lite Interpreter.

    + Parse the output to get bounding boxes and confidence scores.

+ Display results in the app:

    + Draw bounding boxes around detected potholes.

    + Show confidence scores and geolocation data.


### Example Code for TensorFlow Lite Inference (Python) :

```python
import tensorflow as tf
import cv2
import numpy as np

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="yolov8n_float32.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Preprocess the input image
image = cv2.imread("test_image.jpg")
image = cv2.resize(image, (640, 640))
image = image / 255.0  # Normalize
image = np.expand_dims(image, axis=0).astype(np.float32)

# Run inference
interpreter.set_tensor(input_details[0]['index'], image)
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])

# Parse output (e.g., bounding boxes, scores)
print(output)
```