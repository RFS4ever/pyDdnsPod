#!/usr/bin/env python3
#
# 获取域名列表
# curl -X POST https://dnsapi.cn/Domain.List -d 'login_email=api@dnspod.com&login_password=password&format=json'
#
# 获取记录列表
# curl -X POST https://dnsapi.cn/Record.List -d 'login_email=api@dnspod.com&login_password=password&format=json&domain_id=2317346'

import socket
import urllib
import json
import time

__author__ = 'RFS4ever'
version = 0.1

current_ip = None


def ddns(ip):
    ddns_server_url = 'https://dnsapi.cn/Record.Ddns'

    params = dict(
        login_email='email',  # Change to yours
        login_password='password',  # Change to yours
        format='json',
        domain_id='8888',  # Change to yours
        record_id='8888',  # Change to yours
        sub_domain='ddns',  # Change to yours
        record_line='默认',
    )
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/json",
        "User-Agent": "pyDdnsPod/0.1 (beyondrookie#gmail.com)"
    }


def get_public_ip():
    """Create socket connection to get the current public ip address"""

    addr = ('ns1.dnspod.net', 6666)
    sock = socket.create_connection(addr)
    publicIP = sock.recv(16)
    sock.close()
    return publicIP


def main():
    while True:
        ip = get_public_ip()

        time.sleep(60 * 60)  # 1 hour


if __name__ == '__main__':
    main()