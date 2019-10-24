import cv2
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
# img_dir = "data/test/coal/m9.jpg"
# img_dir = "data/test/gangue/s2.jpg"

datadir="data/train/gangue"
files = os.listdir(datadir)
for file in files:      
    img_dir=datadir+"/"+file
    save_dir = "graydata/gangue/"+file
    img = cv2.imread(img_dir)#(1400, 1437, 3)
    # 转为单通道
    img_gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#(1400, 1437)
    # img_gray2 = cv2.resize(img_gray1,(15,15),interpolation=cv2.INTER_CUBIC)
    # 进行filter,灰度值0为黑，255为白，在数据集中煤的灰度min 为13
    # print(img_gray1.min())
    # print(img_gray2)
    def getWhiteBackground(gray_img):
        for i in range(gray_img.shape[0]):
            for j in range(gray_img.shape[1]):
                if gray_img[i][j]>130:
                    gray_img[i][j]=0
                
        return gray_img
    img_gray1_process = getWhiteBackground(img_gray1)*2
    img_gray1_process = cv2.resize(img_gray1_process,(256,256),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(save_dir,img_gray1_process)
    print("saved in "+save_dir)
    # plt.figure("coal")
    # plt.imshow(img_gray1_process,cmap='gray')
    # plt.show()