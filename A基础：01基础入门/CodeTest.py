# _*_ coding: utf-8 _*_

"""
给定一个单词，你需要判断单词的大写使用是否正确。我们定义，在以下3种情况时，单词的大写用法是正确的：
1.全部字母都是大写，比如"USA"。
2.单词中所有字母都不是大写，比如"code"。
3.如果单词不只含有一个字母，只有首字母大写，比如 "Google"。否则，定义该单词没有正确使用大写字母。
请将示例直接代入求解！
示例 1:输入: "USA"输出: True
示例 2:输入: "FlaG"输出: False
"""


class TfWord:
    """TfWord"""

    def __init__(self):
        self.xx()

    @staticmethod
    def response(word: str = "") -> bool:
        """
        判断单词的大写使用是否正确

        :param word:
        :return: True or False
        """
        lst = list(word)
        num = len(lst)
        tf = True

        if num <= 2:
            return tf

        if lst[0].isupper():
            # 第0个字母为大写
            for i in range(2, num):
                if lst[i - 1].isupper() != lst[i].isupper():
                    tf = False
                    return tf
        else:
            for i in range(1, num):
                if lst[i - 1].isupper() != lst[i].isupper():
                    tf = False
                    return tf
        return tf


if __name__ == '__main__':
    res1 = TfWord.response("TTdsdEQE")
    res2 = TfWord.response("SDSDFDS")
    res3 = TfWord.response("dsassdd")
    print(res1)  # False
    print(res2)  # True
    print(res3)  # True
