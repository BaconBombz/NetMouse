#!/usr/bin/python3

#Import Libraries For Functions
import sys
import os
import time
import readline

#Setup Colors
class tc:
    black = '\033[0;30m'
    red = '\033[0;31m'
    green = '\033[0;32m'
    gold = '\033[0;33m'
    blue = '\033[0;34m'
    purple = '\033[0;35m'
    cyan = '\033[0;36m'
    lGrey = '\033[0;37m'
    dGrey = '\033[1;30m'
    lRed = '\033[1;31m'
    lGreen = '\033[1;32m'
    yellow = '\033[1;33m'
    lBlue = '\033[1;34m'
    lPurple = '\033[1;35m'
    lCyan = '\033[1;36m'
    white = '\033[1;37m'
    noColor = '\033[0m'

def lr():
    print("\n")

def clear():
    os.system("clear")

def longl():
    print("--------------------------------------------------------------------------------")

def title():
    clear()
    os.system("figlet NetMouse")
    longl()
