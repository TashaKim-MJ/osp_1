#!/usr/bin/python

def bincal():
    n = input("input binary number : ")
    num = str(n)
    decnum = int(num,2)
    octnum = format(decnum, 'o')
    hexnum = format(decnum, 'X')
    print("OCT> %s" % octnum)
    print("DEC> %d" % decnum)
    print("HEX> %s" % hexnum)