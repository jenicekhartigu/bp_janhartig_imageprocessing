
import math
import cv2 as cv
from cv2 import imshow
from cv2 import split
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageQt

def makeHist(image):
    
    image_gray = cv.cvtColor(np.float32(image), cv.COLOR_RGB2GRAY)

    # převod na histogram - orig
    hist, bin_edges = np.histogram(image_gray.flatten(),256,(0,255))
    plt.title('Histogram')
    plt.bar(bin_edges[:-1], hist, width = 1)
    plt.xlim(min(bin_edges), max(bin_edges))
    plt.show()
    
    # redraw the canvas
    fig = plt.gcf()
    fig.canvas.draw()
    
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # opencv format
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    
    plt.close()
    res = Image.fromarray(img)
    return res
    
def erosion(img):
    
    kernel = np.ones((3,3),np.uint8)
    erosion = cv.erode(np.asarray(img),kernel,iterations = 1)
    res = Image.fromarray(erosion)
    return res

def dilatation(img):
    kernel = np.ones((3,3),np.uint8)
    dilate = cv.dilate(np.asarray(img),kernel,iterations = 1)
    res = Image.fromarray(dilate)
    return res
    
def tophat(img):
    
    kernel = np.ones((3,3),np.uint8)
    tophat = cv.morphologyEx(np.asarray(img), cv.MORPH_TOPHAT, kernel)
    res = Image.fromarray(tophat)
    return res

def blackhat(img):
    
    kernel = np.ones((3,3),np.uint8)
    blackhat = cv.morphologyEx(np.asarray(img), cv.MORPH_BLACKHAT, kernel)
    res = Image.fromarray(blackhat)
    return res


def changeColorSpace(img, choose):
    retImage = img
    if choose == 1:
        retImage = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2BGRA)
        
    elif choose == 2:
        retImage = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2GRAY)
    elif choose == 3:
        retImage = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2HSV)
    elif choose == 4:
        retImage = cv.cvtColor(np.asarray(img), cv.COLOR_BGR2YCrCb)
    print(retImage.shape)
    res = Image.fromarray(retImage)
    return res

# Color space changing
def rgb2DColorSpace(img, choose):
    img = (np.asarray(img))
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    if choose == -2:
        retImage = b
    elif choose == -3:
        retImage = g
    elif choose == -4:
        retImage = r
    imshow("",retImage)
    print(retImage.shape)
    res = Image.fromarray(retImage)
    
    return res

def hsv2DColorSpace(img, choose):
    img = (np.asarray(img))
    h, s, v = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    if choose == -2: 
        retImage = h
    elif choose ==  -3:
        retImage = s
    elif choose == -4:
        retImage = v
    # imshow("",retImage)
    print(retImage.shape)
    res = Image.fromarray(retImage)
    
    return res

def ycbcr2DColorSpace(img, choose):
    img = (np.asarray(img))
    y, cb, cr = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    if choose == -2: 
        retImage = y
    elif choose ==  -3:
        retImage = cb
    elif choose == -4:
        retImage = cr
    # imshow("",retImage)
    print(retImage.shape)
    res = Image.fromarray(retImage)
    
    return res

def all2DColorSpace(img, choose):
    img = (np.asarray(img))
    st, nd, rd = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    if choose == 1: 
        retImage = st
    elif choose == 2:
        retImage = nd
    elif choose == 3:
        retImage = rd
    # imshow("",retImage)
    
    print("min ",np.amin(retImage))
    print("max ",np.amax(retImage))
    
    res = Image.fromarray(retImage)
    return res

def edgeNoiseFunctions(img, choose):
    img = (np.asarray(img))
    retImage = img
    
    if choose == 1:
        retImage = cv.Canny(img,np.amin(img)*2,round(np.amax(img)/2))
        
    elif choose == 2:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        retImage = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    elif choose == 3:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        retImage = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
        
    res = Image.fromarray(retImage)
    return res

def morphOperation(img, choose):
    # img = np.asarray(img)
    if choose == -2:
        retImage = erosion(img)
    elif choose ==  -3:
        retImage = dilatation(img)
    elif choose == -4:
        retImage = tophat(img)
    elif choose == -5:
        retImage = blackhat(img)
    # imshow("",retImage)
    return retImage
    
        
if __name__ == '__main__':
    print("")

