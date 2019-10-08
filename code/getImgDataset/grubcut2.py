import cv2  
import numpy as np

def execute(imgName):
    print(imgName)
    img = cv2.imread('imgSaved/test1/'+imgName, 1)  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
    
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    if len(contours)>1 :
        c = sorted(contours, key=cv2.contourArea, reverse=True)[1]
    else:
        return
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    # draw a bounding box arounded the detected barcode and display the image
    draw_img = cv2.drawContours(img.copy(), [box], 0, (0, 0, 255), 3)
    #cv2.imwrite('imgProcessed/'+imgName,draw_img)  

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1
    crop_img = img[y1:y1+hight, x1:x1+width].copy()
    cv2.imwrite('imgProcessed/test1/'+imgName,crop_img)  

nameFile = open('imgSaved/test1/imgNames.txt')
for line in nameFile.readlines():
    #execute(line)
    execute(line.strip('\n'))

# mask = np.zeros(crop_img.shape[:2], np.uint8)
  
# bgdModel = np.zeros((1, 65), np.float64)
# fgdModel = np.zeros((1, 65), np.float64)
  
# rect = (20, 20, 413, 591)
# cv2.grabCut(crop_img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
# mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
# img = crop_img * mask2[:, :, np.newaxis]
# img += 255 * (1 - cv2.cvtColor(mask2, cv2.COLOR_GRAY2BGR))
# # plt.imshow(img)
# # plt.show()
# img = np.array(img)
# mean = np.mean(img)
# img = img - mean
# img = img * 0.9 + mean * 0.9
# img /= 255
# cv2.imwrite('imgProcessed/final_img.jpg',img)  

