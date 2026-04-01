'''
paramiko：SSH 登录 Linux 查询默认网关
安装 paramiko：

pip3 install paramiko
交互界面测试：

>>> import paramiko
>>> ssh = paramiko.SSHClient()
>>> ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
>>> ssh.connect('196.21.5.228', port=22, username='root', password='Cisc0123', timeout=5, look_for_keys=False, allow_agent=False)
>>> stdin, stdout, stderr = ssh.exec_command('hostname')
>>> print(stdout.read().decode())
AIOps
>>> ssh.close()
也可以直接粘贴运行以下脚本快速验证 paramiko 是否安装成功：

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('196.21.5.228', port=22, username='root', password='Cisc0123', timeout=5, look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = ssh.exec_command('hostname')
print(stdout.read().decode())
ssh.close()
预期输出：

AIOps
编写 Python 脚本，封装一个 SSH 执行命令的函数，然后调用该函数 SSH 登录 Linux，执行 route -n，提取并打印默认网关（Destination 为 0.0.0.0 的那一行的 Gateway 字段）：
默认网关: 196.21.5.1
代码提示: 封装函数接收 host、username、password、command 参数，返回命令输出字符串；对 route -n 输出逐行用 re.match 匹配 Destination 为 0.0.0.0 且 Flags 含 UG 的行，用正则表达式捕获组提取网关 IP。

注意：ssh.connect() 建议加上 look_for_keys=False, allow_agent=False，禁用密钥认证，避免连接非 Linux 设备（如思科路由器）时因密钥尝试失败导致认证中断。
'''
import paramiko
import re

def ssh_exec(host, username, password, command):
    # 创建 SSH 客户端
    ssh = paramiko.SSHClient()
    # 自动添加策略，接受不在本地 known_hosts 文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(host, port=22, username=username, password=password, 
                timeout=5, look_for_keys=False, allow_agent=False)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    # 获取输出
    output = stdout.read().decode()
    # 关闭连接
    ssh.close()
    return output

if __name__ == '__main__':
    # 远程主机信息
    host_ip = '10.10.1.201'
    user = 'root'
    pwd = 'huawei@123'  # 确认密码正确，注意大小写
    
    # 1. 远程执行 route -n 获取路由表
    route_output = ssh_exec(host_ip, user, pwd, 'route -n')
    
    # 2. 正则匹配 Destination 为 0.0.0.0 的行，提取网关 IP
    # 示例行: 0.0.0.0         192.168.10.1    0.0.0.0         UG    100    0        0 ens160
    regex_pattern = r'^0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+0\.0\.0\.0\s+UG'
    
    match = re.search(regex_pattern, route_output, re.MULTILINE)
    
    if match:
        gateway = match.group(1)
        print(f"默认网关: {gateway}")
    else:
        print("未找到默认网关。")




