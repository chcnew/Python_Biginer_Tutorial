# coding: utf-8

import time,sys
import pyautogui,pyperclip
import pandas as pd
import numpy as np
import cv2

#保护措施，避免失控
pyautogui.FAILSAFE = True
#为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.2

#请先设置接单时限坐标 回单时限坐标！！！！！！！！！！
#请先设置接单时限坐标 回单时限坐标！！！！！！！！！！
#请先设置接单时限坐标 回单时限坐标！！！！！！！！！！
jdx=414  
jdy=538

hdx=1100
hdy=562


#最大化时 进行最小化IDLE
pyautogui.click(x=1264, y=17, clicks=1, interval=0.0, button='left', duration=0.5, tween=pyautogui.linear)
#pyautogui.click(x=1264, y=17, clicks=1, interval=0.0, button='left', duration=0.5, tween=pyautogui.linear)


df=pd.read_excel('info0.xlsx',sheet_name=0)
time.sleep(1)

def Pause_key(keypress):
	key = 0
	print('准备开始，按空格键暂停与继续...\n')
	img = np.zeros((100, 200, 3), np.uint8)
	img.fill(255)
	cv2.putText(img, '!!!!!!', (10, 50),cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
	cv2.imshow('Attention!', img)

	for i in range(df.shape[0]):
		input_kb = cv2.waitKey(1) & 0xFF
		if input_kb == ord(' '):
			print('Paused')
			cv2.waitKey(0)
			print('Continued')
		time.sleep(1)

		Hangdate=df.iloc[i].tolist() #用列表操作 其实Series也可以操作
		a=Hangdate[0]  #小区名称
		b=Hangdate[1]  #主题
		c=Hangdate[2]  #描述
		
		time.sleep(1)
		
		#右键创建工单
		pyautogui.click(x=1318, y=201, clicks=1, interval=0.0, button='left', duration=0.5, tween=pyautogui.linear)
		time.sleep(12)


		#右击右方下拉按钮(上)
		pyautogui.click(x=1343, y=285, clicks=3, interval=0.2, button='left', duration=0.8, tween=pyautogui.linear)
		time.sleep(0.2)
		#选类型
		pyautogui.mouseDown(548,375,button='left')
		pyautogui.mouseUp(548,375,button='left',duration=0.5)
		#pyautogui.click(x=548, y=375, clicks=1, interval=0.0, button='left', duration=0.8, tween=pyautogui.linear)
		pyautogui.click(548,507,duration=0.5)
		time.sleep(2)

		#输入主题
		pyperclip.copy(b)
		pyautogui.click(x=870, y=375,clicks=2, interval=0.5, button='left', duration=0.8, tween=pyautogui.linear)
		time.sleep(0.2)
		pyautogui.hotkey('ctrl','a') 
		pyautogui.hotkey('ctrl','v') 
		time.sleep(0.2)

		#输入描述
		pyperclip.copy(c) 
		pyautogui.click(x=336, y=432, clicks=2, interval=0.2, button='left', duration=0.8, tween=pyautogui.linear)
		time.sleep(0.2)
		pyautogui.hotkey('ctrl','a') 
		pyautogui.hotkey('ctrl','v') 
		time.sleep(0.2)

		pyautogui.click(x=1357, y=197, clicks=1, interval=0.0, button='left', duration=0.8, tween=pyautogui.linear)
	cv2.destroyAllWindows()
	print("所有单子派单已完成！")
	sys.exit(0)

if __name__ == '__main__':
	Pause_key(keypress=' ')