# **Anaconda之conda、pip命令管理+ Virtualenv使用**



## ● **配置python更新源**

### **pip国镜像源**

```
阿里云 https://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```

例如配置阿里云镜像源：

新建文本文件【"C:\Users\Administrator\pip\pip.ini"】

```
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=https://mirrors.aliyun.com
```

### **conda配置阿里云源**

新建文本文件【"C:\Users\Administrator\.condarc"】

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - http://mirrors.aliyun.com/anaconda/pkgs/main
  - http://mirrors.aliyun.com/anaconda/pkgs/r
  - http://mirrors.aliyun.com/anaconda/pkgs/msys2
custom_channels:
  conda-forge: http://mirrors.aliyun.com/anaconda/cloud
  msys2: http://mirrors.aliyun.com/anaconda/cloud
  bioconda: http://mirrors.aliyun.com/anaconda/cloud
  menpo: http://mirrors.aliyun.com/anaconda/cloud
  pytorch: http://mirrors.aliyun.com/anaconda/cloud
  simpleitk: http://mirrors.aliyun.com/anaconda/cloud
```

### **conda查看添加的镜像**

```
conda config --get channels
```



## ● **Python包安装命令**

### 1.**安装版本列表**

```shell
pip index versions pip
# 或者
# pip install pip==

PS C:\Users\Administrator> pip index versions pip
WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.
pip (22.0.4)
Available versions: 22.0.4, 22.0.3, 22.0.2, 22.0.1, 22.0, 21.3.1, 21.3, 21.2.4, 21.2.3, 21.2.2, 21.2.1, 21.2, 21.1.3, 21.1.2, 21.1.1, 21.1, 21.0.1, 21.0, 20.3.4, 20.3.3, 20.3.2, 20.3.1, 20.3, 20.2.4, 20.2.3, 20.2.2, 20.2.1, 20.2, 20.1.1, 20.1, 20.0.2, 20.0.1, 20.0, 19.3.1, 19.3, 19.2.3, 19.2.2, 19.2.1, 19.2, 19.1.1, 19.1, 19.0.3, 19.0.2, 19.0.1, 19.0, 18.1, 18.0, 10.0.1, 10.0.0, 9.0.3, 9.0.2, 9.0.1, 9.0.0, 8.1.2, 8.1.1, 8.1.0, 8.0.3, 8.0.2, 8.0.1, 8.0.0, 7.1.2, 7.1.1, 7.1.0, 7.0.3, 7.0.2, 7.0.1, 7.0.0, 6.1.1, 6.1.0, 6.0.8, 6.0.7, 6.0.6, 6.0.5, 6.0.4, 6.0.3, 6.0.2, 6.0.1, 6.0, 1.5.6, 1.5.5, 1.5.4, 1.5.3, 1.5.2, 1.5.1, 1.5, 1.4.1, 1.4, 1.3.1, 1.3, 1.2.1, 1.2, 1.1, 1.0.2, 1.0.1, 1.0, 0.8.3, 0.8.2, 0.8.1, 0.8, 0.7.2, 0.7.1, 0.7, 0.6.3, 0.6.2, 0.6.1, 0.6, 0.5.1, 0.5, 0.4, 0.3.1, 0.3, 0.2.1, 0.2
  INSTALLED: 21.2.2
  LATEST:    22.0.4
```

### 2.**安装指定版本**

```shell
pip install pip==22.0.4
```

### 3.**安装第三方包的方式**

#### 3.1 使用setup.py文件

复制到python的第三方包存放目录【... .../Lib/site-packages/第三方包文件夹】

cd 进入包的位置

```shell
python setup.py install
```

#### 3.2 使用.whl文件

针对.whl文件：先放到python目录下的.../Scripts/包名.whl

cmd 切换目录存放至路径

```shell
pip install 包名.whl
```

#### 3.4 conda升级第三方包

```shell
python -m pip install --upgrade pip
python -m pip --default-timeout=100 install --upgrade pip
python -m pip install pip==

# 设置超时断开时间
pip --default-timeout=100 install 包名
pip --default-timeout=100 install PyQt5==5.12.3
pip --default-timeout=100 install PyQtWebEngine==5.12.1


# 升级conda(升级Anaconda前需要先升级conda)：
conda update conda

# 升级anaconda：
conda update conda

# 升级anaconda：
conda update anaconda

# 更新所有包：
conda update --all

# 更新包：
conda update packagename

# 卸载包：
conda remove packagename

# 查询某个conda指令使用-h后缀，如conda update -h
```

#### 3.5 更改conda中的python版本

```
conda install -c anaconda python=3.8
```



## ● **pip管理命令**

### 一、查看和导出python已安装的包列表

```shell
# 全部列表
pip list
pip freeze

