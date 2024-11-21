# program to capture single image from webcam in python 

# importing OpenCV and time library
import cv2
import time

# initialize the camera 
cam = cv2.VideoCapture(0)

# discard the first 150 frames
for _ in range(150):  
	result, image = cam.read() # the variable disappear once the "for" ends

# reading the input using the camera 
result, image = cam.read() 

# If image will detected without any error, 
# show result 
if result: 

	# showing result, it take frame name and image 
	# output 
	cv2.imshow("ImagenTomada.png", image) 

	# saving image in local storage 
	cv2.imwrite("ImagenTomada.png", image) 

	# If keyboard interrupt occurs, destroy image 
	# window 
	cv2.waitKey(0) 
	cv2.destroyWindow("ImagenTomada.png") 

# If captured image is corrupted, moving to else part 
else: 
	print("No se detectó imagen, intente nuevamente.") 
