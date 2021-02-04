#!/usr/bin/python3
# python3 domain-ip.py list.txt
# list without http://
# source : https://github.com/dextercyberlab/Domain-to-IP-Converter
# Fixed & Colored Output 


import socket,os
d = []
os.system('clear')
print("""
\033[37;1m  ____                        _       ____  ___ ____  
 |  _ \  ___  _ __ ___   __ _(_)_ __ |___ \|_ _|  _ \ 
 | | | |/ _ \| '_ ` _ \ / _` | | '_ \  __) || || |_) |
 | |_| | (_) | | | | | | (_| | | | | |/ __/ | ||  __/ 
 |____/ \___/|_| |_| |_|\__,_|_|_| |_|_____|___|_|    \033[0m
                                                                                                                              
	""")

def domaintoip(file):
    with open(file) as t:
        for Hostname in t:  
            Hostname = Hostname.rstrip()
            try:
                s = socket.gethostbyname(Hostname)
                d.append(s)
                print(Hostname + ' \033[32m[Valid] ===> ' + s + "\033[0m")
            except:
                print(Hostname, '\033[31m[Not Valid]\033[0m')
                continue
 
 
    with open('output.txt', 'w') as output:
        for out in d:
            print(out, file=output)
        output.close()
 
f = str(input('\033[34mEnter the file you want to extract: '))
print("\033[0m")
domaintoip(f)
