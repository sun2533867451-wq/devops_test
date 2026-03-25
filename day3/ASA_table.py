'''
正则表达式测试 2：解析ASA防火墙连接表
字符串为ASA防火墙 show conn 输出:

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
使用正则表达式匹配，提取出协议、目标IP、目标端口、源IP、源端口，使用 format() 对齐后打印结果如下:

Protocol    : TCP
Server IP   : 172.16.1.101
Server Port : 443
Client IP   : 172.16.66.1
Client Port : 53710
'''
import re

conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

regex = r"(\w+)\s+server\s+([\d\.]+):(\d+)\s+localserver\s+([\d\.]+):(\d+)"

match = re.search(regex, conn)

if match:
    # 提取提取分组数据
    protocol, s_ip, s_port, c_ip, c_port = match.groups()
    # 2. 定义打印模板
    # {0:<12} 表示第一个参数左对齐占12个字符
    # {1:<} 表示第二个参数直接跟在后面
    format_table = "{0:<12}: {1}"
    # 3. 格式化打印
    print(format_table.format("Protocol", protocol))
    print(format_table.format("Server IP", s_ip))
    print(format_table.format("Server Port", s_port))
    print(format_table.format("Client IP", c_ip))
    print(format_table.format("Client Port", c_port))
else:
    print("未匹配到连接信息")