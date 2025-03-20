import xlrd

excel = xlrd.open_workbook("info1.xlsx")
data = excel.sheets()[0]
hangshu = data.nrows 

for i in range(1,hangshu):
	Hangdata=data.row_values(i) #用列表操作 其实Series也可以操作
	a=str(Hangdata[0]) #单号
	b=str(Hangdata[1]) #小区级_filename
	c=str(Hangdata[2]) #分析-WD_filename

print(a)
print(b)
print(c)