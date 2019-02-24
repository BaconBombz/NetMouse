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
from startalistener import *

def netCatMenu():
    print(tc.lBlue)
    title()
    print("1) Start A Listener")
    time.sleep(0.2)
    print("2) Connect To A Listener")
    longl()
    option = input("(" + tc.lGreen + "MainMenu/NetCat" + tc.lBlue + ")" + tc.lBlue + "> " + tc.yellow)
    netCatOps(option)

def netCatOps(option):
    if (option == "1"):
        startAListener()
