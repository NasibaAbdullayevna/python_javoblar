"""
python 17-dars "WHILE SIKLI"
Nasiba Abdulloyevna
02.06.2024
"""

"""savol='Sevimli kitobingizni kiriting'
savol+="\n(dasturni to'xtatish uchun 'stop' so'zini kiriting): "
while True:
    kitob=input(savol)
    if kitob=='stop':
        break
print('Dastur to\'xtatildi')"""

"""savol='Yoshingiz nechchida? '
savol+="\n(dasturni to'xtatish uchun 'exit' yoki 'quit' so'zini yozing): "
ishora=True
while ishora:
    yosh=input(savol)
    if str(yosh)=='exit' or str(yosh)=='quit':
        ishora=False
    elif int(yosh)==7:
        print("Sizga muzeyga kirish 2000 so'm")
    elif int(yosh)>7 and int(yosh)<18:
        print("Sizga muzeyga kirish 3000 so'm")
    elif int(yosh)>=18 and int(yosh)<=65:
        print("Sizga muzeyga kirish 10000 so'm")
    elif int(yosh)<=6 or int(yosh)>=66:
        print("Sizga muzeyga kirish bepul")
print('Dastur to\'xtatildi')"""

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.title()=='Exit':
        break
    elif float(qiymat)<0:
        continue 
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")



































