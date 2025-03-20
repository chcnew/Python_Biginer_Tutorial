# _*_encoding: utf-8 _*_

"""
功能：对pytest生成xml解析统计
"""

import json
import os.path
import shutil

import pyecharts.options as opts
import xmltodict
from jinja2 import Template
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType


class ParseRsultXml:
    """ParseRsultXml"""

    def __init__(self, xml_list, output_html):
        self.xml_list = xml_list
        self.output_html = output_html
        self.task_name = os.path.basename(output_html).replace(".html", "")
        self.data_dict, self.data_list = self.retn_data_dict_and_list()
        self.result_dir = os.path.join(os.path.dirname(output_html), "ResultFiles")
        self.chart_html = os.path.join(self.result_dir, "chart.html")
        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

    def retn_data_dict_and_list(self):
        """获取任务层面全部的result/xxx.xml结果数据汇总"""
        data_dict = {
            "TESTS": 0,
            "FAILURES": 0,
            "ERRORS": 0,
            "DISABLED": 0,
            "IGNORED": 0,
            "UNAVAILABLE": 0
        }
        data_list = []
        # 解析xml文件获取结果加至汇总字典
        for xml_path in self.xml_list:
            if not os.path.exists(xml_path):
                continue
            with open(xml_path, 'r', encoding="utf-8") as rfff:
                xml_str = rfff.read()
            json_parse = json.loads(json.dumps(xmltodict.parse(xml_str, encoding="utf-8")))
            for key, value in data_dict.items():
                lowkey = "@" + key.lower()
                data_dict[key] = value + int(json_parse["testsuites"][lowkey])
            result_name_list = [("@" + item.lower()) for item in data_dict.keys()][1:]
            # 内部用例结果
            failed_dict = {
                item.replace("@", "").capitalize(): int(json_parse["testsuites"][item]) for item in
                result_name_list
            }
            count = int(json_parse["testsuites"]["@tests"])
            for key, value in failed_dict.items():
                if key != "UNAVAILABLE" and \
                        count >= value:
                    count = count - value
            # JSON用例总结果
            result = f"Passed"
            for item in result_name_list:
                if int(json_parse["testsuites"][item]) > 0:
                    result = "Failed"
                    break
            result += "({}/{})".format(count, int(json_parse["testsuites"]["@tests"]))
            result_dict = {
                **{"JsonCaseName": json_parse["testsuites"]["@name"], "Result": result,
                   "BlockDir": os.path.basename(
                       os.path.dirname(os.path.dirname(os.path.dirname(xml_path))))},
                **{"Passes": count},
                **failed_dict
            }
            data_list.append(result_dict)
        count = data_dict.pop("TESTS")
        for key, value in data_dict.items():
            if key != "UNAVAILABLE" and \
                    count >= value:
                count = count - value
        data_dict = {"PASSES": count, **data_dict}  # python3.6之后字典有序
        return data_dict, data_list

    def summary_drawing(self):
        """汇总作图"""
        pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        cate = [item for item in self.data_dict.keys()]
        data = [item for item in self.data_dict.values()]
        data_pair = [list(z) for z in zip(cate, data)]
        pie.add("", data_pair, label_opts=opts.LabelOpts(position="outside", formatter="{d}%"))
        pie.set_colors(["#28FF28", "#FF2D2D", "#FF9224", "#FAD985", "#CA8EC2", "#E800E8"])
        #  设置其他配置项
        pie.set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title=self.task_name,
                pos_left='0%'
            ),
            #  图例配置项
            legend_opts=opts.LegendOpts(
                type_="scroll",
                pos_top="20%",
                pos_left="80%",
                orient="vertical"
            ),
        )
        pie.render(path=self.chart_html)
        # 内容替换
        with open(self.chart_html, "r+", encoding="utf-8") as fff:
            content = fff.read()
            content = content.replace(
                "https://assets.pyecharts.org/assets/v5/echarts.min.js", "./echarts.min.js")
            fff.seek(0)
            fff.truncate()
            fff.write(content)
        source_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "templates", "echarts.min.js")
        shutil.copy(source_file, self.result_dir)

    def make_index_page(self):
        """主页展示"""
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "templates", "task_summary_chart.html")
        with open(template_path, "r", encoding="utf-8") as r_file:
            content = r_file.read()
        template = Template(content)
        total = 0
        for value in self.data_dict.values():
            total += int(value)
        pass_yield_flo = int(self.data_dict.get("PASSES")) / total
        pass_yield = "{}/{}*100%={}".format(
            int(self.data_dict.get("PASSES")), total, "%.2f%%" % (pass_yield_flo * 100))
        element = {
            "title": self.task_name,
            "pass_yield": pass_yield,
            "data_dict": self.data_dict,
            "data_list": self.data_list
        }
        with open(self.output_html, "w", encoding="utf-8") as w_file:
            w_file.write(template.render(element))

    def run(self):
        """运行输出图表"""
        self.summary_drawing()
        self.make_index_page()
