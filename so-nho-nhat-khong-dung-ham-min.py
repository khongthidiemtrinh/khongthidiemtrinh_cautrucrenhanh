# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:42:44 2024

@author: diemtrinh
"""
print(" IN SỐ CÓ GIÁ TRỊ NHỎ NHẤT ")
a = int(input("nhập số a :"))
b = int(input("nhập số b :"))
c = int(input("nhập số c :"))
d = int(input("nhập số d :"))
min = a
if min > b : 
    min = b
elif min > c :
    min = c
elif min > d :
    min = d
print("Giá trị nhỏ nhất là :", min)