import cv2
import face_recognition
from simple_facerec import SimpleFacerec
import sys
import os


sfr=SimpleFacerec()
sfr.load_encoding_images(r"C:\Users\grizi\OneDrive\Desktop\Projects\Personal Projects\Face Recognition\images")

cap=cv2.VideoCapture(0) #captures the video

while True:
    ret, frame=cap.read()

    face_locations,face_names=sfr.detect_known_faces(frame) #detects face in each frame
    for face_loc, name in zip(face_locations,face_names):
        y1,x1,y2,x2=face_loc[0],face_loc[1],face_loc[2],face_loc[3] 

        cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,100)) 
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,200),2) #the rectangle around the face

    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)

    if key==27: #Esc button
        break
cap.release()
cv2.destroyAllWindows()
