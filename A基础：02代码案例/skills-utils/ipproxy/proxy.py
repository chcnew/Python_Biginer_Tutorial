# _*_coding: utf-8 _*_

"""
功能：获取快代理免费可用的代理ip
快代理ip网页：https://www.kuaidaili.com/free/inha/
实现思路：
第一步：构造主页url地址，发送请求获取响应
第二步：解析数据，将数据分组
第三步：将数组的数据提取出来
第四步：检测代理IP的可用性
第五步：保存到文件中
"""

import requests
from lxml import etree  # 网页转换为Elements对象的库
import time
from typing import List, Tuple


class ProxyPool:
    def __init__(self, pages: List[int] or Tuple[int] or int = None):
        """
        :param pages: 爬取页范围
        """
        self.pages = pages
        self.target_url = "https://www.kuaidaili.com/free/inha"
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/95.0.4638.69 Safari/537.36'

    @staticmethod
    def save(can_use):
        """可用ip写入文件"""
        with open('IP.txt', 'w') as wf:
            for i in range(len(can_use)):
                s = str(can_use[i]) + '\n'
                wf.write(s)

    @staticmethod
    def parse_data(data):
        """解析数据"""
        html_data = etree.HTML(data)  # 数据转换
        parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')  # 分组数据
        return parse_list

    def send_request(self, page):
        """发送请求，获取响应"""
        print("=============正在抓取第{}页===========".format(page))
        # 目标网页，添加headers参数
        base_url = '{}/{}/'.format(self.target_url, page)
        headers = {"user-agent": self.user_agent}

        # 发送请求：模拟浏览器发送请求，获取响应数据
        response = requests.get(base_url, headers=headers)
        data = response.content.decode()
        time.sleep(1)
        return data

    def check_ip(self, proxies_list):
        """检测代理ip是否可用"""
        headers = {'user-agent': self.user_agent}
        can_use = []
        for proxies in proxies_list:
            try:
                response = requests.get('https://www.baidu.com/', headers=headers, proxies=proxies, timeout=0.1)
                if response.status_code == 200:
                    can_use.append(proxies)
            except Exception as e:
                print(e)
        return can_use

    def run(self):
        proxies_list = []
        # 实现翻页获取数据
        if not self.pages:
            self.pages = [1, 1]
        if isinstance(self.pages, int):
            self.pages = [1, self.pages]
        for page in range(*self.pages):
            data = self.send_request(page)
            parse_list = self.parse_data(data)
            # 循环解析到的数据列表
            for tr in parse_list:
                proxies_dict = {}
                http_type = tr.xpath('./td[4]/text()')
                ip_num = tr.xpath('./td[1]/text()')
                port_num = tr.xpath('./td[2]/text()')
                http_type = ' '.join(http_type)
                ip_num = ' '.join(ip_num)
                port_num = ' '.join(port_num)
                # 拼接为ip:端口形式
                proxies_dict[http_type] = ip_num + ":" + port_num
                proxies_list.append(proxies_dict)
        print("获取到的代理IP数量：", len(proxies_list))
        can_use = self.check_ip(proxies_list)
        print("能用的代理IP数量：", len(can_use))
        print("能用的代理IP:", can_use)
        self.save(can_use)


if __name__ == '__main__':
    proxy_pool = ProxyPool(10)
    proxy_pool.run()
