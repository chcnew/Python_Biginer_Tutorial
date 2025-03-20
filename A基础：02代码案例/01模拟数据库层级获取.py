# -*- coding: utf-8 -*-

"""
    id   name  parent
0    1    sds     NaN
1    2    dgg     NaN
2    3  fghhj     NaN
3    4     jj     1.0
4    5   fgdf     2.0
5    6      h     3.0
6    7     fg     5.0
7    8    dfg     7.0
8    9      f     9.0
9   10     hj     1.0
10  11   kkhg     1.0
11  12   were     1.0
12  13    fgf     1.0

结果：
[4, 10, 11, 12, 13]

"""

import pandas as pd


def get_childs(idx, myids):
    res = df.loc[df["parent"] == idx]
    lst = res["id"].tolist()
    if lst:
        myids.extend(lst)
        for item in lst:
            get_childs(item, myids)


def retn_childs(idx):
    myids = []
    get_childs(idx, myids)
    return myids


if __name__ == '__main__':
    df = pd.read_excel("data.xlsx")
    print(df)
    print(retn_childs(idx=3))
