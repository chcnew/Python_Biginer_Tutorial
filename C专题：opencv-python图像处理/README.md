# C专题：opencv-python图像处理

高级用法必会涉及使用c++相关类库：

解决错误：**error: Microsoft Visual C++ 14.0 or greater is required.**

下载安装：Visual C++ Build Tools for Visual Studio 2015 with Update 3

下载地址：https://my.visualstudio.com/Downloads

安装参考：https://zhuanlan.zhihu.com/p/505983312



## 1. 安装opencv-python

```shell
pip install opencv-python
pip install opencv-contrib-python

解决找不到引用'imread‘in’__init__.py‘的问题：
    找到cv2包，复制cv2.pyd文件至site-packages目录下即可
```



## 2.色彩空间转换

```python
# _*_ encoding: utf-8 _*_

import cv2


def read_demo(file: str):
    """读取图像
    32位深度的图会被自动转为24位，舍弃透明通道
    :param file: 文件路径
    :return:
    """
    image = cv2.imread(file)
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


if __name__ == '__main__':
    # read_demo("pic.jpg")
    color_space("pic.jpg")

```



## 3.