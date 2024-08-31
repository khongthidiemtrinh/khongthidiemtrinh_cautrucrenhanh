# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:36:25 2024

@author: diemtrinh
"""
a = int(input("Nhập một số nguyên: "))
b = ["Khong doc duoc", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
if 0 <= a <= 9:
    print(b[a])
else:
    print("Khong doc duoc")
