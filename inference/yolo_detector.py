import cv2
import numpy as np

# Yolo Detector class
class YoloDetector:
    #weights :  weights file for Yolo
    #config  :  config file for Yolo
    #classes :  list of object names for detection
    def __init__(self, weights, config, classes):
        self.net = cv2.dnn.readNet(weights, config)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.colors = np.array([[255.,0.,0.]]) #red colour for bounding boxes
        self.classes = classes
        
    def detect(self,img):
        img = img.copy()
        height, width, channels = img.shape

        # Detect objects from img frame
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        # Get bounding boxes, prune for confidence, and NMS, and then return the result
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    # Object detected
                    print(class_id)
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]]) + ":" + str(round(confidences[0], 3))
                color = self.colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x - 30, y + 250), font, 3, color, 2)
                
        #width = int(img.shape[1])
        #height = int(img.shape[0])
        #dim = (width, height)
        #resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        return img
    
    






#def yolo_init(weights, config):



