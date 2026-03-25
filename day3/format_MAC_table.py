'''
正则表达式测试 1：解析MAC地址表
字符串为交换机MAC地址表内容:

mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
使用正则表达式匹配，提取出 VLAN、MAC地址、类型、接口，使用 format() 对齐后打印结果如下:

VLAN  : 166
MAC   : 54a2.74f7.0326
Type  : DYNAMIC
Port  : Gi1/0/11

intf1 =intf.format(a="Gi0/0", b="up", c="1G")
'''
import re

mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
regex = r"(\d+)\s+(\w+\.\w+\.\w+)\s+(\w+)\s+(\w+/\w+/\d+)"
match = re.search(regex, mac_table)
if match:
    vlan, mac, type, port = match.groups()
    format_table = "{0:<12}: {1}"
    print(format_table.format("VLAN", vlan))
    print(format_table.format("MAC", mac))
    print(format_table.format("Type", type))
    print(format_table.format("Port", port))
else:
    print("未匹配到MAC地址表信息")