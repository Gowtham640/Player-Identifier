import cv2
import face_recognition
from simple_facerec import SimpleFacerec
import sys
import os

img=cv2.imread("messi1.jpg") #takes in the image
rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #converts the image into rgb
img_encoding=face_recognition.face_encodings(rgb_img)[0] #o is the index so it takes the face alone from the picture

img2=cv2.imread("messi2.jpg")
img2_rgb=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img2_encoding=face_recognition.face_encodings(img2_rgb)[0]

result=face_recognition.compare_faces([img_encoding],img2_encoding) #compares the faces of the two pictures we encoded
print(result)

if img is None:
    print("Image not found or failed to load.")
else:
    cv2.imshow("messi", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()