# _*_coding: utf-8 _*_

"""
功能：关于ip的一些获取，使用等操作
"""

import socket
import subprocess

import requests


class IpFunc:
    """ip处理类"""

    @staticmethod
    def get_intranet_ip():
        """获取内网IP"""
        so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        so.connect(('8.8.8.8', 80))
        res = so.getsockname()[0]
        so.close()
        return res

    @staticmethod
    def get_external_ip():
        """获取外网IP（前提是可以接入外网）"""
        res = requests.get('http://ifconfig.me/ip', timeout=1).text.strip()
        if not res:
            res = requests.get('http://ifconfig.me', timeout=1).text.strip()
        return res

    @staticmethod
    def extract_ip():
        """获取本机ip（执行机可以获取大网ip）"""
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            st.connect(('10.255.255.255', 1))
            ip = st.getsockname()[0]
        except Exception as e:
            print(e)
            ip = '127.0.0.1'
        finally:
            st.close()
        return ip

    @staticmethod
    def filt_ip_list(start="192.168."):
        """
        获取筛选本机非列表开头的ip地址

        :param start: 被排除的ip列表开头（str）
        :return: 筛选后的ip
        """
        if isinstance(start, str):
            not_start_list = [start]
        else:
            not_start_list = start
        proc = subprocess.Popen("ipconfig", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # 命令结束返回信息
        # out, err = proc.communicate()
        # print(out)
        # 命令实时返回信息
        count = 0
        all_ip_list = []
        for line in iter(proc.stdout.readline, 'b'):
            if count >= 66:  # 设置允许的连续空行不可超过66行
                break
            info = str(line, encoding="gbk").strip()
            if info.startswith("IPv4"):
                ip = info.split(":")[1].strip()
                all_ip_list.append(ip)
            count += 1
        # 筛选外网ip
        res_list = []
        for ip in all_ip_list:
            for ip_head_str in not_start_list:
                if not ip.startswith(ip_head_str):
                    res_list.append(ip)
        return res_list


if __name__ == '__main__':
    print(IpFunc.extract_ip())
    print(IpFunc.filt_ip_list())
    print(IpFunc.get_external_ip())
    print(IpFunc.get_intranet_ip())
