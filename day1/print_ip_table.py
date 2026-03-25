'''
假设你负责一个小型网络，有3台设备，请定义变量并打印如下格式的IP规划表:

========== IP地址规划表 ==========
设备名称          管理地址          角色
-----------------------------------------
CoreSwitch        10.1.1.1          核心交换机
Firewall          10.1.1.2          防火墙
WLC               10.1.1.3          无线控制器
=========================================
提示: 可以直接用多个print语句，也可以尝试用 \t (Tab) 来对齐。
'''
#定义设备名称、管理地址、角色
device_name = "CoreSwitch"
device_ip = "10.1.1.1"
device_role = "核心交换机"
device_name2 = "Firewall"
device_ip2 = "10.1.1.2"
device_role2 = "防火墙"
device_name3 = "WLC     "
device_ip3 = "10.1.1.3"
device_role3 = "无线控制器" 

print('============== IP地址规划表 ==============')
print('设备名称\t管理地址\t角色')
print('------------------------------------------')
print(device_name + '\t' + device_ip + '\t' + device_role)
print(device_name2 + '\t' + device_ip2 + '\t' + device_role2)
print(device_name3 + '\t' + device_ip3 + '\t' + device_role3)
print('==========================================')