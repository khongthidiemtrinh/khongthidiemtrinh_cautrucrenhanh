# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:09:03 2024

@author: diemtrinh
"""
print(" TÍNH CHU VI DIEN TÍCH CÁC HÌNH ")
a=input("Nhập hình bạn muốn tính(1= hình vuông, 2=hình chữ nhật, 3= hình tròn):  ")
if a == '1':
    canh= float(input("Nhập cạnh hình vuong= "))
    chuvihvuong= canh*canh
    dientichhvuong=canh**4
    print(" Chu vi hình vuông= ", chuvihvuong)
    print(" Diện tích hình vuông= ", dientichhvuong)
elif a == '2':
    dai= float(input("Nhập chiều dài hình chữ nhật= "))
    rong= float(input("Nhập chiều rộng hình chữ nhật= ")) 
    chuvihcn= (dai+rong)*2
    print(" Chu vi hình chữ nhật= ",chuvihcn)
    dientichhcn= dai*rong
    print(" Diện tích hình chữ nhật= ", dientichhcn)
elif a == '3':
    r= float(input(" Nhập bán kính hình tròn= "))
    pi= 3.14       
    chuvihtron= pi*r**2
    print(" Chu vi hình tròn= ", chuvihtron)
    dientichhtron= 2*pi*r
    print(" Diện tích hình tròn= ", dientichhtron)
else:
    print("Không thể thực hiện! Vui lòng chỉ nhập 1 2 hoặc 3!!")



    
    
    
