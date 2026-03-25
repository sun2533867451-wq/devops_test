'''
format格式化：打印接口状态巡检报告
定义以下变量，使用 format() 打印一份格式整齐的接口状态报告:

intf1 = "Gi0/0", status1 = "up", speed1 = "1G"
intf2 = "Gi0/1", status2 = "down", speed2 = "1G"
intf3 = "Gi0/2", status3 = "up", speed3 = "10G"
打印效果如下:

接口      状态    速率
--------------------
Gi0/0     up      1G
Gi0/1     down    1G
Gi0/2     up      10G
'''

intf = "{a:<10} {b:<10} {c:10}"

intf1 =intf.format(a="Gi0/0", b="up", c="1G")
intf2 =intf.format(a="Gi0/1", b="down", c="1G")
intf3 =intf.format(a="Gi0/2", b="up", c="10G")
print(f"接口       状态       速率")
print(f"{"-" *26}")
print(intf1)
print(intf2)
print(intf3)   

