chcp 65001
@echo off

echo "正在创建项目基本结构~"
mkdir ".\data"
mkdir ".\docs"
mkdir ".\src\package"
type nul>".\src\package\__init__.py"
type nul>".\src\package\__main__.py"
type nul>".\src\package\utils\util.py"
type nul>".\src\package\utils\__init__.py"
mkdir ".\test"
type nul>".\README.md"
type nul>".\setup.py"
echo "项目基本结构创建完成！"
pause