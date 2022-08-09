import numpy as np
import cv2
from PIL import Image

def preprocess_image(img):
    gray_image= cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY) #converting color pic to grayscale
    resized=cv2.resize(gray_image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR) #arguments--> (input size, output size, fx=x axis rescale, fy= y axis rescale, interpolation= fill the empty pixels as a result of interpolation)
    processed_img=cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,11) #apply adaptive thresholding for resized image
    return processed_img