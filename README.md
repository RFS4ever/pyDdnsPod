pyDdnsPod
=========

#### 我的DNSPod动态域名解析脚本。My DNSPod DDNS script.

+ Base on [python3](https://.python.org/ "Python")
+ Change dynamic ip record on [DNSPod](https://www.dnspod.cn/ "DNSPod.cn")
+ Used on my [Raspberry Pi](http://www.raspberrypi.org/ "Raspberry Pi")

#### 获取域名列表
`curl -X POST https://dnsapi.cn/Domain.List -d 'login_email=api@dnspod.com&login_password=password&format=json'`

#### 获取记录列表
` curl -X POST https://dnsapi.cn/Record.List -d 'login_email=api@dnspod.com&login_password=password&format=json&domain_id=2317346'`

******
Free for everyone. Have fun!