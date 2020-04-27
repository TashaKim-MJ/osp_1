#!/usr/bin/python
import re

def setcal():
    
    temp1 = input("1st list: ")
    temp2 = input("2nd list: ")

    temp1 = re.sub('[,\[\] ]', '', temp1)
    temp2 = re.sub('[,\[\] ]', '', temp2)

    list1 = list(temp1)
    list2 = list(temp2)
    union = list(set(list1) | set(list2))
    uni = sorted(list(map(int, union)))
    intersection = list(set(list1) & set(list2))
    ins = sorted(list(map(int, intersection)))
    print ("union " , uni)
    print ("intersection " , ins)

