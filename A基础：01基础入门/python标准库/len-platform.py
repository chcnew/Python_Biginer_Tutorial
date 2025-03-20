# _*_ coding: utf-8 _*_

"""
功能：
"""
import platform

# 1. 返回操作系统的名称，例如 'Windows'、'Linux'、'Darwin'（MacOS）等。
system_name = platform.system()
print(f"Operating System: {system_name}")

# 2. 返回操作系统的版本信息。
system_version = platform.version()
print(f"Operating System Version: {system_version}")

# 3. 返回一个字符串，包含操作系统的名称、版本和架构信息。
system_info = platform.platform()
print(f"System Information: {system_info}")

# 4. 返回一个元组，包含解释器的位数和操作系统的位数。
arch_info = platform.architecture()
print(f"Architecture Information: {arch_info}")

# 5. 返回硬件的架构信息。
machine_info = platform.machine()
print(f"Machine Architecture: {machine_info}")

# 6. 返回处理器的信息。
processor_info = platform.processor()
print(f"Processor Information: {processor_info}")

# 7. 返回 Python 解释器的版本信息。
python_version = platform.python_version()
print(f"Python Version: {python_version}")

# 8. 返回 Python 解释器的编译器信息。
compiler_info = platform.python_compiler()
print(f"Python Compiler Information: {compiler_info}")

# 9. 返回一个包含构建信息的元组，包括构建号、构建日期等。
build_info = platform.python_build()
print(f"Python Build Information: {build_info}")

# 10. 返回 Python 解释器的分支信息。
branch_info = platform.python_branch()
print(f"Python Branch Information: {branch_info}")

# 11. 返回 Python 解释器的实现，可能是 'CPython'、'Jython'、'IronPython' 等。
implementation_info = platform.python_implementation()
print(f"Python Implementation: {implementation_info}")

# 12. 返回 Python 解释器的修订号。
revision_info = platform.python_revision()
print(f"Python Revision: {revision_info}")

# 13. 返回 Python 版本的元组，包含主版本、次版本和修订号。
version_tuple = platform.python_version_tuple()
print(f"Python Version Tuple: {version_tuple}")

# 14. 返回一个包含系统相关信息的元组，包括系统名称、主机名、系统版本等。
system_info_tuple = platform.uname()
print(f"System Information Tuple: {system_info_tuple}")

