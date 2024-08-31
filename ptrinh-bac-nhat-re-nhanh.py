# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:05:13 2024

@author: diemtrinh
"""
print("Giải và biện luận phương trình bậc nhất")
a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
if a!= 0:
    x=-b / a
    print("Phương trình có một nghiệm duy nhất: ",x )
else:   
    if b==0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
