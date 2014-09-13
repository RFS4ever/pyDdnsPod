#!/usr/bin/env python3
#
# 获取域名列表
# curl -X POST https://dnsapi.cn/Domain.List -d 'login_email=api@dnspod.com&login_password=password&format=json'
#
# 获取记录列表
# curl -X POST https://dnsapi.cn/Record.List -d 'login_email=api@dnspod.com&login_password=password&format=json&domain_id=2317346'

import socket
import urllib.request
import urllib.parse
from urllib.error import URLError
import json
import time
import datetime

__author__ = 'RFS4ever'
__homepage__ = 'https://github.com/RFS4ever/pyDdnsPod'
version = '0.3'

# Set global default timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

# Initial Configuration
current_ip = None
config = {
    'ddns_api_url': 'https://dnsapi.cn/Record.Ddns',
    'headers': {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/json",
        "User-Agent": u"{0:s}'s pyDdnsPod/{1:s} (beyondrookie#gmail.com)".format(__author__, version)  # Change to yours
    },
    'params': {
        'login_email': 'email',  # Change to yours
        'login_password': 'password',  # Change to yours
        'format': 'json',
        'domain_id': '8888',  # Change to yours
        'record_id': '8888',  # Change to yours
        'sub_domain': 'ddns',  # Change to yours
        'record_line': '默认',
    }
}


def get_public_ip():
    """Create socket connection to get the current public ip address"""

    addr = ('ns1.dnspod.net', 6666)
    sock = socket.create_connection(addr)
    public_ip = sock.recv(16).decode('utf-8')
    sock.close()
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %a')
    print(u'[{0:s}] Public ip is "{1:s}"'.format(now, public_ip))
    return public_ip


def ddns(ip):
    """Connect to the API server, change the ddns's ip record to current public ip"""

    url = config['ddns_api_url']
    params = config['params']
    params.update({'value': ip})
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    headers = config['headers']
    req = urllib.request.Request(url, data, headers)

    try:
        res = urllib.request.urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        # everything is fine
        return_info = res.read().decode('utf-8')
        return_info = json.loads(return_info)

    if return_info.get('status', {}).get("code") == '1':
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %a')
        print('=' * 60)
        print('[%s] New ddns ip has changed to "%s"!' % (now, ip))
        print(json.dumps(return_info, indent=4))
        print('=' * 60)
        return True
    else:
        raise Exception(return_info)


def main():
    global current_ip

    while True:
        try:
            ip = get_public_ip()

            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception as e:
            print(e)
            # print(json.dumps(e.decode('utf-8'), indent=4))

        time.sleep(60 * 60)  # 1 hour (sleep in seconds)


if __name__ == '__main__':
    main()