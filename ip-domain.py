#!/usr/bin/python3
# python3 ip-domain.py



import socket,os,sys
from datetime import date

d = []
date = date.today()
dl = date.strftime("%d-%m-%Y")
title = "IP-2-DOMAIN | {} | @MrBlackX".format(dl)

os.system('echo -n -e "\033]0;{}\007"'.format(title))
os.system('clear')

print("""
\033[37;1m
  ___ ____ ____  ____                        _       
 |_ _|  _ \___ \|  _ \  ___  _ __ ___   __ _(_)_ __\033[31mV2\033[37m
  | || |_) |__) | | | |/ _ \| '_ ` _ \ / _` | | '_ \ 
  | ||  __// __/| |_| | (_) | | | | | | (_| | | | | |
 |___|_|  |_____|____/ \___/|_| |_| |_|\__,_|_|_| |_|

\t  \033[35m M A D E  B Y  @ M R B L A C K X
\033[0m
""")


def filecheck():
	if os.path.isfile("Domains.txt"):
		os.rename("Domains.txt", "Domains-Old.txt")

  

def iptodomain(file):
  t = open(file)
  filecheck()
  l = len(t.readlines())
  t.close()
  t = open(file)
  num = 1
  for Hostname in t:
    Hostname = Hostname.rstrip()
    try:
      num += 1
      s = socket.gethostbyaddr(Hostname)[0]
      d.append(s)
      print(f"\033[34m[\033[37m{num}\033[34m|\033[37m{l}\033[34m] \033[32m{Hostname}  \033[32m[Valid] ===> https://{s}\033[0m")
      dd=open("Domains.txt","a+")
      dd.write(s+"\n")
      dd.close()
    except socket.herror:
      print(f"\033[34m[\033[37m{num}\033[34m|\033[37m{l}\033[34m] \033[31m{Hostname} \033[31m[Not Valid]\033[0m")
      continue


f = str(input('\033[34mEnter the file you want to extract: '))
print("\033[0m")
iptodomain(f)
