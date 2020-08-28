# 使用 Python 脚本同步 Gralde 服务器镜像
- Python,Gradle,服务器,镜像
- 2018.05.09

Android 开发离不开 Gralde，而国内下载 Gradle 又特别的慢，为了方便团队内的小伙伴开发，我申请了一台内网服务器，这台服务器的一个作用就是做 Gradle zip 包的下载镜像。

Android 开发离不开 Gralde，而国内下载 Gradle 又特别的慢，为了方便团队内的小伙伴开发，我申请了一台内网服务器，这台服务器的一个作用就是做 Gradle zip 包的下载镜像。

## 镜像服务器

镜像服务器我采用的 nginx 服务器，简单的配置一个下，域名 downloads.gradle.org ，端口 80 ，然后指定一下 root 地址。然后把我写的脚本放在这个目录下，执行脚本就可以了。执行脚本可能会碰见一下问题，比如我是用 Python3 写的，如果服务器上没有 Python3 需要安装以下。还有就是一些模块可能没有安装，pip3 install 一下就行了。

## 客户端使用

客户端需要把 https 改成 http，然后就是改一下 hosts ，把 downloads.gradle.org 指向内网的服务器 ip 地址。 这样下载 gradle zip 文件就飞快了。

## 源代码

大致代码如下：

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    from pyquery import PyQuery as pq
    import os
    import requests


    def download_file(url,path):
        print('准备下载 ' + url)
        if '-rc-' in url or '-milestone-' in url:
            print('\t-rc- 和 -milestone- 的包不下载.')
            return

        dir = os.path.dirname(path)
        if dir != '' and not os.path.exists(dir):
            os.makedirs(dir)

        resq = requests.head(url)
        content_length = int(resq.headers['Content-Length'])
        print('\t下载文件大小 : ' + str(content_length))

        file_size = 0
        if os.path.exists(path):
            file_size = os.stat(path).st_size
        print('\t本地文件大小 : ' + str(file_size))

        if content_length == file_size and content_length != 0 :
            print('\t文件大小一致，不需要下载.')
            return

        if os.path.exists(path):
            os.remove(path)

        print('\t开始下载 ' + url)
        r = requests.get(url,stream=True)

        with open(path,'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk :
                    file.write(chunk)

    # https://downloads.gradle.org/distributions/distributions/gradle-4.7-all.zip
    _DOWN_LOAD_URL = 'http://downloads.gradle.org'
    _BASE_URL_ = 'https://services.gradle.org/distributions/'

    r = requests.get(_BASE_URL_)
    d = pq(r.content)
    items = d('a')
    for item in items:
        a = pq(item)
        herf = a.attr('href')
        if herf.endswith('-all.zip') :
            url = _DOWN_LOAD_URL + herf
            path = herf[1:]
            download_file(url,path)
