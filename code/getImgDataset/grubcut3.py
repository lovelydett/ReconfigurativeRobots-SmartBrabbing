import cv2
import numpy as np

img = cv2.imread("imgSaved/training1/s15.jpg", 1) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (9, 9),0)

gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)

gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

blurred = cv2.GaussianBlur(gradient, (9, 9),0)
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

(cnts, _) = cv2.findContours(
	closed.copy(),
	#参数二：轮廓类型
    cv2.RETR_EXTERNAL,             #表示只检测外轮廓
    # cv2.RETR_CCOMP,                #建立两个等级的轮廓,上一层是边界
    # cv2.RETR_LIST,                 #检测的轮廓不建立等级关系
    # cv2.RETR_TREE,                 #建立一个等级树结构的轮廓
    # cv2.CHAIN_APPROX_NONE,         #存储所有的轮廓点，相邻的两个点的像素位置差不超过1
    #参数三：处理近似方法
    cv2.CHAIN_APPROX_SIMPLE,         #例如一个矩形轮廓只需4个点来保存轮廓信息
    # cv2.CHAIN_APPROX_TC89_L1,
    # cv2.CHAIN_APPROX_TC89_KCOS
    )

c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the image
draw_img = cv2.drawContours(img.copy(), [box], -1, (0, 0, 255), 3)
cv2.imwrite('imgProcessed/draw_img.jpg',draw_img)  

Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
hight = y2 - y1
width = x2 - x1
crop_img= img[y1:y1+hight, x1:x1+width]
cv2.imwrite('imgProcessed/crop_img.jpg',crop_img)  
