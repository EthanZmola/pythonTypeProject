import cv2 as cv
import numpy as np
import time
import pyautogui as pya



img = cv.imread("multiple.png",cv.IMREAD_GRAYSCALE)
# cv.IMREAD_GRAYSCALE
#alphabet.jpg   multiple.png
img2 = cv.imread("multiple.png")

screenshot = pya.screenshot('toDisk.png')
cvScreenshot = cv.imread('todisk.png')
cv.imshow("Testing screenshot", cvScreenshot)


template = cv.imread("alphabet.jpg",cv.IMREAD_GRAYSCALE) #IS NOW CROP_IMG

# px = img[10,10]
#print(img.shape)
#print(template.shape)
x= 115
y= 160
h = 85
w =60
crop_img = template[y:y+h, x:x+w]
# for i in range( 550):
#     img[i, 10] = [255,255,255] 
# cv.imshow("Display window", crop_img)
# cv.imshow("Display window 2", img)

thresh_hold =.8



res = cv.matchTemplate(img,crop_img,cv.TM_CCOEFF_NORMED)
threshold =.8
loc = np.where(res>=threshold)


# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] +w, top_left[1]+h)
for pt in zip(*loc[::-1]):
    cv.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

#cv.rectangle(img2,top_left,bottom_right, 255, 2)
#cv.imshow("Display window", crop_img)
cv.imshow("Display window 2", img2)

k = cv.waitKey(0) # Wait for a keystroke in the window

#pya.write('Hello there')

#hotkey('ctrl', 'esc')


#cv.imwrite('res.png',img_rgb)



