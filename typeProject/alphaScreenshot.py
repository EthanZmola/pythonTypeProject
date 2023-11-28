import cv2 as cv
import numpy as np
import time
import pyautogui as pya



#time.sleep(4)
#screenshot = pya.screenshot('alphaPic/allAlphaUp.png')
cvScreenshot = cv.imread('alphaPic/allAlphaUP.png')

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w = 16
h =25

#cv.imshow("signle letter", temp)

pt = [228,576]
pt_copy = pt[0]
for i in range(26):
    pt[0] = pt_copy + int(18*i)
    #cv.rectangle(cvScreenshot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    temp = cvScreenshot[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
    cv.imwrite("alphaPic/" + letters[i] + "UP.png",temp)

# space = cvScreenshot[pt[1]+25:pt[1]+h+25, pt[0]:pt[0]+w,]
# cv.imshow("thing", space)

# k = cv.waitKey(0)
# cv.imwrite("alphaPic/space.png", space)
#cv.imshow("thing", cvScreenshot)

k = cv.waitKey(0)