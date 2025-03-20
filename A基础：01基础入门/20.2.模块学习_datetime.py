import datetime

# 输出当前日期和时间 2022-03-04 16:52:14.028834
print(datetime.datetime.today())
print(datetime.datetime.today().strftime("%Y-%m-%d"))
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d"))
print(datetime.datetime.utcnow())
print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

# 时间计算
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# 获取到日期
date_aft10 = datetime.date.today() + datetime.timedelta(days=10)
print(date_aft10)

date_set = datetime.date(2022, 1, 1)  # 设置时间
date_set_week1 = date_set + datetime.timedelta(weeks=1)  # 计算一周日期，一周按7天计算
print(date_set_week1)

# 时间日期格式化方法：strftime()
# 时间日期解析类方法：datetime.strptime(date_string, format)
time_set = datetime.datetime(2022, 3, 4, 17, 11, 22, tzinfo=datetime.timezone.utc)
print(time_set)
print(time_set.strftime("%Y-%m-%d %H-%M-%S %Z"))
print(time_set.strftime("%Y-%m-%d %H-%M-%S %z"))

# 字符串转为时间
mytime = datetime.datetime.strptime("2022-10-14", "%Y-%m-%d")
print(mytime, type(mytime))
