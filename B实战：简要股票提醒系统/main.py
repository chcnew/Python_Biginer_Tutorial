# coding: utf-8

#股票提醒系统
import tushare,pandas

datanow=tushare.get_realtime_quotes('000591')  #使用方法以股票代码获取对应股票的信息
#获取数据默认为字符串
name=datanow.loc[0][0] #股票名
price=datanow.loc[0][3] #当前价格
high=datanow.loc[0][4] #最高价
low=datanow.loc[0][5] #最低价
volumn=datanow.loc[0][8] #成交额
amount=datanow.loc[0][9] #成交量
openToday=datanow.loc[0][1] #当天开盘价
pre_close=datanow.loc[0][2] #昨日收盘价
the_time=datanow.loc[0][30] #时间

buy=4.5 #设置买点
sale=4.8 #设置卖点

if