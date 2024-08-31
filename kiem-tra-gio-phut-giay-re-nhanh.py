# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:16:07 2024

@author: diemtrinh
"""
print(" KIỂM TRA GIỜ PHÚT GIÂY")
a= int(input("Nhập số giờ: "))
b= int(input("Nhập số phút: "))
c= int(input("Nhập só giây: "))
if 0 <=a<= 23 and 0 <=b<= 59 and 0 <=c<= 59:
    print("Giờ, phút, giây hợp lệ.")
    print(f"{a}giờ {b}phút {c}giây")
else:
    print("Không hợp lệ.")

