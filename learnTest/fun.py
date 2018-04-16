#!/usr/bin/python3
import sys

def printMax(a,b):
    '''比较最大值'''
    max = a;
    if(a<b):
        max=b;
    print(max);
printMax(4,6);
print(printMax.__doc__);

def area(*args):
    end = 1;
    for i in args:
        end *= i;
    print(end);
    print(args);
#Print(sys.argv());pip
area(5,2,3,6,7,8,9);