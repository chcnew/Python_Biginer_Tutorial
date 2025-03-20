# _*_ coding: utf-8 _*_

"""
功能：第三方库jieba
"""

import jieba

text = "我喜欢使用jieba库进行中文分词。"
seg_list = jieba.cut(text, cut_all=False)

print(" ".join(seg_list))


# import jieba.posseg as pseg
#
# words = pseg.cut("我喜欢使用jieba库进行中文分词。")
# for word, flag in words:
#     print(f"{word} {flag}")
