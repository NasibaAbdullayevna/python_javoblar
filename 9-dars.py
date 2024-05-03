"""
python 9-dars "For loop"
Nasiba Abdulloyevna
27.04.2024
"""
#oilam=['Onam','Otam','Qaynonam','Qaynotam','Turmush o\'rtog\'im','Kamola','Akbarali','Sarvar']
#s=0
#for azo in oilam:
#    print(f"Men {azo}ni yaxshi ko\'raman")
#    s+=1
#print(f"Kod {s} marta takrorlandi")
#sonlar=list(range(11,100,2))
#for son in sonlar:
#    print(son**3)
#kinolar=[]
#print('5 t eng sevimli kinolaringizni kiriting')
#for kino in range(5):
#    kinolar.append(input(f"{kino+1}-sevimli filmingiz: "))
#print(kinolar)
suhbatdoshlar=[]
n=int(input("Bugun necha kishi bilan suhbatlashdingiz?>>>"))
for i in range(n):
    suhbatdoshlar.append(input(f"{i+1}-suhbatdoshingiz: "))
print(suhbatdoshlar)