# 导出当前环境所有包及版本到txt  
pip freeze > requirements.txt

# 安装requirements.txt里面所有包  
pip install -r requirements.txt

# pip查看单个包信息
pip show numpy

# conda查看单个包信息
conda list numpy
```

### **二、列出可更新的包**

```shell
pip list --outdate
```

### **三、更新全部包**

#### 1. pip-review方式

```shell
pip install pip-review
pip-review --local --interactive
```

#### 2. python执行代码方式

```python
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
for dist in get_installed_distributions():
	call("pip install --upgrade " + dist.project_name, shell=True)
```

### 四、卸载包的方法

```shell
pip uninstall numpy

```

## ● **Anaconda-虚拟环境管理**

### 1.**初始化conda对powershell的使用**

```shell
conda init powershell

# 查看帮助
conda init -h
```

### 2.**列出虚拟环境信息**

```shell
conda info --envs
```

### 3.**创建python版本的虚拟环境（不指定和系统版本一致）**

```shell
conda create -n env_name
conda create -n env_name python=3.8
```

### 4.**激活虚拟环境：**

```shell
# Linux:  source activate your_env_name(虚拟环境名称)
source activate your_env_name

# Windows: activate your_env_name(虚拟环境名称)
activate your_env_name

# 比如：activate env_saas_py3.8
# 此时使用python --version可以检查当前python版本是否为想要的（即虚拟环境的python版本）。
```

### 5.**退出虚拟环境**

```shell
Linux:  source deactivate your_env_name(虚拟环境名称)
Windows:deactivate env_name，也可以使用`activate root`切回root环境
```

### 6.**删除虚拟环境**

```shell
conda remove -n your_env_name --all
```

### 7.**删除虚拟环境中的包：**

```shell
conda remove --name $your_env_name  $package_name
```

### 8.**conda常用命令**

```shell
# 查看安装了哪些包
conda list

# 安装包
conda install package_name(包名)

# 查看当前存在哪些虚拟环境
conda env list 或 conda info -e

# 检查更新当前conda
conda update conda
```

### 9.**powershell使用虚拟环境activate virtual_space问题解决**

**问题提示：**

```
PS C:\Users\Administrator> activate virtual_space

activate : 无法加载文件 F:\Anaconda\Scripts\activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.mi

crosoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。

所在位置 行:1 字符: 1

\+ activate virtual_space

\+ ~~~~~~~~

\+ CategoryInfo          : SecurityError: (:) []，PSSecurityException

\+ FullyQualifiedErrorId : UnauthorizedAccess
```

**解决方法：**

```
PowerShell管理员运行，更改策略：
PS C:\WINDOWS\system32> get-ExecutionPolicy
Restricted
PS C:\WINDOWS\system32> set-ExecutionPolicy RemoteSigned

执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170 中的
about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): y
PS C:\WINDOWS\system32> get-ExecutionPolicy
RemoteSigned
PS C:\WINDOWS\system32>
```



## ● **powershell conda初始化文件处理**

```
适用于：Windows PowerShell 2.0, Windows PowerShell 3.0
当我们打开一个PowerShell对话框，并在里面创建一些变量（variables）、函数（functions）时，这些变量、函数均只在当前会话中有效。一旦我们关闭这个对话框重新打开PowerShell时，这些变量都不存在了。如果我们想保留这些设置，我们就需要用到profile，翻译过来就是配置文件。在PowerShell启动的时候，会自动导入配置文件里面的设置。这有点像autorun.bat，如果有dos系统还有印象的朋友，应该知道这个。
配置文件存放于如下几个地方，不同的配置文件，作用域不同。

1、%windir%\system32\WindowsPowerShell\v1.0\profile.ps1
它作用于所有用户、所有的Shell。
2、%windir%\system32\WindowsPowerShell\v1.0\ Microsoft.PowerShell_profile.ps1
作用于所有用户，但只作用于Microsoft.PowerShell这个shell。这个我也没懂是什么意思，难道还有不是PowerShell的PowerShell shell？呃，有点像绕口令。
3、%UserProfile%\My Documents\WindowsPowerShell\profile.ps1
作用于当前用户的所有shell。
4、%UserProfile%\My Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
作用于当前用户的Microsoft.PowerShell这个shell。
以上的Windows的PowerShell profiles不是自动创建的。言下之意是，如果要用，我们就自己去创建。我们只要按照上面给出的文件路径和文件名，编写我们自己的内容进去即可。
有一个变量：$profile，它保存了当前Profile的路径。使用Test-Path $profile可以查看当前有没有这个文件。如果没有，可以使用new-item -path $profile -itemtype file -force命令来创建它。然后再使用notepad $profile来快捷的打开它来编辑。我们在里面输入function pro { notepad $profile }，呵呵明眼人都懂了，以后我们想要修改profile的时候，直接运行pro命令就可以了。

