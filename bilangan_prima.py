# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:13:05 2018

@author: Lisa Nurfauziyya
"""

def prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return n, "is not prime number"
                break
        else:
            return n, "is prime number"
    else:
        return n, "is not prime number"

def main():
    print "Prime number"
    input = int(raw_input("Enter input number : "))
    print prime(input)
main()