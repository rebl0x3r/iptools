#!/usr/bin/python3
# python3 ip-domain.py



import socket,os,sys,threading,queue,time,random
from datetime import date

d = []
date = date.today()
dl = date.strftime("%d-%m-%Y")
title = "DOMAIN-2-IP | {} | @MrBlackX".format(dl)

os.system('echo -n -e "\033]0;{}\007"'.format(title))
os.system('clear')

num = 0


print("""
\033[37;1m  ____                        _       ____  ___ ____  
 |  _ \  ___  _ __ ___   __ _(_)_ __ |___ \|_ _|  _ \\033[31mV3\033[37m 
 | | | |/ _ \| '_ ` _ \ / _` | | '_ \  __) || || |_) |
 | |_| | (_) | | | | | | (_| | | | | |/ __/ | ||  __/ 
 |____/ \___/|_| |_| |_|\__,_|_|_| |_|_____|___|_|    \033[0m

\t  \033[35m M A D E  B Y  @ M R B L A C K X
\033[0m
""")


class Checker:
  inputQueue = queue.Queue()

  def __init__(self):
    self.leads = input("\033[34;1m[DOMAIN-2-IP] \033[32;1mURLs:\033[0m\033[37;1m ")
    self.threads = input("\033[34;1m[DOMAIN-2-IP] \033[32;1mHow many threads?:\033[0m\033[37;1m ") 
    self.length = len(list(open(self.leads)))
    print('')

  def save_to_fie(self, sent, lead):
      kl = open(sent, "a+")
      kl.write(lead)
      kl.close()

  def send(self,target):
    ip = target
    try:
      s = socket.gethostbyname(Hostname)
      return s
    except socket.herror:
      #pass
      return 'dead'
  
  def check(self):
    global num
    global l
    while 1:
      target = self.inputQueue.get()
      num += 1
      result = self.send(target)
      if result == "dead":
        print(f"\033[34m[\033[37m{num}\033[34m|\033[37m{self.length}\033[34m] \033[31m{target} \033[31m[Not Valid]\033[0m")

      else:
        print(f"\033[34m[\033[37m{num}\033[34m|\033[37m{self.length}\033[34m] \033[32m{target}  \033[32m[Valid] ===> {result}\033[0m")
        kl = open("IPs.txt", "a+")
        kl.write(result+"\n")
        kl.close()

  def run_thread(self):
    while True:
      for x in range(int(self.threads)):
        t = threading.Thread(target=self.check)
        t.setDaemon(True)
        t.start()
      for y in open(self.leads, 'r').readlines():
        self.inputQueue.put(y.strip())
      self.inputQueue.join()

start = Checker()
start.run_thread()
