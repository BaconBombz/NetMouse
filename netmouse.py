#/usr/bin/python3
version = " NetMouse Version: Alpha_1.0"

#Import Necessary Libraries
import sys
import os
import time
import readline

#Append NetMouse's Modules' Directories
sys.path.append("modules/NetCat/")
sys.path.append("modules/")

#Import NetMouse Modules
from reqFunc import *
import netcatmenu

#ARGV Setup
if (len(sys.argv) > 1):
    arg1 = sys.argv[1]
else:
    arg1 = ""

#Command Line Arguments
if (len(arg1) > 1):
    if (arg1 == "-h" or arg1 == "--help"):
        print(help)
    elif (arg1 == "--version"):
        print(version)
    elif (arg1 == "--colorTest"):
        print("\n")
        print(reqFunc.tc.black + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.red + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.green + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.gold + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.blue + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.purple + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.cyan + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lGrey + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.dGrey + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lRed + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lGreen + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.yellow + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lBlue + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lPurple + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.lCyan + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print(reqFunc.tc.white + "The Quick Brown Fox Jumped Over The Lazy Dogs" + reqFunc.tc.noColor)
        print("\n")
    else:
        print("Invalid Argument")

def mainMenu():
    print(tc.lBlue)
    title()
    time.sleep(0.2)
    print("1)   NetCat")
    time.sleep(0.2)
    print("2)   CryptCat")
    time.sleep(0.2)
    print("3)   Nmap")
    time.sleep(0.2)
    print("00)  Exit")
    time.sleep(0.2)
    longl()
    option = input("(" + tc.lGreen + "MainMenu" + tc.lBlue + ")" + tc.lBlue + "> " + tc.yellow)
    mainMenuOps(option)

def mainMenuOps(option):
    if (option == "1"):
        netcatmenu.netCatMenu()
    elif (option == "2"):
        cc
    elif (option == "3"):
        nm
    elif (option == "00"):
        clear()
        exit()
    else:
        mainMenu();

if (len(arg1) == 0):
    mainMenu()
