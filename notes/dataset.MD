## Prepare the Dataset

+ Collect Images:

    + Gather images of potholes and non-potholes (e.g., roads without potholes, sidewalks, etc.).

    + Use publicly available datasets or collect your own images.

+ Annotate Images:

    + Use tools like LabelImg or Roboflow to annotate potholes in the images.

    + Save annotations in YOLO format (each image has a corresponding .txt file with bounding box coordinates).

+ Organize the Dataset:

    + Create a folder structure:

    ```bash
    dataset/
        images/
            train/
            val/
        labels/
            train/
            val/
    ```

Split the dataset into training (train) and validation (val) sets (e.g., 80% train, 20% val).

