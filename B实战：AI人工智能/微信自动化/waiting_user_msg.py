# _*_ coding: utf-8 _*_

"""
功能：微信监听指定用户消息回复
"""
import time

from wxauto import WeChat

from ollama_auto import get_answer

wx = WeChat()

wx.AddListenChat(who="林鹏")

while True:
    msg_dict = wx.GetListenMessage()
    for chat_win, msg_list in msg_dict.items():
        chat_user = chat_win.who
        for msg in msg_list:
            if msg.type != "friend":
                continue
            print(chat_user, msg.content)
            answer = get_answer(msg.content)
            chat_win.SendMsg(answer)  # 回复消息

    time.sleep(5)
