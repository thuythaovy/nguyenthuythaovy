# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:24:07 2024

@author: nguyenthuythaovy
"""

a=float(input("Nhap so km quang duong:"))
               
if a <= 1:
    x = 20
    print("Thanh toan:",x)
elif a > 1 and a <=3:
    x = a * 13
    print("Thanh toan:",x)
elif a > 3 and a <= 8:
    x = 39 + ( a - 3 ) * 12
    print("Thanh toan:",x)
else:
    x = a * 10
    if x > 100:
        x = ( a * 10 ) - ( a * 10 ) * ( 8 / 100 )
        print ("Tien taxi la:",x)
        