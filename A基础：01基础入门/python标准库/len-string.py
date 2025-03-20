# _*_ coding: utf-8 _*_

"""
功能：字符串对象学习
txt=""
txt.isdigit()       # 判断字符串是否只包含数字字符。
txt.isalnum()       # 判断字符串是否只包含字母、数字及中文字符。
txt.isalpha()       # 判断字符串是否只包含字母字符。
txt.isascii()       # 判断字符串是否只包含ASCII字符。
txt.isdecimal()     # 判断字符串是否只包含十进制数字字符。
txt.islower()       # 判断字符串所有字母是否都是小写。
txt.isupper()       # 判断字符串所有字母是否都是大写。
txt.isprintable()   # 判断字符串的字符是否都是可打印字符。
txt.istitle()       # 判断字符串的单词是否都以大写字母开头。
txt.isidentifier()  # 判断字符串是否是一个合法的Python标识符。
txt.isnumeric()     # 判断字符串是否只包含数字字符。
txt.isspace()       # 判断字符串是否只包含空格字符。

string.
- `ascii_letters`：包含所有ASCII字母，即a-z和A-Z。
- `ascii_lowercase`：包含所有小写ASCII字母，即a-z。
- `ascii_uppercase`：包含所有大写ASCII字母，即A-Z。
- `capwords`：将字符串中的每个单词的首字母大写。
- `digits`：包含所有数字0-9。
- `hexdigits`：包含所有十六进制数字，即0-9和a-f/A-F。
- `octdigits`：包含所有八进制数字，即0-7。
- `printable`：包含所有可打印的ASCII字符，包括空格和标点符号。
- `punctuation`：包含所有ASCII标点符号。
- `whitespace`：包含所有ASCII空格字符。
- `Formatter`和`Template`是字符串格式化的工具，用于将变量插入到字符串中。`Formatter`提供了更灵活的格式化选项，而`Template`则提供了更简单的语法。
"""

# 字符串定义
string_example = "Hello, World!"

# 1. 字符串长度
string_length = len(string_example)
print(f"String Length: {string_length}")

# 2. 字符串切片
substring = string_example[7:12]
print(f"Substring: {substring}")

# 3. 查找子字符串的位置
substring_index = string_example.find("World")
print(f"Substring Index: {substring_index}")

# 4. 替换字符串中的部分内容
new_string = string_example.replace("World", "Python")
print(f"Modified String: {new_string}")

# 5. 大小写转换
uppercase_string = string_example.upper()
lowercase_string = string_example.lower()
print(f"Uppercase String: {uppercase_string}")
print(f"Lowercase String: {lowercase_string}")

# 6. 去除字符串两侧的空格
trimmed_string = "   Example String   "
stripped_string = trimmed_string.strip()
print(f"Stripped String: '{stripped_string}'")

# 7. 字符串分割
split_string = string_example.split(", ")
print(f"Split String: {split_string}")

# 8. 字符串连接
joined_string = "-".join(split_string)
print(f"Joined String: {joined_string}")

# 9. 字符串格式化
formatted_string = "Hello, {}!".format("Python")
print(f"Formatted String: {formatted_string}")

# 10. 字符串是否以特定前缀或后缀开始或结束
starts_with_hello = string_example.startswith("Hello")
ends_with_world = string_example.endswith("World")
print(f"Starts with 'Hello': {starts_with_hello}")
print(f"Ends with 'World': {ends_with_world}")

# 11. 字符串是否只包含字母或数字或中文
is_alpha_numeric = string_example.isalnum()
print(f"Is Alpha Numeric: {is_alpha_numeric}")

# 12. 字符串是否只包含字母
is_alpha = string_example.isalpha()
print(f"Is Alpha: {is_alpha}")
