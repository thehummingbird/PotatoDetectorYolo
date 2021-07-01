# PotatoDetector using YoloV3

<img src="https://github.com/thehummingbird/PotatoDetectorYolo/blob/main/images_for_githubReadme/out.JPG">

**The project is divided into three parts**

* Creating a custom dataset for potato detection, 

* Training,

* Inference

**NOTE - If you wish to directly look at the results of this project, open out.mp4. The video, along with some large files used during inference are pushed to github using lfs. So please use the command line to clone this repo so that lfs can work properly and download large files.**

**1. Creating a custom dataset for potato detection:**

I used a training video and extracted frames at regular intervals. Then, I use the annotation tool "labelImg" for creating a training dataset for YOLO. 

To reproduce the results of this step, save the frames of training video (not provided in this repo). I used an interval of 5 frames and obtained 232 images. Then, use labelimg annotation tool to save YOLO type bounding box information as a txt file for each image.

**2. Training**

I trained YoloV3 using darknet (an open source framework for neural networks supporting object detection. OpenCV supports darknet models and we later use it for inference).
I used colab for training YoloV3 using darknet. For tasks which do not require a local structured python project, I use colab because the GPU allocated is more powerful than my local machine (I have a 4GB Nvidia GPU). The folder "training" in this repo has a notebook which has to be run on Colab.

To reproduce the results of this step, zip the dataset obtained from step one. Make a folder "potato_yolov3" in your google drive and place the zip file inside. Then, run colab notebook. The notebook unzips the dataset and trains YoloV3 model using darknet. It then trains the model(I ran it for 2000 epochs -about 6 hours) and stores weights in the same folder as the dataset (potato_yolov3 on google drive). Next, download the weights for inference.

**3. Inference**
The folder "inference" consists of - *main.py, yolo_detector.py, yolov3_testing.cfg, yolov3_training.weights, test.mp4, and out folder*

* *main.py -* main file to run for inference
* *yolo_detector.py -* yolov3 model which takes weights and config and has an API detect which takes frames and returns results from yolo. The model is abstracted out from main.py so that it can ideally be used for other objects as well, depending on weights and name of the classes(object) passed
* *yolov3_testing.cfg -* config file for the model
* *yolov3_training.weights -* weights obtained from training on colab
* *test.mp4 -* Video used for inference
* *out folder -* location where the results for each frame is stored

To reproduce the results of this step, run main.py in the folder "inference". The script will take each frame from test.mp4 and save the corresponding jpg result in the folder "out". You can use ffmpeg to create a video from all these images, if required (like the video out.mp4 in this repo)

**Comments on the results**

The model, as seen from out.mp4, successfully detects potatoes in the frames. While the detection results are decent, give the cluttered environment, further improvements can be done.

1. During dataset creation, I tried for compact bounding boxes for each frame. During inference, the box size is less than required if the object is too close. Trying out for slightly bigger bounding boxes for dataset creation can be a good experiment.

2. Training for a longer period will slightly improve the results.

3. Converting RGB frames to a more color sensitive color space such as LAB before training and inference could be another experiment. But, I am slightly sceptical of this idea because the model might start over-using color information, and extract less information from shape, texture, etc. This is unsuitable for cluttered enviromments with similar colors.






