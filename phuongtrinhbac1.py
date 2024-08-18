# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:38:00 2024

@author: nguyenthuythaovy
"""

a=float(input("Nhập a:"))

b=float(input("Nhập b:"))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Nghiệm của phương trình là:",x)