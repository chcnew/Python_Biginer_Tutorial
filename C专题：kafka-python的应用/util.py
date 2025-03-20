# -*- coding: utf-8 -*-
import socket


class Utils:
    @staticmethod
    def get_local_host():
        """获取ip"""
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            st.connect(('10.255.255.255', 1))
            local_ip = st.getsockname()[0]
        except ConnectionError:
            local_ip = '127.0.0.1'
        finally:
            st.close()
        return local_ip


if __name__ == '__main__':
    print(Utils.get_local_host())
