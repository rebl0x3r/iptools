#!/usr/bin/python3
# python3 formatter.py

import os,sys,time,random,re
from datetime import date

d = []
date = date.today()
dl = date.strftime("%d-%m-%Y")
title = "IP-2-DOMAIN | {} | @MrBlackX".format(dl)

os.system('echo -n -e "\033]0;{}\007"'.format(title))
os.system('clear')

num = 0

print("""
\033[37;1m    ______                           __  __           
   / ____/___  _________ ___  ____ _/ /_/ /____  _____\033[31mV1\033[37m
  / /_  / __ \/ ___/ __ `__ \/ __ `/ __/ __/ _ \/ ___/
 / __/ / /_/ / /  / / / / / / /_/ / /_/ /_/  __/ /    
/_/    \____/_/  /_/ /_/ /_/\__,_/\__/\__/\___/_/     
                                                    
\t  \033[35m M A D E  B Y  @ M R B L A C K X
\033[0m
""")

def formatter(url):
	if re.findall(r':\/\/',url):
		url = re.sub(r':\/\/', '', url)

	if re.findall(r'https?', url):
		url = re.sub(r'https?', '' , url)

	if re.findall(r'\/$', url):
		url = re.sub(r'\/$', '' , url)

	return url

def save(filename, content):
	temp = open(filename, 'a')
	temp.write(content)
	temp.close()

def main():
	urls = input("\033[34;1m[FORMATTER] \033[32;1mDOMAINS/URLS:\033[0m\033[37;1m ")
	urls = open(urls,'r')
	urls = urls.readlines()
	length = len(list(urls))
	for url in urls:
		global num
		num += 1
		url = url.replace("\n", "")
		out = formatter(url)
		print(f"\033[34m[\033[37m{num}\033[34m|\033[37m{length}\033[34m] \033[32m{url}  \033[32m[Formatted] ===> {out}\033[0m")
		save('domains-formatted.txt', f'{out}\n')


if __name__ == '__main__':
	main()