# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:50:00 2024

@author: diemtrinh
"""
#a) Cho ba số a, b, c được nhập vào từ bàn phím. Hãy in ra màn hình theo thứ tự tăng dần các số (Chỉ dùng 1 biến phụ).
a= int(input("Nhập số a:  "))
b= int(input("Nhập số b:  "))
c= int(input("Nhập số c:  "))
x=0
if a>b:
    x=a
    a=b
    b=x
elif a>c:
    x=a
    a=c
    c=x
elif b>c:
    x=b
    b=c
    c=x
print(" Ba số theo thứ tự tăng dần là: ", a,b,c)
#(b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần.
N= int(input("Nhập số nguyên: "))
N= str(N)
y=sorted(N)
print("Số sau khi sắp xếp các chữ số theo thứ tự tăng dần là:", ''.join(y))