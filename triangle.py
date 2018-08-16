# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:46:53 2018

@author: Lisa Nurfauziyya
"""

def triangle(n):
    n = n.replace(".", "")
    x = []
    for i in zip(reversed(n), range(len(n))):
        x = [i[0]+"0"*i[1]] + x

    for i in range(len(x)):
        print x[i]
        
def main():
    print "Reserved Triangle"
    input = raw_input("Enter input number : ")
    triangle(input)
main()