#!/usr/bin/python
import re

def setcal():
    
    temp1 = input("1st list: ")
    temp2 = input("2nd list: ")

    list1 = list(temp1)
    list2 = list(temp2)
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    print "union " , union
    print "intersection " , intersection

