#coding: utf-8


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
import win32clipboard
import time
import os

def click_locxy(driver, x, y, left_click=True):

# dr:浏览器
# x:页面x坐标
# y:页面y坐标
# left_click:True为鼠标左键点击，否则为右键点击
	if left_click:
		ActionChains(driver).move_by_offset(x, y).click().perform()
	else:
		ActionChains(driver).move_by_offset(x, y).context_click().perform()

	ActionChains(driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

def Doubleclick_locxy(driver, x, y):
# dr:浏览器
# x:页面x坐标
# y:页面y坐标
# left_click:True为鼠标左键点击，否则为右键点击
	ActionChains(driver).move_by_offset(x, y).double_click().perform()
	ActionChains(driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前


def Fuzhi(m):
	# 打开粘贴板
	win32clipboard.OpenClipboard()
	# 清空粘贴板
	win32clipboard.EmptyClipboard()
	# 设置复制的内容
	win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, m) #复制变量a
	# 关闭粘贴板线程
	win32clipboard.CloseClipboard()

def Jsq(ds):
	while ds>=0:
		print('计时还剩：',ds,'秒！')
		time.sleep(1)
		ds=ds-1


if __name__ == '__main__':
	driver=webdriver.Chrome()
	#网优大数据平台-OLD
	driver.get('http://117.187.6.14:6054/mtex/login')
	driver.maximize_window()
	driver.refresh() #刷新
	time.sleep(2)
	print("正在登陆账号，请稍等~")
	click_locxy(driver, 916, 343-103, left_click=True) # 左键点击
	ActionChains(driver).send_keys('qnyd_longfuyu').perform()
	click_locxy(driver, 916, 397-103, left_click=True) # 左键点击
	ActionChains(driver).send_keys('QAZwsx#13579@').perform()
	print("-----你有80秒时间输入验证码、进入日常优化、设置flash！-----")
	Jsq(80)  #计时器

	print("相信你已经设置完成了！开始回单咯 ——>")
	df=pd.read_excel('info1.xlsx',sheet_name=0)
	for i in range(df.shape[0]):
		Hangdata=df.iloc[i].tolist() #用列表操作 其实Series也可以操作
		a=str(Hangdata[0]) #单号
		b=str(Hangdata[1]) #跟踪表
		c=str(Hangdata[2]) #分析评估报告
		Fuzhi(a)
		click_locxy(driver, 795, 211-103, left_click=True) # 左键点击
		# 直接复制进去
		ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
		click_locxy(driver, 1242, 213-103, left_click=True) # 左键点击
		time.sleep(10)
		# 进入工单
		Doubleclick_locxy(driver, 1242, 318-103) # 左键双击 双击未设置右键
		time.sleep(20)
		#下拉到底
		aa=1
		while aa<10:
			click_locxy(driver, 1342, 686-113, left_click=True) # 左键点击
			aa=aa+1
			time.sleep(1.5)



		click_locxy(driver, 589, 525-113, left_click=True) # 左键点击
		time.sleep(0.5)
		click_locxy(driver, 589, 591-113, left_click=True) # 左键点击
		time.sleep(2)

		click_locxy(driver, 589, 555-113, left_click=True) # 左键点击
		time.sleep(0.5)
		click_locxy(driver, 589, 599-113, left_click=True) # 左键点击
		time.sleep(1)

		click_locxy(driver, 1296, 588-113, left_click=True) # 左键点击
		time.sleep(1)

		click_locxy(driver, 464, 398-113, left_click=True) # 左键点击	添加
		time.sleep(1)

		pathheader=r"H:/1.Study/1.Python learning/Spyder Test Projects/2G派单回单设计-chc pc chrome/5.一键生成回单各种文件/EX-WD/" + b
		os.system('cctest.exe %s' %pathheader)
		time.sleep(1)



	print(" <—— 所有工单回复完成了！请检查一下哟~~")
	time.sleep(60)
	driver.quit()