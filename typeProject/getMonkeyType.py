import cv2 as cv
import numpy as np
import time
import pyautogui as pya

time.sleep(3)
pya.screenshot("alphaPic/testing.png")
letters = "abcdefghijklmnopqrstuvwxyz"
printVal =""
            #letterH = cv.imread("h.png",cv.IMREAD_GRAYSCALE)


img = cv.imread("alphaPic/testing.png",cv.IMREAD_GRAYSCALE)
#cv.imshow("Display", img)

w = 16
h =25
#cv.imshow("signle letter", temp)
pt = [228,576]
spaceBool =False
repeatSpace= False
h_shift=0
endLine = False

space_count=0
img2 = img.copy()
pt_copy = pt[0]
for z in range(3):
    space_count = 0
    pt = [228,576+(48*(z))]
    endlLine = False
    repeatSpace = False
    spaceBool = True

    for i in range(84):
    # i = 0
    # while (endLine == False):
        #17.4 earlier
        spaceBool =True
        pt[0] = pt_copy + int(18*i) -space_count

        for x in letters:
            letter = cv.imread("alphaPic/" +x+".png",cv.IMREAD_GRAYSCALE ) 
            res = cv.matchTemplate(img[pt[1]:pt[1] + h, pt[0]:pt[0] + w],letter,cv.TM_CCOEFF_NORMED)
            #cv.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
            if (res >=.9999):
                printVal+=x
                spaceBool = False
                repeatSpace = False
            else:
                letter = cv.imread("alphaPic/" + x+"UP.png",cv.IMREAD_GRAYSCALE ) 
                res = cv.matchTemplate(img[pt[1]:pt[1] + h, pt[0]:pt[0] + w],letter,cv.TM_CCOEFF_NORMED)
                #cv.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
                if (res >=.9999):
                    printVal+=x.upper()
                    spaceBool = False
                    repeatSpace = False
        #space check
        if (spaceBool):
            if (repeatSpace):
                endLine = True
            else:
                printVal+=" "
                space_count = space_count+3
                repeatSpace = True
                # print(space_count)
        # i+=1

# cv.imshow("single letter", img2)
# k = cv.waitKey(0)

#print(img.shape)
# print(printVal)
pya.write(printVal)
# cv.imshow("single letter", img2)
# k = cv.waitKey(0)

# if i == 1:
#     imgA = img[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
#     cv.imwrite('h.png',imgA)



