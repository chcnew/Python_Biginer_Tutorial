# coding:utf-8

# ip与端口号
# ip代表是哪一个地址的主机 端口号是代表通信的接口，即对应进程的端口

# 实现客户端与服务端通信
import socket

client = socket.socket()  # 创建对象
client.connect('localhost')  # 和目标连接
client = client.send('hello 你在干啥?'.encode())
client.close()
