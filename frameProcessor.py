"""
frameProcessor.py --- contains logic for converting a frame into a boolean array
"""
import cv2
import numpy as np

def processFrame(path):
    frame = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    x = len(frame)
    y = len(frame[0])
    frameData = np.zeros((x,y)).astype(np.bool8)

    for i in range(x):
        for j in range(y):
            frameData[i,j] = int(frame[i,j] > 0)
    
    return frameData
