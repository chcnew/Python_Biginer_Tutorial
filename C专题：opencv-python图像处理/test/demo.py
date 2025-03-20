# _*_ encoding: utf-8 _*_
import cv2
import numpy as np


def read_demo(file: str):
    """读取图像
    32位深度的图会被自动转为24位，舍弃透明通道
    :param file: 文件路径
    :return:
    """
    image = cv2.imread(file)
    print(image.shape)  # H/W/C - 高/宽/通道数
    cv2.imshow("input", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def color_space(file: str):
    """读取图像
    32位深度的图会被自动转为24位，舍弃透明通道
    :param file: 文件路径
    :return:
    """
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # H通道范围：0~180
    cv2.imshow("gray", gray)
    cv2.imshow("hsv", hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def copy_picture(file: str):
    """读取图像
    32位深度的图会被自动转为24位，舍弃透明通道
    :param file: 文件路径
    :return:
    """
    image = cv2.imread(file)
    cv2.imshow("input", image)
    # roi = image[100:500, 100:800, :]
    # cv2.imshow("roi", roi)
    # blank = np.zeros_like(image)
    # blank = np.zeros(image.shape, dtype=np.uint8)
    # blank[100:500, 100:800, :] = roi
    blank = np.copy(image)  # 指向地址不同，类比字典copy/deepcopy
    cv2.imshow("blank", blank)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # read_demo("pic.jpg")
    # color_space("pic.jpg")
    copy_picture("../src/package/resource/pic.jpg")
