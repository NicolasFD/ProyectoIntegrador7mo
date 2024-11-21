from ultralytics import YOLO
import cv2

#start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

#discard 50 first frames to intialize de cam
for _ in range(50):  
	result, image = cap.read()
success, img = cap.read()
results = model(img, stream=True)
# create list
List=''
    #Pendiente por analizar!!!!!!!!!!!!
for r in results:
    boxes = r.boxes

    for box in boxes:
            #objects detected write in a string
        cls = int(box.cls[0])
        List+=(classNames[cls]+"\n")

    #write txt file with detected objects
txt=open("lista de objetos.txt",'w')
txt.writelines(List)
