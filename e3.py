# e3


import os
import sys
import time
from random import random , randint()
from colorama import Fore

def __1__():
    time.sleep(1)
    print(Fore.YELLOW + "Hello . Welcome Back ;)")
    time.sleep(0.4)
    my_list = ["goll" , "puch"]
    rand = my_list(random(0,1))
    for i in range(5):
        time.sleep(0.4)
        i10 = input(Fre.RED + "\n[" + Fore.BLUE +m "!" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "Pleass Enter Your Number\n1 : Goll  |  2 : Puch" + Fore.YELLOW + "  ==>  ")
        if i10 == "" or None:
            try:
                print(Fore.RED + "\nError : Your Number Is Not Found ;(")
                time.sleep(0.7)
                sys.exit()
            except:
                pass
        if i10 == "1" and rand == "goll":
            time.sleep(Fore.GREEN + "\n[+] ~ Your Won ;)")
            time.sleep(0.4)
            sys.exit()
        if i10 == "1" and rand == "puch":
            time.sleep(0.5)
            print(Fore.RED + "\n[-] ~ Your Input Is Dont Ok ;(")
            time.sleep(0.5)
        if i10 == "2" and rand == "goll"
            time.sleep(0.5)
            print(Fore.RED + "\n[-] ~ Your Input Is Dont Ok ;(")
            time.sleep(0.5)
        if i10 == "1" and rand == "puch":
            time.sleep(Fore.GREEN + "\n[+] ~ Your Won ;)")
            time.sleep(0.4)
            sys.exit()
        else:
            print(Fore.YELLOW + f"\n[!] ~ Your Have {5 - i} Time More ;)")
__1__()
