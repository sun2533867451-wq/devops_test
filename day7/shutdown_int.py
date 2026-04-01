'''
文件作业：批量审计设备配置中的 shutdown 接口
编写 一个 Python 脚本，自动完成以下三步：

创建 backup/ 目录，写入以下 4 个设备配置文件：
files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}
遍历 backup/ 目录，找出含有 shutdown（排除 no shutdown）接口的配置文件，打印文件名
搜索完成后，自动删除 backup/ 目录及其所有文件
期望输出：
发现包含 shutdown 接口的设备配置文件:
R1_config.txt
SW1_config.txt
backup/ 目录已清理
代码提示: 使用 os.makedirs() 创建目录，os.listdir() 遍历目录，字符串方法排除 no shutdown，shutil.rmtree() 删除目录。
'''


import os
import shutil

# 1. 准备数据
backup_dir = 'backup'
files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}
# 2. 创建目录并写入文件
# exist_ok=True 避免目录已存在时报错
os.makedirs(backup_dir,exist_ok=True)
for filesname, content in files.items():
    file_path = os.path.join(backup_dir,filesname)
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(content)
# 3. 遍历目录并搜索特定接口状态
print("发现包含 shutdown 接口的设备配置文件：")

for file_name in os.listdir(backup_dir):
    file_path =os.path.join(backup_dir,file_name)
    #定位文件
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-8') as f:
            content = f.read()
            #判断是否有shutdown接口
            if content.count('shutdown')-content.count('no shutdown')>0:
                print(file_name)
#4. 删文件
shutil.rmtree(backup_dir)
print(f"\n{backup_dir}/ 目录已清理")