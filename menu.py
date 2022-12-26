import pyfiglet
import time
import os
import colorama
from colorama import *
from pyfiglet import *
import random
import sys
###### COLOR SETTINGS ######
r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
b=Fore.BLUE
colors = [r, lg, w, ye, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '*' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
plus = lg + '(' + w + '+' + lg + ')' + rs
####### DONE #######

#### NICE BANNER  #####
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText(' ODOBOT')
    print(random.choice(colors) + logo)
    print(f'{r}   Version: {w}1.0 {r}| Author: {w}Orlando{rs}')   
###########################    
banner()
def sleep():
	time.sleep(2)
menu={
1:"Start Bot",
2:"Install a Malware",
3:"Quit",	   
}
sleep()

for keys in menu.keys():
	print(keys,f"{ye}+{rs}",menu[keys])
opt=int(input(f"{lg}[÷] SELECT OPTION! [÷] {rs}"))

def option1():
	sleep()
	os.system("clear")
	sleep()
	print(f"{lg}{info}[÷] PLEASE WAIT WHILE I BOOT UP THE BOT FOR YOU![÷]{rs}")
	sleep()
	print("done!")
	sleep()
	print(success+lg+"YOUR BOT IS NOW ONLINE BOSS!")
	print(success+ye+f"BOT IS NOW HANDELING ALL INCOMIMG MESSAGES!\n\n\n{info}Press ctrl+c  to stop the process..."+rs)
	os.system("python orlandobot.py")

def option2():
	os.system('clear')
	os.system("pip install bs4")
	sleep()
	os.system("clear")
	sleep()
	print(f"{lg}{info} PLEASE WAIT...[÷]{rs}")
	print(ye+success+"[÷]  DONE BOSS! [÷]{rs}")
	
def option3():
	os.system("clear")
	os.system("pip install phonenumbers")
	sleep()
	opt2={
	1:" 1 for YES",
	2:" 2 for NO"
	}
	for key in opt2.keys():
		print(keys,"-",opt2[key])
	ask=int(input(info+" Are you sure you wanna quit bro ?"))
	if ask == 1:
		sleep()
		os.system("clear")
		sys.exit()
	elif ask == 2:
		os.system("python menu.py")
				


if opt ==1:
	sleep()
	print(lg+info+" hold on bro..."+rs)
	sleep()
	option1()		

elif opt ==2:
	sleep()
	print(lg+info+" hold on bro..."+rs)
	sleep()
	option2()
elif opt == "":
	time.slee(1)
	print(info+lg+"[÷]   WRONG OPTION BRO! "+rs)
	os.system("python menu.py")				
	
elif opt == 3:
	sleep()
	os.system('clear')
	banner()
	print(lg+info+f"{r} there are ustopped jobs bro....{rs}")
	sleep()
	option3()			
	