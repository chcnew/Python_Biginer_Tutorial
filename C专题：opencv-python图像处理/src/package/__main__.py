# _*_ encoding: utf-8 _*_

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

# 读取图像
img = cv2.imread("./resource/pic.jpg")
lower_hsv = np.array([74, 56, 42])
upper_hsv = np.array([212, 194, 180])
# 区域筛选
mask = cv2.inRange(img, lower_hsv, upper_hsv)
mask = cv2.GaussianBlur(mask, (1, 1), 0)
# 修改像素值
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if mask[i, j] == 255:
            img[i, j] = [74, 56, 42]

cv2.imwrite('.resource/res.jpg', img)
cv2.imshow("res.jpg", img)
print('Finished!')
cv2.waitKey(0)
cv2.destroyAllWindows()
