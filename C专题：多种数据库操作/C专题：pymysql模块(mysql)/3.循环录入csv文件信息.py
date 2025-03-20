# _*_ Anaconda3-Python3.8 _*_
import pymysql

conn = pymysql.connect(
    host='192.168.127.140',
    port=3306,
    user='root',
    password='数据库密码',
    charset='utf8',
    db='userdb'
)
cursor = conn.cursor()

with open('info.csv', encoding='utf-8') as f:
    txt = f.readlines()  # 列表，元素含换行符\n,替换时无需转义

# 二维列表
lst = [istr.replace("\n", "").split(',') for istr in txt]

for x in lst:
    cursor.execute("insert into hwork(id,name,password,gender,email,amount,ctime)values(%s,%s,%s,%s,%s,%s,%s)", x)
conn.commit()
print("导入成功！")
