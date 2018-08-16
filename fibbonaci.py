# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:26:23 2018

@author: Lisa Nurfauziyya
"""

def fibbo(n):
    fibbo = [0, 1]
    for a in range(n):
        if a > 1:
            print fibbo[a-1] + fibbo[a-2]
            fibbo.append(fibbo[a-1]+fibbo[a-2])
        else:
            print fibbo[a]

def main():
    print "Fibbonaci"
    input = int(raw_input("Enter input number : "))
    fibbo(input)
main()