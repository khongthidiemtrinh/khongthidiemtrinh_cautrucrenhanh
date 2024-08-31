# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:25:06 2024

@author: diemtrinh
"""
print("THƯỜNG THÀNH HOA VÀ NGƯỢC LẠI")
a= input(" Nhập một chữ cái:  ")
if a.islower():
    x=a.upper()
    print(" Đổi thành chữ hoa:  ",x)
else:
    y=a.lower()
    print(" Đổi thành chữ thường:  ",y)
