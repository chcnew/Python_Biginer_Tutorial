# _*_ coding: utf-8 _*_

"""
pip3 install sqlacodegen
sqlacodegen --tables table1,table2 mysql+pymysql://root:passwd@127.0.0.1:3306/db_name --outfile db.py
"""

import os

mysql_info = "mysql+pymysql://root:数据库密码（@=%40）@192.168.127.140:3306/learn_sqlalchemy"
ex_command = f"sqlacodegen --tables alembic_version,user {mysql_info} --outfile tables.py"
print(ex_command)
os.system(ex_command)
