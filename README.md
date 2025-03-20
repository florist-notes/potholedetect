# Pothole Detection :

This project aims to develop a mobile application that uses AI to detect potholes in real-time. Users can capture images of roads, and the app will automatically determine whether the image contains a pothole. The app leverages YOLOv8, a state-of-the-art object detection model, trained specifically for pothole detection. The model is fine-tuned on a custom dataset of pothole and non-pothole images, ensuring high accuracy. Once trained, the model is converted to TensorFlow Lite format for efficient on-device inference, enabling fast and offline pothole detection. The app also captures geolocation data, allowing users to report potholes to authorities or maintenance teams.


## Define the App Requirements:
+ `Frontend` (Mobile App):

    + Capture images using the device camera.

    + Capture geolocation (latitude and longitude) using GPS.

    + Upload images and metadata (geolocation) to a server.

    + Display results (e.g., "Pothole detected" or "No pothole detected").

+ `Backend` (Server):

    + Receive and store images and metadata.

+ `AI Model`:

    + Train a machine learning model to classify images as "pothole" or "not pothole."

    + Deploy the model for inference (on the device).


## Develop the Mobile App (Flutter)

### Core Features :

+ `Camera Integration`:

    + Use libraries like camera (Flutter) or react-native-camera to capture images.

    + Allow users to take photos or select images from the gallery.

+ `Geolocation`:

    + Use libraries like geolocator (Flutter) or react-native-geolocation-service to fetch the device's GPS coordinates.

+ `Image Upload`:

    + Use HTTP libraries like http (Flutter) or axios (React Native) to send images and metadata to the server.

+ `User Interface`:

    + Design a simple UI for capturing images, displaying results, and showing a map with pothole locations.

## [ [DATASET](./notes/dataset.MD) ]