最后，想要PowerShell启动时能成功的载入配置文件，还需要在PowerShell的Execution Policy（执行策略）中设置允许它这样做。否则，尝试载入配置文件将会失败，PowerShell界面上也会显示错误信息。无法加载配置文件的错误提示如下：
```

 

```
代码如下:

C:\Users\Hong>powershell
Windows PowerShell
版权所有(C) 2012 Microsoft Corporation。保留所有权利。. : 无法加载文件 C:\Users\Hong\Documents\WindowsPowerShell\Microsoft.PowerShell
_profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 http://go.micros
oft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ . 'C:\Users\Hong\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
   + CategoryInfo          : SecurityError: (:) []，PSSecurityException
   + FullyQualifiedErrorId : UnauthorizedAccess
```

其实解决这个问题跟解决执行ps1文件的方法一样，因为这个Profile其实也是一个ps1格式的文件。所以使用Set-ExecutionPolicy RemoteSigned即可。



## ● **Virtualenv使用**

### 1.**安装virtualenv**

```shell
# 更新全部python包
pip install pip-review
echo y|pip-review --local --interactive

# 安装virtualenv
pip install virtualenv virtualenvwrapper-win
```

### 2.**设置virtualenv默认创建文件夹路径**

```shell
# 前提 : 系统中先安装好python
# 第一步：打开cmd命令终端，使用pip安装virtualenv虚拟环境和管理工具：
    pip install virtualenv
    pip install virtualenvwrapper-win
# 第二步：创建一个存放虚拟环境文件的文件夹（建议命名为.env或者.virtualenv）
# 第三步：配置环境变量
    # 在系统环境变量添加环境变量
    # 变量名：WORKON_HOME，
    # 变量值：第二步创建的文件夹路径
# 第四步：打开cmd命令终端，输入workon查看是否配置成功
```

**各个系统安装教程：**[**https://baijiahao.baidu.com/s?id=1697197036687801527&wfr=spider&for=pc**](https://baijiahao.baidu.com/s?id=1697197036687801527&wfr=spider&for=pc)

### 3.**创建虚拟环境及使用方法**

假设目前系统中含有python2.7和python3.9(不加参数用系统默认版本)

```shell
virtualenv 环境名称
virtualenv 环境名称 --python=python2.7
virtualenv 环境名称 --python=python3.9


操作系统 ： windowns10_x64

Python版本：3.6.8
virtualenv版本：16.7.7
virtualenvwrapper版本：1.2.5

方式一：直接使用virtualenv
1、安装
pip install virtualenv
2、创建虚拟环境
virtualenv -p d:/app/Python36/python.exe py36env
3、启动虚拟环境
py36env\Scripts\activate.bat
4、退出虚拟环境
deactivate
如果需要删除虚拟环境直接删除py36env即可。


方式二（推荐）：使用virtualenvwrapper-win
1、安装
pip install virtualenvwrapper-win
2、设置环境变量 WORKON_HOME 指定virtualenvwrapper虚拟环境默认路径
比如设置为 c:\venv，并创建venv目录。
如果不设置，会自动在当前用户目录创建相关文件夹。
3、创建虚拟环境
mkvirtualenv py36env -p d:/app/Python36/python.exe
mkvirtualenv --python=python3.5 venvname # venvname 虚拟环境名称 
或 mkvirtualenv -p python3.5 venvname # venvname 虚拟环境名称
4、查看所有虚拟环境和启动虚拟环境
lsvirtualenv
workon py36env
5、退出虚拟环境
deactivate
如果需要删除虚拟环境，执行如下命令：
rmvirtualenv py36env
```



powershell使用workon切换环境

```shell
powershell配置文件的路径和相对配置：
%windir%\system32\WindowsPowerShell\v1.0\profile.ps1

此配置文件适用于所有用户和所有 shell。
%windir%\system32\WindowsPowerShell\v1.0\ Microsoft.PowerShell_profile.ps1

此配置文件适用于所有用户，但仅适用于 Microsoft.PowerShell shell。
%UserProfile%\My Documents\WindowsPowerShell\profile.ps1

此配置文件仅适用于当前用户，但会影响所有 shell。

%UserProfile%\My Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

此配置文件仅适用于当前用户和 Microsoft.PowerShell shell。
```



添加如下函数 重启即可：

```python
function workon ($env) {
        & $env:WORKON_HOME\$env\Scripts\activate.ps1
}
```