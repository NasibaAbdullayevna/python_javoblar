"""
python 20-dars "QIYMAT QAYTARUVCHI FUNKSIYA"
Nasiba Abdulloyevna
14.06.2024
"""

def kattasini_top(a,b,c):
    if a>=b and a>=c:
        katta=a
    elif b>=a and b>=c:
        katta=b
    else:
        katta=c
    return katta
a=int(input("1-sonni kiriting: "))
b=int(input("2-sonni kiriting: "))
c=int(input("3-sonni kiriting: "))
print(f"Orasidagi eng katta son {kattasini_top(a,b,c)}")

























