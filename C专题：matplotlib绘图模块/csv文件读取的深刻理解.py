# -*- coding: utf-8 -*-

import pandas as pd
import csv

# header=0——表示csv文件的第一行默认为dataframe数据的行名称,
# index_col=0——表示使用第0列作为dataframe的行索引,
# squeeze=True——表示如果文件只包含一列，则返回一个序列。
file_dataframe = pd.read_csv('绘图Test.csv',header=0,index_col=0,squeeze=True)
 