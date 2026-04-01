'''
字典课堂作业
把防火墙状态信息表存为字典!

注意:一定要考虑很多很多行的可能性

asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""
打印分析后的字典:

{('192.168.189.167', '32806', '137.78.5.128', '65247'): ('74', 'UIO'),
 ('192.168.189.167', '80', '137.78.5.128', '65233'): ('334516', 'UIO')}
键为: 源IP, 源端口, 目的IP, 目的端口；值为: 字节数, Flags

格式化打印输出（使用 format() 对齐，用 | 分隔各列）:

src       : 192.168.189.167 | src_port  : 32806  | dst       : 137.78.5.128 | dst_port  : 65247
bytes     : 74              | flags     : UIO
====================================================================================

src       : 192.168.189.167 | src_port  : 80     | dst       : 137.78.5.128 | dst_port  : 65233
bytes     : 334516          | flags     : UIO
====================================================================================
代码提示: 使用 asa_conn.split('\n') 按行遍历，re.match 提取各组，键为 (源IP, 源端口, 目的IP, 目的端口)，值为 (bytes, flags)。
'''
import re
# 原始数据
asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""
# 初始化字典
conn_dict = {}
# 正则表达式说明：
# (\d+\.\d+\.\d+\.\d+):(\d+)   匹配 IP:端口
# .*?bytes\s+(\d+)             忽略中间字符，直到找到 bytes 关键字并捕获数字
# .*?flags\s+(\w+)             忽略中间字符，直到找到 flags 关键字并捕获字母
regex_pattern = r'TCP\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+)\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+).*?bytes\s+(\d+).*?flags\s+(\w+)'

# 1. 解析数据并存入字典
for line in asa_conn.strip().split('\n'):
    match = re.match(regex_pattern, line)
    if match:
        # 提取各组数据
        src_ip, src_port, dst_ip, dst_port, byte_count, flags = match.groups()
        # 构造字典：键为四元组，值为二元组
        key = (src_ip, src_port, dst_ip, dst_port)
        value = (byte_count, flags)
        conn_dict[key] = value

# 2. 打印分析后的字典对象
print(conn_dict)
print("\n" + "="*84 + "\n")

# 3. 格式化打印输出
for (s_ip, s_port, d_ip, d_port), (b, f) in conn_dict.items():
    # 第一行打印 IP 和 端口
    line1 = "src       : {:<15} | src_port  : {:<6} | dst       : {:<15} | dst_port  : {:<6}".format(
        s_ip, s_port, d_ip, d_port
    )
    # 第二行打印 字节和 标志
    line2 = "bytes     : {:<15} | flags     : {:<6}".format(b, f)
    print(line1)
    print(line2)
    print("=" * 84)
