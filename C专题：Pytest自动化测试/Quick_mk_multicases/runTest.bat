@echo off
chcp 65001


set pyfile="F:\My_Study\1.Python_learning\2.Python_Biginer_Tutorial_51zxw\C专题：pytest知识笔记\quick_mk_multicases\taska.py"
python -m pytest %pyfile%  -v -l --color=no --log-cli-level=DEBUG --junit-xml=result.xml --html=report.html --self-contained-html