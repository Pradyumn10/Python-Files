'''
* @Filename : data_collection_unit.py
* @author : Pradyumn Joshi
* @brief : It captures images when gets trigger from IR sensor. This script is written on Rasberry pi 2
* @version : 0.1.0
* 
*@copyright (C) 2021
'''
import os
import cv2
import imutils
from threading import Thread
import numpy as np
import RPi.GPIO as GPIO
import time

#threading class

class ThreadedCamera(object):
    def __init__(self, source = 0):

        self.capture = cv2.VideoCapture(source)

        #self.capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        #self.capture.set(3, 1280)
        #self.capture.set(4, 720)
        
        focus = 255 # min: 0, max: 255, increment: 5
        self.capture.set(28, focus)

        self.thread = Thread(target = self.update, args = ())
        self.thread.daemon = True
        self.thread.start()

        self.status = False
        self.frame  = None

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def grab_frame(self):
        if self.status:
            return self.frame
        return None

#GPIO setup
GPIO.setmode(GPIO.BOARD)
sensor_pin=31 #gpio pin 6
GPIO.setup(sensor_pin, GPIO.IN)

flag= False

set_num = int(input("Enter the number of set to be saved : "))
stream_link = 0
streamer = ThreadedCamera(stream_link)

if not os.path.isfile("./data/set-{}".format(set_num)):
    os.system("mkdir ./data/set-{}".format(set_num))

def high_signal(flag, i, set_num, frame):
    path = "./data/set-{}/image-{}.jpg".format(set_num,i)
    cv2.imwrite(path, frame)
    i+=1
    flag=True
    print(flag)
    return flag,i


#output
i = 0
while True:
    frame = streamer.grab_frame()
    if frame is not None:
        #frame = imutils.resize(frame, width=1080)
        cv2.imshow("Frame", frame)
        height, width, layers = frame.shape
        size = (width,height)
        print("Size of the frame : ", size)

    
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        if GPIO.wait_for_edge(sensor_pin, GPIO.RISING, bouncetime=200) is not None:
            path = "./data/set-{}/image-{}.jpg".format(set_num,i)
            cv2.imwrite(path, frame)
            i += 1




