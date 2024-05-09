"""
python 15-dars "Lug'at elementlari bilan ishlash"
Nasiba Abdulloyevna
08.05.2024
"""
d={'integer':'butun son','boolean':'mantiqiy tip','float':'kasrli son',\
      'string':'matnli tip','list':"ro'yxat",'tuple':"o'zgarmas ro'yxat",\
      'set':'tartiblanmagan tip','dictionary':'indekslanmagan tip',\
      'if':'shart operatori','for':'sikl'}
"""for k in sorted(d):
    print(f"{k.title()} - {d[k]}")"""

davlatlar={'aqsh':'washington','italiya':'rim','rossiya':'moskva',\
           'tojikiston':'dushanbe','germaniya':'berlin'}
"""print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())"""

"""
top=input('Qaysi davlatning poytaxtini bilishni xoxlaysiz? ').lower()
cap=davlatlar.get(top)
if cap==None:
    print('kechirasiz, bizda bunday ma\'lumot yo\'q')
else:
    print(f"{top.upper()}ning poytaxti {davlatlar[top].title()} shahri")"""

menu={'osh':30000,'six kabob':35000,"jo'ja":25000,'qovurma':20000,\
      'salat':10000,'non':5000,'norin':60000,'shashlik':75000,\
      'kompot':4000,'choy':3000}
print('3 ta taom nomini kiriting: ')
buyurtma=[]
for taom in range(3):
    buyurtma.append(input(f"{taom+1}-taom:").lower())
summa=0
for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
        summa+=menu[taom]
    else:
        print(f"Kechirasiz, bizda {taom} yo'q")
print(f"Sizdan jami: {summa} so'm")














