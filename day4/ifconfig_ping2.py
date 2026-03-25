import os
import re

# 1. 获取输入数据
result = os.popen("ifconfig ens160").read()

# --- 第一步：正则表达式提取 ---

# 提取 IP, Netmask, Broadcast
# 逻辑：匹配关键词后的第一个 IP 格式字符串
ip_info = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)\s+netmask\s+(\d+\.\d+\.\d+\.\d+)\s+broadcast\s+(\d+\.\d+\.\d+\.\d+)', result)
# 提取 MAC 地址
mac_info = re.search(r'ether\s+([0-9a-fA-F:]{17})', result)

if ip_info and mac_info:
    ip = ip_info.group(1)
    netmask = ip_info.group(2)
    broadcast = ip_info.group(3)
    mac = mac_info.group(1)

    # 使用 format 格式化打印
    print("{:<12}: {}".format("IP", ip))
    print("{:<12}: {}".format("Netmask", netmask))
    print("{:<12}: {}".format("Broadcast", broadcast))
    print("{:<12}: {}".format("MAC", mac))

    # --- 第二步：拼接网关并执行 Ping ---

    # 提取 IP 前三段并拼接 .1
    # rsplit('.', 1) 从右边切分一次，拿到 ['196.21.5', '228']
    gateway = ip.rsplit('.', 1)[0] + '.1'
    print(f"\n假设网关为: {gateway}")
    print(f"Ping {gateway} ... ", end="", flush=True)

    # 执行 ping 命令 (发送1个包 -c 1，等待1秒 -W 1)
    # 在 Windows 下请将 -c 替换为 -n
    ping_res = os.popen(f"ping -c 1 -W 1 {gateway}").read()

    if "1 received" in ping_res or "0% packet loss" in ping_res:
        print("reachable")
    else:
        print("unreachable")
else:
    print("未能解析到网络信息，请检查输入内容。")