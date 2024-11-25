from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/best.pt")

# object classes
classNames = ["Rin","Bisagra","Llanta","Tornillo","Tuerca","Motor"]


for _ in range(50):  
	result, image = cap.read()
success, img = cap.read()
results = model(img, stream=True)

    # coordinates
for r in results:
    boxes = r.boxes
    
    for box in boxes:
            # bounding box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
        print(x1,y1,y2,x2)
            # put box in cam
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 3)

            # confidence
        confidence = math.ceil((box.conf[0]*100))/100
        print("Confidence --->",confidence)
        
            # class name
        cls = int(box.cls[0])
        print("Class name -->", classNames[cls])

            # object details
        org = [x1, y1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0, 0, 0)
        thickness = 2

        cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

cv2.imshow('Webcam', img)
cv2.imwrite('ImagenDetectadas.jpg',img)

print(classNames[cls])
cap.release()
cv2.destroyAllWindows()