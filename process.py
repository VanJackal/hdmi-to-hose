"""
This file should contain the functionality to process a single image/frame and return it as an array of bytes (1 per line)
"""
import cv2

path = 'Images/TEST.png'

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
print(img)
print(img[0,0])

cv2.imshow("AAAH",img)

cv2.waitKey(0)