# _*_ coding: utf-8 _*_

"""
功能：
"""

# 导入 importlib 模块
import importlib
from importlib import util
# 1. 动态导入模块
module_name = "math"
math_module = importlib.import_module(module_name)
print(f"Imported Module: {math_module}")

# 2. 动态导入模块的属性或方法
sqrt_function = importlib.import_module(module_name).sqrt
result = sqrt_function(25)
print(f"Square Root using import_module: {result}")

# 3. 创建一个模块对象
spec = importlib.util.find_spec(module_name)
math_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(math_module)
print(f"Created Module Object: {math_module}")

# 4. 重新加载模块
reloaded_math_module = importlib.reload(math_module)
print(f"Reloaded Module: {reloaded_math_module}")

# 5. 检查模块是否已经导入
is_imported = importlib.util.find_spec("random") is not None
print(f"Is 'random' Module Imported: {is_imported}")

# 6. 从文件路径导入模块
module_path = "/path/to/custom_module.py"
custom_module = importlib.machinery.SourceFileLoader("custom_module", module_path).load_module()
print(f"Imported Custom Module: {custom_module}")

# 7. 获取模块的规范（Specification）
module_spec = importlib.util.find_spec("sys")
print(f"Module Specification: {module_spec}")

# 8. 获取模块的规范信息
module_spec_info = importlib.util.spec_from_file_location("example_module", "/path/to/example_module.py")
print(f"Module Specification Info: {module_spec_info}")

# 9. 加载模块的规范
loaded_module_spec = importlib.util.module_from_spec(module_spec_info)
module_spec_info.loader.exec_module(loaded_module_spec)
print(f"Loaded Module from Specification: {loaded_module_spec}")

# 10. 获取已加载模块的字典
loaded_modules_dict = importlib.sys.modules
print(f"Loaded Modules Dictionary: {loaded_modules_dict}")

