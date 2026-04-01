
'''
代码提示: 使用 os.popen('ss -tulnp').read() 
获取端口信息，逐行判断是否同时包含 tcp 和 :80 
（注意 避免误匹配 :8080 或 :8000），使用 import time; time.sleep(1) 控制间隔。
'''

import os
import time
while True:
    monitor_result = os.popen("ss -tulnp").read()

    monitor_result_list = monitor_result.split('\n')

    monitor_result_list = monitor_result_list[2:-1]

    #print(monitor_result_list)

    for x in monitor_result_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP（TCP/80）服务已经被打开')
            break
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1)
        continue
    break