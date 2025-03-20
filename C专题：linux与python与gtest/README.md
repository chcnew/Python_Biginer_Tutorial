# linux与python

# linux基本环境依赖库
```shell
yum remove cmake -y ; yum install -y gcc gcc-c++ make automake openssl openssl-devel
```

# 安装cmake指定版本
```shell
1、移除老版本cmake版本并安装依赖包

 yum remove cmake -y ; yum install -y gcc gcc-c++ make automake openssl openssl-devel
2、下载cmake-3.7.2.tar.gz安装包并解压  cmake官网地址 https://cmake.org/download/ 

wget https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz ; tar -zxf cmake*.tar.gz
3、编译/安装

cd cmake* ; ./bootstrap ; gmake -j `grep 'processor' /proc/cpuinfo | wc -l` ; gmake install
4、查看编译后的cmake版本并创建连接

/usr/local/bin/cmake --version
ln -s /usr/local/bin/cmake /usr/bin/
5、验证新版本

cmake --version
```

# Googletest安装流程
1、从官网下载ubuntu下安装的source文件，下载链接为：https://github.com/google/googletest.git

2、解压之后，cd到对应目录中，然后使用cmake进行编译，再进行make生成两个静态库libgtest.a libgtest_main.a，操作流程为：

```
cd /usr/local/googletest-main
mkdir build
cd build
cmake ..
make
```


3、将步骤2中生成的两个库文件及/googletest/include/gtest文件，复制到用户目录下，操作如下：

```
sudo cp libgtest*.a  /usr/lib 
sudo cp -a /home/bruce/software/googletest-master/googletest/include/gtest /usr/include
```


至此Googletest就已经安装完成。

##  Googletest在make报错
```
error: #error This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.
…
…
cc1plus: all warnings being treated as errors
CMakeFiles/gtest.dir/build.make:62: recipe for target ‘CMakeFiles/gtest.dir/src/gtest-all.cc.o’ failed
make[2]: *** [CMakeFiles/gtest.dir/src/gtest-all.cc.o] Error 1
CMakeFiles/Makefile2:104: recipe for target ‘CMakeFiles/gtest.dir/all’ failed
make[1]: *** [CMakeFiles/gtest.dir/all] Error 2
Makefile:83: recipe for target ‘all’ failed
make: *** [all] Error 2
```

**解决办法：**

在安装包的googletest文件夹下(/home/bruce/software/googletest-master/googletest)找到CmakeLists.txt， 在其中添加如下语句：

```
add_definitions(-std=c++11)
```

添加如下：

```
# Note: CMake support is community-based. The maintainers do not use CMake
# internally.

cmake_minimum_required(VERSION 3.5)
add_definitions(-std=c++11)

if (POLICY CMP0048)
  cmake_policy(SET CMP0048 NEW)
endif (POLICY CMP0048)
```


再次make，便可以成功！