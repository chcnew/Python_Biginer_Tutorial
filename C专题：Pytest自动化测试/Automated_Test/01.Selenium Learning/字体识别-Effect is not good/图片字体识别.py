#coding:utf-8

import pytesseract
from PIL import Image
from urllib.request import urlretrieve
import os

# os.makedirs('./image/', exist_ok=True)
# IMAGE_URL = "http://211.139.11.136:18070/mtnx/session/checkcode?"
# urlretrieve(IMAGE_URL, './image/checkcode.png') 

def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 128
            else:
                pixels[x, y] = 0
    return img


captcha = Image.open("checkcode.png")
captcha = convert_img(captcha, 150)
captcha.save("threshold.jpg")

captcha = Image.open("threshold.jpg")
result = pytesseract.image_to_string(captcha)
print(result)  