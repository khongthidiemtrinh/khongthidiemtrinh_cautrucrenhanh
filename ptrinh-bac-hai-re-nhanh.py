# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:50:25 2024

@author: diemtrinh
"""
print("Giải và biện luận phương trình bậc hai")
import math 
print(" Giải và biện luận phương trình bậc hai")
a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
c=float(input("Nhập hệ số c: "))
if a==0: print ("Phương trình không phải phương trình bậc 2")
delta = b**2 - 4*a*c
if delta > 0:
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2= (-b - math.sqrt(delta)) / (2 * a)
    print("Phương trình có hai nghiệm phân biệt: x1 =",x1 ,"và x2=",x2)
elif delta== 0:
    x= -b / (2 * a)
    print("Phương trình có một nghiệm kép: ",x)
else:
    print("Phương trình vô nghiệm")