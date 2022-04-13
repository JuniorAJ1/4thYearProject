#this code will allow the user to set up there face intom the 'profile' file where there
# face will be detected by the facial recognitios software

import cv2
import os
from picamera import PiCamera
from picamera.array import PiRGBArray


name = input("Enter your Name ")

cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))
    
img_counter = 0

while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "profiles/"+ "{}.jpg".format(name)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
            if img_counter >= 1:
                
                response = input("Are you happy with this photo Y/N: ")
                if response == 'Y':
                    print("your pic has been added to the database")
                    break
                elif response == 'N':
                    os.remove(img_name)
                                  
        break;
            
    if k%256 == 27: 
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()

