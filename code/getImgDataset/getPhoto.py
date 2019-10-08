import cv2

cap = cv2.VideoCapture(0)
cap.set(3,2560)
cap.set(4,1980)
i = 0
print("start capturing")
while(cap.isOpened()):  #isOpened()  检测摄像头是否处于打开状态
    ret,img = cap.read()  #把摄像头获取的图像信息保存之img变量
    if ret == True:       #如果摄像头读取图像成功
        #cv2.imshow('Image',img)
        i+=1
        cv2.imwrite("imgSaved/s"+str(i)+".jpg",img)
        cv2.imshow("img",img)
        print("count",i)
        if cv2.waitKey(2500)=='e':
            break