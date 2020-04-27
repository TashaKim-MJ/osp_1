#!/usr/bin/python
from my_pkg.binaryCal import *
from my_pkg.setCal import *

if __name__== '__main__':

    while True:
        num = int(input("Select menu: 1) conversion 2) union/intersection 3) exit? "))

        if num == 1:
            bincal()
        elif num == 2:
            setcal()
        elif num == 3:
            print("exit the program...")
            exit()
        else:
            print("WRONG")


