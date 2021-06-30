# PotatoDetector using YoloV3

<img src="https://github.com/thehummingbird/PotatoDetectorYolo/blob/main/images/out.JPG">

**The project is divided into three parts**

* Creating a custom dataset for potato detection, 

* Training,

* Inference

**NOTE - If you wish to directly look at the results of this project, open out.mp4**

**1. Creating a custom dataset for potato detection:**

I used a training video and extracted frames at regular intervals. Then, I use the annotation tool "labelimg" for creating a training dataset for YOLO. 

The folder with all images + corresponding annotation txt files is stored as a zip in a google drive folder "potato_yolov3". This is used by colab for training the model

**2. Training**

I trained YoloV3 using darknet (an open source framework for neural networks supporting object detection. OpenCV supports darknet models and we later use it for inference)
Since I used colab for training YoloV3 using darknet, the folder "training" has a notebook which has to be run on Colab.

The notebook mounts google drive and uses the folder named "potato_yoloV3" where we store our zip dataset from step 1. 

The notebook unzips the dataset and trains YoloV3 model using darknet. I trained it for 2000 epochs (about 6 hours) and stored model weights in the same folder as the dataset (potato_yolov3 on google drive). We then download the weights for inference.

**3. Inference**
The folder "inference" consists of - *main.py, yolo_detector.py, yolov3_testing.cfg, yolov3_training.weights, test.mp4, and out folder*

* *main.py -* main file to run for inference
* *yolo_detector.py -* yolov3 model which takes weights and config and has an API detect which takes frames and returns results from yolo. The model is abstracted out from main.py so that it can ideally be used for other objects as well, depending on weights and name of the classes(object) passed
* *yolov3_testing.cfg -* config file for the model
* *yolov3_training.weights -* weights obtained from training on colab
* *test.mp4 -* Video used for inference
* *out folder -* location where the results for each frame is stored




