# miniforge3

Miniforge3是一个轻量级的Python发行版，基于Conda，旨在提供一个开源的Python包管理和环境管理解决方案。要开始使用Miniforge3，可以按照以下步骤：

1. **安装Miniforge3**：

   https://github.com/conda-forge/miniforge

   下载适合你系统的安装包，然后运行安装命令。例如，在Linux上，你可以使用`bash Miniforge3-Linux-x86_64.sh`。

   环境变量配置：

   ```shell
   # windows
   D:\Softwares\miniforge3;D:\Softwares\miniforge3\Scripts;D:\Softwares\miniforge3\Library\bin
   
   # linux
   /usr/local/miniforge3/bin
   ```

   

2. **更新Conda**：安装后，更新Conda本身：

   ```
   mamba update conda
   ```

3. **创建环境**：使用以下命令创建一个新的环境：

   ```
   mamba create --name myenv python=3.9.13
   ```

4. **激活/停用环境**：激活你创建的环境：

   ```
   mamba activate myenv
   mamba deactivate
   ```

5. **安装包**：在激活的环境中安装所需的包：

   ```
   mamba install numpy
   ```

6. **列出环境**：查看所有环境：

   ```
   mamba env list
   ```

7. **删除环境**：删除不再需要的环境：

   ```
   mamba remove --name myenv --all
   ```

