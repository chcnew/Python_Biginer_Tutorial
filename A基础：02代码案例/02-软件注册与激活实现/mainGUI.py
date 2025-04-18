# -*- codeing = utf-8 -*-

"""
主界面即注册成功后会进入的页面
"""

from tkinter import *


class mainGUI:
    # 初始化参数
    def __init__(self, title="主界面", version=None, auth="ccplayer"):
        # 生成一个窗口对象
        self.root = Tk()
        self.title = title
        self.version = version
        self.auth = auth
        # 设置窗口名称
        self.root.title("%s-%s by %s" % (self.title, self.version, self.auth))
        # 设置窗口图标  https://blog.csdn.net/nilvya/article/details/104822196/
        self.w = 350
        # self.root.iconbitmap('G:\\Python Project\\spiderM3U8\\img\\spider.ico')
        self.h = 200

        Label(self.root, text='您已注册！欢迎使用。', font=("Lucida Grande", 11)).grid(padx=30, pady=40)
        self.yxqL = Label(self.root, text="有效期截止到：", font=("Lucida Grande", 11))
        self.yxqL.grid(padx=50, pady=00)

        # 令此程序的窗口居中显示
        ws, hs = self.root.winfo_screenwidth(), self.root.winfo_screenheight()  # 获取本地电脑屏幕的大小
        self.root.geometry(
            '%dx%d+%d+%d' % (self.w, self.h, (ws / 2) - (self.w / 2), (hs / 2) - (self.h / 2)))  # 使得程序窗口居中显示
        self.root.resizable(None, None)  # 限制此程序窗口更改其大小
        # self.root.mainloop()


if __name__ == '__main__':
    maingui = mainGUI()
    maingui.yxqL['text'] = "有效期截止到：2022"
    maingui.root.mainloop()
