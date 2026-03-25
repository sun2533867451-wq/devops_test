'''
正则表达式 + os模块：解析ifconfig并ping网关（一个脚本完成）
首先用 os.popen 执行 Linux 命令获取网卡信息:

import os
result = os.popen("ifconfig ens35").read()
如果没有 Linux 环境，可以直接使用下面的字符串作为输入:

result = """ens35: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 196.21.5.228  netmask 255.255.255.0  broadcast 196.21.5.255
        inet6 fe80::20c:29ff:fe4d:73b3  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:4d:73:b3  txqueuelen 1000  (Ethernet)
        RX packets 13573278  bytes 13853395220 (12.9 GiB)
        RX errors 0  dropped 15  overruns 0  frame 0
        TX packets 6514517  bytes 1749699427 (1.6 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0"""
第一步：用正则表达式提取 IP、掩码、广播地址、MAC，使用 format() 对齐打印:

IP        : 196.21.5.228
Netmask   : 255.255.255.0
Broadcast : 196.21.5.255
MAC       : 00:0c:29:4d:73:b3
第二步：根据 IP 地址的前三段拼接网关地址（假设网关为 x.x.x.1），然后用 os.popen 执行 ping 测试:

假设网关为: 196.21.5.1
Ping 196.21.5.1 ... reachable
'''

import os
import re

# 使用模拟数据（容器环境无真实网卡）
'''
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255
        inet6 fe80::20c:29ff:fe14:7a3c  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:14:7a:3c  txqueuelen 1000  (Ethernet)
        RX packets 873822  bytes 1107987466 (1.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 201201  bytes 35352481 (33.7 MiB)
        TX errors 0  dropped 58 overruns 0  carrier 0  collisions 0

'''
result = os.popen("ifconfig ens160").read()
print(result)
# broadcast 和 ether 之间有 inet6 一行，需用 .*? + re.DOTALL 跨行匹配
regex = r'inet\s+(\d+\.\d+\.\d+\.\d+)\s+netmask\s+(\d+\.\d+\.\d+\.\d+)\s+broadcast\s+(\d+\.\d+\.\d+\.\d+).*?ether\s+([0-9a-fA-F:]{17})'

match = re.search(regex, result, re.DOTALL)
if match:
    ip, netmask, broadcast, mac = match.groups()
    print("{:<10}: {}".format("IP", ip))
    print("{:<10}: {}".format("Netmask", netmask))
    print("{:<10}: {}".format("Broadcast", broadcast))
    print("{:<10}: {}".format("MAC", mac))

    gateway = ".".join(ip.split(".")[:3]) + ".1"
    print(f"\n假设网关为: {gateway}")
    ping_result = os.popen(f"ping -c 2 -W 1 {gateway}").read()
    if "1 received" in ping_result or "2 received" in ping_result:
        print(f"Ping {gateway} ... reachable")
    else:
        print(f"Ping {gateway} ... unreachable")
else:
    print("未匹配到网卡信息")
