"""
python 20-dars "QIYMAT QAYTARUVCHI FUNKSIYA"
Nasiba Abdulloyevna
14.06.2024
"""

"""def aylanani_hisobla(radius):
    aylana={'radius':radius,
          'diametr':radius*2,
          'perimetr':round(2*radius*3.14,2),
          'yuza':radius**2*3.14}
    return aylana

r=int(input('Aylananing radiusini kiriting: '))
print(aylanani_hisobla(r))"""

def tublarni_chiqar(a,b):
    tub_sonlar=[]
    if a>1:
        for i in range(a,b+1):
            s=0
            for j in range(1,i+1):
                if i%j==0:
                    s+=1
            if s==2:
                tub_sonlar.append(i)
    return tub_sonlar
print("Oraliqni kiriting: (a boshi, b oxiri) ")
a=int(input('a= '))
b=int(input('b= '))
print(f"{a} va {b} orasidagi tub sonlar {tublarni_chiqar(a,b)}")

























