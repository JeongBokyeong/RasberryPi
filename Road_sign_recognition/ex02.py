import keras
import numpy as np
import time
classifier = keras.models.load_model('C:\code\IoTProject\djlkfdsjl\RasberryPi\Road_sign_recognition\SignRec-CNN.h5')
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

def ImgCapture():
    ret, img = cap.read()
    cv2.imshow('img', img)
    #captured img
    # imgwrite = cv2.resize(img, (1280, 720))
    cv2.imwrite('C:\RasberryPi\Demo01111\signDetected.jpg', img)
        

from PIL import Image


def prepare(path):
    img = Image.open(path)
    img_reshaped = img.resize((32, 32))
    img_rotated = img_reshaped.rotate(180)
    img_rotated.save(path)
    img = Image.open(path)
    img = np.expand_dims(img, axis = 0)
    img = img/255
    return img


def predictt(path):
	prediction = classifier.predict([prepare(path)])
	L1=[]
	prediction
	n=(np.argmax(prediction))
	X=prediction[0][n]
	#print(np.argmax(prediction))
	L1.append(n)
	L1.append(X)
	return L1

def drive():
    print("a")
    L1=[]
    ImgCapture()
    prepare('C:\RasberryPi\Demo01111\signDetected.jpg')
    L1=predictt('C:\RasberryPi\Demo01111\signDetected.jpg')
    if(L1[0]==4):
        print("forward")
    elif(L1[0]==3):
        print("RIGHT")
    elif(L1[0]==2):
        print("LEFT")
    else :
        print("stop")

import curses

screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        drive()
        ret, frame = cap.read()
        #show the frame
        cv2.imshow("Frame", frame)
        #resize the frame
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print("up")
            drive()

        elif char == curses.KEY_DOWN:
            print("down")
        elif char == curses.KEY_LEFT:
            print("left")
        elif char == curses.KEY_RIGHT:
            print("right")


finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()