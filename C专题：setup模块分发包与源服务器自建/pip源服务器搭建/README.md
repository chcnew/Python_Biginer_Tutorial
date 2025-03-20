# pypi-server+nginx搭建pip源

学习链接：https://blog.csdn.net/hekaiyou/article/details/109996487

## 一、安装pypiserver

```shell
# python>=3.7,<=3.8
pip install pypiserver==1.4.2
```

​	**1.4.2版本启动参数含义**

```
-P xxx # 大写表示密码
-a . # 认证方式启动
-p 8888  # 小写表示端口
--fallback-url http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/    # 当请求的Python包在本地上没有找到时，我们可以将请求转发到外部PyPI源
```

​	**pypiserver1.4.2版本启动命令**

```shell
# 无认证方式且直接启动
pypi-server -p 8888 --fallback-url http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/ /data/pip3Src8888/

# nginx反向代理端口启动
pypi-server -p 10012 --fallback-url http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/ /data/pip3Src8888/

# 后台启动
pgrep -f pypi-server | xargs kill -9
nohup pypi-server -p 10012 --fallback-url http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/ /data/pip3Src8888/ > ~/nohup.out 2>&1 &
```



## 二、Nginx反向代理配置

### 1. pypi服务nginx反向代理配置文件pypi.conf

```nginx
mkdir -p /usr/local/nginxAgent/myconf/
vim /usr/local/nginxAgent/myconf/pypi.conf
tee /usr/local/nginxAgent/myconf/pypi.conf <<-'EOF'

upstream pypiserver {
  server 127.0.0.1:10012;
}

server {
  listen 8888;

  # disable any limits to avoid HTTP 413 for large package uploads
  client_max_body_size 0;

  location / {
    proxy_pass http://pypiserver/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    # When setting up pypiserver behind other proxy, such as an Nginx instance, remove the below line if the proxy already has similar settings.
    proxy_set_header X-Forwarded-Proto $scheme;

    proxy_buffering off;
    proxy_request_buffering off;
  }

  location /packages/ {
    alias /data/mypypi/;
    autoindex on;
  }
}

EOF
```

### 2. 配置nginx多文件支持

```shell
vim /usr/local/nginxAgent/conf/nginx.conf
# 添加这一句
# include /usr/local/nginxAgent/myconf/*.conf;
```

```nginx
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
	... ...
    #gzip  on;
	... ...
	include /usr/local/nginxAgent/myconf/*.conf;
}
```



### 3. 验证配置文件与重启nginx服务

```
/usr/local/nginxAgent/sbin/nginx -t
/usr/local/nginxAgent/sbin/nginx -s reload
```

