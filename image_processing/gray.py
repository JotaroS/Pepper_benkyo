# -*- coding: utf-8 -*-
import cv2
import numpy as np


img_src = cv2.imread("img/lena.png");
height, width, channels = img_src.shape
img_dst = np.zeros((height,width,3), np.uint8)

for i in range(0,width):
    for j in range(0,height):
        val = ??????? #TRY HERE
        img_dst[i,j][0]=val #B
        img_dst[i,j][1]=val #G
        img_dst[i,j][2]=val #R

# PROPER WAY OF GRAYSCALE TRANSFORM
gray = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)


cv2.imshow("result_average", img_dst)
cv2.imshow("result_gray", gray)

cv2.waitKey(0)
