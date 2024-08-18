# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:30:18 2024

@author: nguyenthuythaovy
"""


a=float(input("Nhập a:"))

b=float(input("Nhập b:"))

c=float(input("Nhập c:"))

if a+b>c and b+c>a and a+c>b:
    print("Đây là một tam giác")
    if a==b==c:
        print("Đây là tam giác đều")
    elif a==b or b==c or a==c:
        print("Đây là tam giác cân")
        if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("Đây là tam giác vuông cân")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là một tam giác")
    