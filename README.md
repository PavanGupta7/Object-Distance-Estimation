
## Object Distance Estimation 
- This GitHub repository presents a deep learning-based approach for object distance estimation using the popular YOLO (You Only Look Once) algorithm. The YOLO model has been adapted and fine-tuned to not only detect objects in images but also estimate their distances from the camera without using any sensor. This enables a wide range of applications, such as autonomous navigation, surveillance, and robotics.

### Key Features:

- 1. YOLO Integration: The repository includes the modified YOLO model, which has been enhanced to incorporate distance estimation capabilities while preserving the real-time object detection performance.
- 2.    Dataset Preparation: A detailed guide on preparing the dataset is provided, along with sample data for training and testing the model. The dataset consists of labeled images with corresponding ground truth distance annotations.
- 3.    Model Training: Instructions and scripts to train the YOLO model on the custom dataset are available. Additionally, pre-trained weights are provided for users to kickstart their experiments.
    Inference and Evaluation: Users can perform inference on their own images or videos to estimate distances for detected objects. The repository also includes evaluation scripts to measure the model's performance metrics like accuracy and precision.
 - 4.    Demo Application: An interactive demo application is included, allowing users to visualize the object detection and distance estimation in real-time through a webcam or uploaded videos.
    Sample Results: Sample results from the model's performance on different datasets are showcased, along with comparisons to other distance estimation methods.

### Getting Started:
To get started with object distance estimation using YOLO, follow these steps:

- 1.    Clone the repository and install the required dependencies.
           cd yolov5

- 2.   Prepare your dataset by following the provided guidelines and annotations format.
           pip install -r requirements.txt
           cd distance_test
- 3.    Train the YOLO model using the prepared dataset or utilize the pre-trained weights.
- 4.   Run the inference scripts on your images or videos to estimate object distances.
          python detect_obj.py
- 5.   Check the demo application for real-time distance estimation.

Contributing:
Contributions to the repository are welcome. If you encounter any issues, feel free to open an issue or submit a pull request. Please adhere to the repository's code of conduct and contribution guidelines.


