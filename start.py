import os
import sys
from rich.panel import Panel
from rich import print
import time
import datetime
from rich.console import Console
def banner():
  print(Panel("""[bold red]<[bold green]<[bold white]<[bold blue]
  _________       __                
 /   _____/ _____/  |_ __ ________  
 /_____  /_/ __ /   __/  |  /____ / 
 /        /  ___/|  | |  |  /  |_> >
/_______  //___  >__| |____/|   __/ 
        //     //           |__|    
        """ , style="bold green" ,title="(Welcome)"))
  print(Panel(""" 
  [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]> [bold green]Devloped By Stark [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]>
  [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]> [bold green] INSTA : @mr_lalu_1232 [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]>
  [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]>[bold green] Github : github.com/STARK-404 [bold red]<[bold blue]/[bold red]>[bold red]<[bold blue]/[bold red]>
       """ , style="red" , title="(Developer)"))

def welcom():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        print(Panel(" [bold green]HeyGood morning!" , title=(f" Time is {time_prnt}") , style="green"))
    elif current_time < datetime.time(18):
        print(Panel("[bold blue]Hey Good afternoon!" , title=(f"[bold green] Time is {time_prnt}") , style="green"))
    else:
        print(Panel(f" [bold blue]Hey Good night!", title=(f"[bold green]  Time is {time_prnt} Now!!") , style="green"))
now_time = datetime.datetime.now()
time_prnt = now_time.strftime("%H:%M:%S")


os.system("clear")
welcom();
banner();
print("""
[bold white][[bold blue]1.[bold white]] [bold green] Get FaceBook Hack Orginal Script.
[bold white][[bold blue]2.[bold white]] [bold green] [bold green]Contact Admin/Owner
[bold white][[bold blue]0.[bold white]] [bold green] [bold red]Exit!!!
""")
choose = input("\x1b[92m Enter Your Choice  : ")


if choose == '0' or choose == '00':
	print("Bye!!")
	exit();
if choose == '2' or choose == '02':
	print("[bold green]Redirecting....")
	os.system("xdg-open https://instagram.com/mr_lalu_1232/")
	exit();
	
def inner():
	web = input("\x1b[92m Press(y/\x1b[91mn\x1b[92m)    :  ")
	if web == 'y':
		os.system("xdg-open 'http://starkstore.42web.io/stark.html' ")
		print("[italic green] Happy Buying !! Thankz \n Read Full Instruction !!")
		exit();
	else:
			print("[italic blue] Contact Admin !! \n You will be Redirected to Admin")
			os.system("xdg-open https://instagram.com/mr_lalu_1232/")
			exit();
if choose == '1' or choose == '01':
	os.system("clear")
	print(Panel("""[bold red] Hello, Iam Stark-404 This is A FaceBook Multi Bruteforce Script You Can crack Random Ids from Friend list public id its will crack passwords Without Passwordlist 
	If You need To Use Buy it From Admin 
	[bold green]press (y) [bold red]
	You Are Not Intrested[bold yellow] press (n)
""" , title="(Disclamer)" , style="red"))
inner();
exit();