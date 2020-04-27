#!/usr/bin/python
import re

def setcal():
    
    temp1 = input("1st list: ")
    temp2 = input("2nd list: ")
    print(type(temp1))

    temp1.replace(" ", "")
    print(temp1)
    temp2.replace(" ", "")
    temp1 = re.sub('[,\[\] ]', '', temp1)
    temp2 = re.sub('[,\[\] ]', '', temp2)

    list1 = list(temp1)
    print(list1)
    list2 = list(temp2)
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    print ("union " , union)
    print ("intersection " , intersection)

