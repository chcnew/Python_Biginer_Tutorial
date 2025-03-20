import cv2
import numpy as np

path = "../src/package/resource/pic1.jpg"  # 记得不要有中文路径

img = cv2.imread(path)
height, width = img.shape[0:2]
# 开始操作
thresh = cv2.inRange(img, np.array([21, 20, 20]), np.array([69, 67, 70]))
scan = np.ones((3, 3), np.uint8)
cor = cv2.dilate(thresh, scan, iterations=1)
specular = cv2.inpaint(img, cor, 5, flags=cv2.INPAINT_TELEA)
# 操作结束，下面开始是输出图片的代码
cv2.namedWindow("image", 0)
# cv2.resizedWindow("image", int(width / 2), int(height / 2))
cv2.imshow("image", img)

cv2.namedWindow("modified", 0)
# cv2.resizeWindow("modified", int(width / 2), int(height / 2))
cv2.imshow("modified", specular)

cv2.waitKey(0)
cv2.destroyAllWindows()
