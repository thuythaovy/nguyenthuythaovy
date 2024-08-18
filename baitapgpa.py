# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:25:48 2024

@author: nguyenthuythaovy
"""

distance=float(input("Nhập điểm trung bình(GPA):"))

if distance<3.5:
    print("Học lực kém")
elif distance>=3.5 and distance<5.0:
    print("Học lực yếu")
elif distance>=5.0 and distance<7.0:
    print("Học lực trung bình")
elif distance>=7.0 and distance<8.0:
    print("Học lực khá")
elif distance>=8.0 and distance<9.0:
    print("Học lực giỏi")
elif distance>=9.0 and distance<=10.0:
    print("Học lực xuất sắc")
    6.98