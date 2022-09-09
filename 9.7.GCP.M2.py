# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:40:29 2022

@author: jingy
"""

print('Enter quadratic coefficients')
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = (b**2) - (4*a*c)
if d>0:
    print(f'2 real solutions')
elif d<0:
        print(f'2 complex solutions')
else:
    print(f'1 real solution')

year = int(input('Enter year: '))
year100 = year%100
year400 = year%400
year4 = year%4
if year100 and year400 == 0:
    print(f'{year} is a leap year.')
elif year100==0 and year400>0:
    print(f'{year} is not a leap year.')
elif year100>0 and year4==0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')
    
    
    
    
    