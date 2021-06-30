import cv2
from yolo_detector import YoloDetector

def main():
    #Initialize yolo detector object for potato detection
    classes = ["Potato"]
    potato_detector = YoloDetector("yolov3_training.weights", "yolov3_testing.cfg", classes)
    
    #Open video for inference 
    cap = cv2.VideoCapture('test.mp4')
    #count of images stored
    img_count = 0
    while (cap.isOpened()):
        # Loading image
        ret, img = cap.read()
        if ret:
            result = potato_detector.detect(img)
            #show results from Yolo
            cv2.imshow("Image", result)
            cv2.imwrite("out/Image"+str(img_count)+".jpg",result)
            img_count = img_count + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cv2.destroyAllWindows()
    print("Inference stopped at the end of the video")

   
if __name__ == '__main__':
    main()