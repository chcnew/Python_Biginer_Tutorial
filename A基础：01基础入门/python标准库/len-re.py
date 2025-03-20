# _*_ coding: utf-8 _*_

"""
功能：

# 1. re.search(pattern, string, flags=0)
# 在字符串中搜索匹配模式的第一个位置。

# 2. re.match(pattern, string, flags=0)
# 在字符串的开头匹配模式。

# 3. re.findall(pattern, string, flags=0)
# 返回字符串中所有匹配模式的非重叠列表。

# 4. re.finditer(pattern, string, flags=0)
# 返回一个迭代器，产生所有匹配模式的匹配对象。

# 5. re.sub(pattern, repl, string, count=0, flags=0)
# 使用 repl 替换字符串中匹配模式的部分。

# 6. re.split(pattern, string, maxsplit=0, flags=0)
# 使用模式分割字符串。

# 7. re.fullmatch(pattern, string, flags=0)
# 确保整个字符串与模式匹配。

# 8. re.escape(string)
# 转义字符串中的特殊字符，使其能够安全地用作模式。

# 9. re.compile(pattern, flags=0)
# 将字符串形式的正则表达式编译为正则对象，可用于多次匹配。

# 10. re.purge()
# 清除正则表达式缓存。

# 11. re.Pattern.search(string, pos=0, endpos=sys.maxsize)
# 正则对象的搜索方法，类似于 re.search()。

# 12. re.Pattern.match(string, pos=0, endpos=sys.maxsize)
# 正则对象的匹配方法，类似于 re.match()。

# 13. re.Pattern.fullmatch(string, pos=0, endpos=sys.maxsize)
# 正则对象的全匹配方法，类似于 re.fullmatch()。

# 14. re.Pattern.finditer(string, pos=0, endpos=sys.maxsize)
# 正则对象的迭代匹配方法，类似于 re.finditer()。

# 15. re.Pattern.findall(string, pos=0, endpos=sys.maxsize)
# 正则对象的查找所有匹配方法，类似于 re.findall()。

# 16. re.Pattern.sub(repl, string, count=0)
# 正则对象的替换方法，类似于 re.sub()。

# 17. re.Pattern.split(string, maxsplit=0)
# 正则对象的分割方法，类似于 re.split()。

# 18. re.Pattern.flags
# 正则对象的标志位。

# 19. re.Pattern.pattern
# 正则对象的模式字符串。

"""

import re

# 要匹配的字符串
text = "Hello, my email is john@example.com. Please contact me there."

# 1. 搜索匹配的字符串
match_result = re.search(r'email', text)
print(f"Search Result: {match_result.group()}")

# 2. 查找所有匹配的字符串
find_all_results = re.findall(r'\w+@[\w.]+', text)
print(f"Find All Results: {find_all_results}")

# 3. 替换匹配的字符串
new_text = re.sub(r'\w+@[\w.]+', 'user@example.org', text)
print(f"Modified Text: {new_text}")

# 4. 判断字符串是否以特定模式开始
starts_with_hello = re.match(r'Hello', text)
print(f"Starts with 'Hello': {starts_with_hello.group() if starts_with_hello else None}")

# 5. 判断字符串中是否存在特定模式
contains_email = re.search(r'\w+@[\w.]+', text)
print(f"Contains Email: {contains_email.group() if contains_email else None}")

# 6. 分割字符串
split_results = re.split(r'\s', text)
print(f"Split Results: {split_results}")

# 7. 使用正则表达式的组
match_with_groups = re.search(r'(\w+)@([\w.]+)', text)
if match_with_groups:
    username, domain = match_with_groups.groups()
    print(f"Username: {username}, Domain: {domain}")

# 8. 匹配开头和结尾
starts_with_hello = re.match(r'^Hello', text)
ends_with_dot = re.search(r'\.$', text)
print(f"Starts with 'Hello': {starts_with_hello.group() if starts_with_hello else None}")
print(f"Ends with '.': {ends_with_dot.group() if ends_with_dot else None}")

# 9. 使用预定义的字符类
digits = re.findall(r'\d', "The price is $15.99")
print(f"Digits: {digits}")

# 10. 使用修饰符（例如，忽略大小写）
case_insensitive_match = re.search(r'John', "john@example.com", re.IGNORECASE)
print(f"Case-Insensitive Match: {case_insensitive_match.group() if case_insensitive_match else None}")
