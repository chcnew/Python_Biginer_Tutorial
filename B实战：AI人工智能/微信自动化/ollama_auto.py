# _*_ coding: utf-8 _*_

"""
功能：
"""
import json
import re

import ollama

# 加载 DeepSeek 模型
model = "deepseek-r1"


def remove_think_tags(text):
    # 使用正则表达式匹配并删除 <think> 标签及其中的内容
    cleaned_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return cleaned_text.strip()


# 定义问答函数
def get_answer(question):
    try:
        # 调用模型进行问答
        resp = ollama.chat(model=model,
                           messages=[
                               {"role": "user", "content": question}
                           ])
        answer = remove_think_tags(json.loads(resp.model_dump_json())["message"]["content"])
        return answer
    except Exception as e:
        print(f"调用模型时发生错误: {e}")
        return None


# def run_command(command):
#     try:
#         # 执行命令并获取输出
#         result = subprocess.run(command, capture_output=True, text=True, check=True)
#
#         # 打印标准输出
#         print("输出:", result.stdout)
#
#         # 打印标准错误
#         if result.stderr:
#             print("错误:", result.stderr)
#     except subprocess.CalledProcessError as e:
#         print(f"命令执行失败: {e}")
#     except Exception as e:
#         print(f"发生异常: {e}")


if __name__ == '__main__':
    # 示例问题
    question = "Python 是什么？"

    # 获取答案
    answer = get_answer(question)
    print("问题:\n", question)
    print("答案:\n", answer)

    # os.chdir(r"C:\Users\Administrator\AppData\Local\Programs\Ollama")
    # cmd = "ollama run deepseek-r1 \"Python 是什么？\""
    # run_command(cmd)
