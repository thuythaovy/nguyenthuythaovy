# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:48:36 2024

@author: nguyenthuythaovy
"""
import math
a=float(input("Nhập a:"))

b=float(input("Nhập b:"))

c=float(input("Nhập c:"))
delta=b**2-(4*a*c)
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép x1=x2=",-(b/(2*a)))
else:
    print("Phương trình có hai nghiệm phân biệt:")
    x1= (-(b) + (math.sqrt(delta)))/(2*a)
    x2= (-(b) - (math.sqrt(delta)))/(2*a)
    print("x1=", x1)
    print("x2=", x2)
          