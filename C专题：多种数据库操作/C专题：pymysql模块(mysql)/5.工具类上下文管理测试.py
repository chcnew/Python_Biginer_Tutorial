# _*_ encoding: utf-8 _*_

import pandas as pd
from db工具类.db_context import Connect

connect = Connect()  # 实例化
with connect:  # 对象本身
    data = connect.fetch_all("select sname,class_id from student")

# [{:,:,:},{:,:,:},{:,:,:}...] => DataFrame
df = pd.DataFrame(data)
print(df)
