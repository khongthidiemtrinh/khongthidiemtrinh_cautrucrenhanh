# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:25:23 2024

@author: diemtrinh
"""
print("TÌM GIÁ TRỊ LỚN NHẤT KHOONG DÙNG HÀM HỖ TRỢ")
a = int(input("nhập số a :"))
b = int(input("nhập số b :"))
c = int(input("nhập số c :"))
x=a
if x<b:
    x=b
elif x<c:
    x=c
print(" Giá trị lớn nhất là:  ",x)