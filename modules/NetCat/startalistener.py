#!/usr/bin/python3

#Import Necessary Libraries
import sys
import os
import time
import readline

#Append NetMouses' Modules Directories
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules'))

#Import Functions From Other Files
from reqFunc import *
import netcatmenu

#Define Variables
ip = os.system("hostname -I | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'")
port = "4444"
args = ""

def startAListener():
    print(tc.lBlue)
    title()
    print("Port     " + port + "      The Port That The Listener Will Bind To")
    time.sleep(0.2)
    print("Args     " + args + "          Any Other Arguments To Include")
    longl()
    print("Execute     Start The Listener")
    time.sleep(0.2)
    print("Set         Set The Value Of An Option")
    time.sleep(0.2)
    print("Back        Go Back")
    longl()
    option = input("(" + tc.lGreen + "Main Menu/NetCat/Start A Listener" + tc.lBlue + ")" + tc.lBlue + "> " + tc.yellow)
    ops(option)

def ops(option):
    #Define Global Variables
    global port
    global args

    if (option.lower() == "execute"):
        print(tc.lBlue)
        title()
        print("Press CTRL-C To Stop")
        longl()
        print("Your IP Is: " + str(ip))
        time.sleep(0.2)
        print("Listener Port: " + port)
        longl()
        os.system("nc -l -p " + port + " " + args)
        longl()
        back = input("Return To NetCat Menu? ")
        if (back.lower() == "y" or back.lower() == "yes"):
            netcatmenu.netCatMenu()
        else:
            exit()
    elif (option[0:3].lower() == "set"):
        if (option[4:9].lower() == "port "):
            port = option[9:]
            startAListener()
        elif (option[4:9].lower() == "args "):
            args = option[9:]
            startAListener()
        else:
            startAListener()
    elif (option.lower() == "back"):
        netcatmenu.netCatMenu()
    else:
        startAListener()
