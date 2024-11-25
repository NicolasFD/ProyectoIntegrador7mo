from ultralytics import YOLO
import cv2

# start webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/best.pt")

# object classes
classNames = ["Rin","Bisagra","Llanta","Tornillo","Tuerca","Motor"]

# discard 50 first frames to intialize de cam
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
        
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)   # objects detected write in a string
        
        """if(y1<200):
            if(x1<213):
        """""


        cls = int(box.cls[0])
        List+=(classNames[cls]+"\n")

    # write txt file with detected objects
txt=open("lista de objetos.txt",'w')
txt.writelines(List)
