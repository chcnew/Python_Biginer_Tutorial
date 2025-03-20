# _*_ coding: utf-8 _*_

"""
功能：
"""
from wxauto import WeChat

wx = WeChat()
while True:
    # 等待接受收到的最新消息
    # {"用户昵称A":「消息对象1,消息对象2,消息对象31，"用户昵称B":「消息对象1,消息对象2,消息对象31，}
    msg_dict = wx.GetNextNewMessage()
    for username, msg_list in msg_dict.items():
        print("昵称:", username)
        # [消息对象1，消息对象2，消息对象3]
        for msg in msg_list:
            print("\t消息", msg.type, msg.content)
