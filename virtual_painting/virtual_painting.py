import cv2 as c
import numpy as np
import numpy as np
video=c.VideoCapture(0)
video.set(10,150)
color_point=np.array([[0,91,0,74,216,255],[25,16,12,111,45,34]])

def findcolors(image):
    for color in color_point:
        low = np.array(color[0:3])
        higt = np.array(color[3:6])
        mask = c.inRange(image, low, higt)
        # bounding(mask)
        c.imshow(str(color[0]), mask)
def bounding(im):
    contour=c.findContours(im,c.RETR_EXTERNAL,c.CHAIN_APPROX_NONE)
    for con in contour:
        area=c.contourArea(con)
        if(area>500):
            c.drawContours(image1,con,-1,(0,0,255),3)
            c.imshow('bounding',image1)
while True:
   s,image=video.read()
   image1=image.copy()
   colour= findcolors(image1)
   if(c.waitKey(1) & 0Xff==ord('z')):
         break

