# TechVidvan Face detection

import cv2
import numpy as np
import face_recognition
import os

# Define the path for training images

path = '/Users/suditigupta/Documents/Replicate1/faces'

images = []
classNames = []

# Reading the training images and classes and storing into the corresponsing lists
for img in os.listdir(path):
    print("Img :", img)  # Make sure image_path is defined
    #print(" path:", path)  # Make sure image_path is defined
    full_image_path = f'{path}/{img}'  
    print("Checking image path:", full_image_path)  
    print("Full Image Path:", full_image_path)
    image = cv2.imread(path)
    print("Image with changes:", image)
    images.append(image)
    print("Images :", images)
    classNames.append(os.path.splitext(img)[0])

print("Classname:", classNames)
#print("BLOCK ONE Working")
#print("Image :", images)  # Make sure image_path is defined
#print(" path:", encodeList)  # Make sure image_path is defined
# Image resize scale

'''Change this scale according to your need between 0 and 1.
    A lower number will give better performance but 
    it will not be able to detect faces if the face 
    is small in the image, and a greater number can detect 
    small faces in the image but the performance will be slow'''

scale = 0.25
box_multiplier = 1/scale


# Function for Find the encoded data of the input image
def findEncodings(images):
    encodeList = []
    for img in images:
        print("Image in block 2 :", images) 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        print(encode)
        encodeList.append(encode)
    return encodeList

# Find encodings of training images
print('Loop Complete')
knownEncodes = findEncodings(images)
print('Encoding Complete')
 
# Define a videocapture object
cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()  # Reading Each frame
    
    # Resize the frame
    Current_image = cv2.resize(img,(0,0),None,scale,scale)
    Current_image = cv2.cvtColor(Current_image, cv2.COLOR_BGR2RGB)

    # Find the face location and encodings for the current frame
    # 'cnn' runs on gpu and it is more accurate. change it to 'hog' is you want to run on cpu.
    face_locations = face_recognition.face_locations(Current_image, model='cnn')  
    face_encodes = face_recognition.face_encodings(Current_image,face_locations)

    # print(face_locations)
    
    # Find the matches for each detection
    
    for encodeFace,faceLocation in zip(face_encodes,face_locations):
        matches = face_recognition.compare_faces(knownEncodes,encodeFace, tolerance=0.6)
        # print(matches)
        faceDis = face_recognition.face_distance(knownEncodes,encodeFace)
        matchIndex = np.argmin(faceDis)

        # print(matchIndex)
        # If match found then get the class name for the corresponding match

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

        else:
            name = 'Unknown'

        y1,x2,y2,x1 = faceLocation
        y1, x2, y2, x1 = int(y1*box_multiplier),int(x2*box_multiplier),int(y2*box_multiplier),int(x1*box_multiplier)

        # Draw rectangle around detected face

        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(img,(x1,y2-20),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)


    # show the output
    cv2.imshow('Webcam',img)

    if cv2.waitKey(1) == ord('q'):
        break

# release the camera object

cap.release()
cv2.destroyAllWindows()