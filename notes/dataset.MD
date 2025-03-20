## Prepare the Dataset

+ Collect Images:

    + Gather images of potholes and non-potholes (e.g., roads without potholes, sidewalks, etc.).

    + Use publicly available datasets or collect your own images. [[kaggle](https://www.kaggle.com/datasets/atulyakumar98/pothole-detection-dataset/code)]

+ Annotate Images:

    + Use tools like LabelImg or [Roboflow](https://roboflow.com/annotate) to annotate potholes in the images.

    + Save annotations in YOLO format (each image has a corresponding .txt file with bounding box coordinates).

+ Organize the Dataset:

    + Create a folder structure:

    ```bash

    pothole_dataset/
    images/
        train/          # Training images (70 pothole + 70 normal road)
        val/            # Validation images (20 pothole + 20 normal road)
        test/           # Test images (10 pothole + 10 normal road) - Optional
    labels/
        train/          # Training labels (annotations for pothole images)
        val/            # Validation labels (annotations for pothole images)
        test/           # Test labels (annotations for pothole images) - Optional

    ```

Split the dataset into training (train) and validation (val) sets (e.g., 80% train, 20% val).

