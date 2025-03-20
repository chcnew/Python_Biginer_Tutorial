# _*_ coding: utf-8 _*_

"""
功能：
"""
import redis

# 创建redis连接池
pool = redis.ConnectionPool(
    host='192.168.127.150',
    port=6379,
    password='cc123456',
    encoding='utf-8',
    max_connections=1000)
# 去连接池中获取一个连接
conn = redis.Redis(connection_pool=pool)
# 设置键值：name="诸葛亮" 且超时时间为10秒（值写入到redis时会自动转字符串）
conn.set('name', "诸葛亮", ex=10)
# 根据键获取值：如果存在获取值（获取到的是字节类型）；不存在则返回None
value = conn.get('name').decode("utf-8")
print(value)
