# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:14:13 2024

@author: nguyenthuythaovy
"""

from random import randint
print("Hay chon Keo hoac Bua hoac Bao:")
player = input ()
computer = randint(0,2)

if computer==0:
    computer="Keo"
if computer==1:
    computer="Bua"
if computer==2:
    computer="Bao"
print("Ban chon:",player)
print("May chon:",computer)

if computer==player:
    print("Hoa")
elif computer != player:
    if player=="Bao":
        if computer=="Bua":
            print("Thang")
        else:
            print("Thua")
    elif player=="Keo":
        if computer=="Bao":
            print("Thang")
        else:
            print("Thua")
else:
    print("Nhap sai!")
    