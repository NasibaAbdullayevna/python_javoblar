"""
python 20-dars "QIYMAT QAYTARUVCHI FUNKSIYA"
Nasiba Abdulloyevna
14.06.2024
"""

def fibonachchi(n):
    sonlar=[1,1]
    for i in range(2,n):
        sonlar.append(sonlar[i-1]+sonlar[i-2])
    return sonlar
a=int(input('Fibonachchi ketma-ketligidagi nechta sonni ko\'rishni istaysiz? '))
print(fibonachchi(a))






















