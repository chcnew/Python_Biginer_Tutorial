# -*- coding: utf-8 -*-

import json
import ssl
from http.client import HTTPConnection, HTTPSConnection
from urllib.parse import urlparse


class HttpClientUserDefine:
    """用户自定义Http客户端"""

    def __init__(self, url, body, headers, method):
        """
        :param url:
        :param body:
        :param headers:
        :param method:
        """
        self.url = url
        self.body = body
        self.headers = headers
        self.method = method

        self.urlparser = urlparse(url)

        self.netloc = self.urlparser.netloc
        self.path = self.urlparser.path
        self.query = self.urlparser.query
        self.scheme = self.urlparser.scheme

        self.connection = None

    def get_connection(self):
        """获取连接，超时设置为2分钟"""
        if self.scheme == "http":
            conn = HTTPConnection(self.netloc, timeout=2 * 60)
        else:
            ssl._create_default_https_context = ssl._create_unverified_context
            conn = HTTPSConnection(self.netloc, timeout=2 * 60)
        if conn is None:
            raise Exception("http connection is none")
        return conn

    def close_connection(self):
        """关闭连接"""
        if self.connection is not None:
            self.connection.close()

    def request_url(self):
        """请求url处理"""
        url = self.path if self.query == "" else "%s?%s" % (self.path, self.query)
        return url

    def request_body(self):
        """请求body处理"""
        body = self.body
        if body is not None \
                and (isinstance(body, dict) or isinstance(body, list)):
            body = json.dumps(body)
        return body

    def request_headers(self):
        """请求headers处理"""
        body = self.request_body()
        self.headers["Content-Length"] = 0 if body is None else len(body)
        self.headers["Content-Type"] = "application/json; charset=UTF-8"
        return self.headers

    def get_response(self):
        """获取返回数据"""
        self.connection = self.get_connection()
        self.connection.request(self.method, self.request_url(), self.request_body(),
                                self.request_headers())
        return self.connection.getresponse()

    def do_request(self):
        """需在子类中实现"""
        pass


class CommonHttpClient(HttpClientUserDefine):
    """CommonHttpClient"""

    def __init__(self, url, body=None, headers=None, method="POST"):
        """
        :param url:
        :param body:
        :param headers:
        :param method:
        """
        HttpClientUserDefine.__init__(self, url, body, headers, method)

    def do_request(self):
        """重写父类do_request函数"""
        code = 400
        headers = {}
        try:
            response = self.get_response()
            code = response.getcode()
            headers = dict(response.getheaders())
            data = response.read().decode()
        except Exception as e:
            data = json.dumps({"status": "failed", "result": {"reason": str(e)}})
        finally:
            self.close_connection()
        return code, headers, data
