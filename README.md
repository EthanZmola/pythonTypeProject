Using openCV to use image recognition to automatically do typing test on monkeytype.com. 

#Function takes a screen shot of computer screen with delay of .5 seconds. It also have input of the top left corner of the first line to be read.
#Then goes character by character on two lines of words, and looks for matches between a small part of the screenshot and library of letter images.
#Adds each character to string when recognized so the string can be types using pyautogui
#Each line has a max of 84 characters so loops that many times, but to avoid doing multiple spaces at the end of a blank line there is spaceBool.

Inefficient and was used to learn basic image recognition can computer vision.
Likely only works on specific monitors and does not do punctuation.
