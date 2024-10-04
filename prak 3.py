# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:06:45 2024

@author: Lenovo
"""

print("=====Selamat Datang di Segitiga Detektor=====")

# Meminta input dari user
a = int(input("Isi sisi a: "))
b = int(input("Isi sisi b: "))
c = int(input("Isi sisi c: "))

# Mengecek apakah nilai-nilai tersebut bisa membentuk segitiga
if a + b > c and a + c > b and b + c > a:
    # Mengecek jenis segitiga
    if a == b == c:
        print("Jenis segitiga: Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Jenis segitiga: Segitiga Sama Kaki")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Jenis segitiga: Segitiga Siku-Siku")
    else:
        print("Jenis segitiga: Segitiga Sembarang")
else:
    print("Jenis segitiga: Ini bukan merupakan segitiga")

print("=====Terimakasih=====")