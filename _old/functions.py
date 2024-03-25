import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def najdi_souradnice(filename):

    # Mouse callback function
    global click_list
    positions, click_list = [], []
    def callback(event, x, y, flags, param):
        if event == 1: click_list.append((x,y))
    cv.namedWindow('img')
    cv.setMouseCallback('img', callback)

    img = cv.imread(filename)

    # Mainloop - show the image and collect the data
    while True:
        cv.imshow('img', img)    
        # Wait, and allow the user to quit with the 'esc' key
        k = cv.waitKey(1)
        # If user presses 'esc' break 
        if k == 27: break        
    cv.destroyAllWindows()
    
    return click_list

def nacti_display(filename):
    click_list = najdi_souradnice(filename)

    img = cv.imread(filename)

    rows,cols,ch = img.shape
    #[[77,231],[813,0],[182,570],[940,323]]
    pts1 = np.float32(click_list)

    print(*click_list, sep = "\n")
    str1 = click_list[0][0] - click_list[2][0]
    str2 = click_list[0][1] - click_list[2][1]
    str3 = click_list[1][0] - click_list[0][0]
    str4 = click_list[0][1] - click_list[1][1]
    res1 = math.sqrt((str1**2)+(str2**2))
    res2 = math.sqrt((str3**2)+(str4**2))
    print (str(res1) + " " + str(res2))
    res1 = math.floor(res1)
    res2 = math.floor(res2)
    print (str(res1) + " " + str(res2))


    pts2 = np.float32([[0,0],[res2,0],[0,res1],[res2,res1]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(res2,res1))

    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')

    plt.show()

def read_jpg_to_red(filename):
    try:
        jpg = cv.imread(filename)  # načteni jpg
        print("Reading " + filename)

        picture = cv.cvtColor(jpg, cv.COLOR_BGR2RGB) # převod do RGB
        red_part = cv.cvtColor(jpg, cv.COLOR_BGR2RGB) 
        white = np.ones(3)*255  # bílá
        current = np.zeros(3)

        # 
        for i in range(0,red_part.shape[0]):
            for j in range(0,red_part.shape[1]):
                current = red_part[i][j]  # aktualni pozice
                np.seterr(divide='ignore', invalid='ignore')
                tmp = current[0]/np.sum(current)
                if tmp < 0.5:
                    red_part[i][j] = white  # přepsani na bilou

        # vykresleni
        plt.figure(1) 
        plt.subplot(1,2,1) 
        plt.title('picture')
        plt.imshow(picture)

        plt.subplot(1,2,2) 
        plt.title('Red part')
        plt.imshow(red_part)

        plt.show() 

    except Exception as error:
        print('ERROR: ' + error.__str__())

    return None

def remove_noise(filename):
    img = cv.imread(filename,0)
    # global thresholding
    ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    # Otsu's thresholding
    ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # plot all the images and their histograms
    images = [img, 0, th1,
            img, 0, th2,
            blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
            'Original Noisy Image','Histogram',"Otsu's Thresholding",
            'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

def erosion(filename):
    img = cv.imread(filename,0)
    kernel = np.ones((10,10),np.uint8)
    erosion = cv.erode(img,kernel,iterations = 1)

    erodile = cv.dilate(erosion,kernel,iterations = 1)

    plt.figure(1) 
    plt.subplot(1,3,1) 
    plt.title('original') 
    plt.imshow(img,  cmap='gray')

    plt.subplot(1,3,2) 
    plt.title('Erosion')
    plt.imshow(erosion,  cmap='gray')

    plt.subplot(1,3,3) 
    plt.title('Erosion than diletation')
    plt.imshow(erodile,  cmap='gray')

    plt.show() 

def dilatation(filename):
    img = cv.imread(filename,0)
    kernel = np.ones((5,5),np.uint8)
    dilate = cv.dilate(img,kernel,iterations = 1)

    dileero = cv.erode(dilate,kernel,iterations = 1)

    plt.figure(1) 
    plt.subplot(1,3,1) 
    plt.title('original') 
    plt.imshow(img,  cmap='gray')

    plt.subplot(1,3,2) 
    plt.title('Diletation') 
    plt.imshow(dilate,  cmap='gray')

    plt.subplot(1,3,3) 
    plt.title('Diletation than erosion')
    plt.imshow(dileero,  cmap='gray')

    plt.show() 


def edges(filename):
    img = cv.imread(filename,0)
    edges = cv.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

"""
if __name__ == '__main__':
    nacti_display('display.png')s
    #read_jpg_to_red('ball.jpg')
    #najdi_souradnice()

"""