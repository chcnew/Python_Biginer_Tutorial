# encoding = utf-8

from PIL import Image, ImageDraw, ImageFont, ImageMode

# 设置字体打印大小
font_size = 15
# 设置添加的名字
text = "爱你哟"
img_path = "pic.jpg"

# 导入指定的图片
img_raw = Image.open(img_path)
# 使用load函数获取到每一个像素值
img_array = img_raw.load()

# 新建画布并设置好相关参数
img_new = Image.new("RGB", img_raw.size, (255, 255, 255))  # 参数： image = Image.new(mode,size,color)
# 添加字体
draw = ImageDraw.Draw(img_new)
# 字体，可以使用windows系统自带的(可打开c盘的fonts文件夹查看你所喜欢的文字)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)


# 文本循环生成
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]


ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)
# 把生成的图片保存下来
img_new.convert('RGB').save("picture.png")
