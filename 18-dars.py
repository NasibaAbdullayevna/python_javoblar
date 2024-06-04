"""
python 18-dars "WHILE, RO'YXATLAR VA LUG'ATLAR"
Nasiba Abdulloyevna
04.06.2024
"""

"""savol1="Buyurtma qilmoqchi bo'lgan mahsulotingizni kiriting: "
savol2="Yana buyurtma bermoqchimisiz? (ha/yo'q)"
buyurtma=[]
while True:
    javob=input(savol1)
    buyurtma.append(javob)
    javob=input(savol2)
    if javob.lower()=="yo'q":
        break
print(f"\nSizning buyurtmangiz: {buyurtma}")"""

"""mahsulotlar={}
savol="Yana mahsulot kiritasizmi? (ha/yo'q)"
while True:
    nomi=input("Mahsulot nomini kiriting: ")
    narxi=input(f"{nomi}ning narxini kiriting: ")
    mahsulotlar[nomi]=int(narxi)
    javob=input(savol)
    if javob!='ha':
        break
print(f"\nMahsulotlar nomi va narxining ro'yxati: ")
for nomi, narxi in mahsulotlar.items():
    print(f"{nomi.title()} {narxi} so'm")"""

savol1="Buyurtma qilmoqchi bo'lgan mahsulotingizni kiriting: "
savol2="Yana buyurtma bermoqchimisiz? (ha/yo'q)"
buyurtma=['manti','non','sharbat']
s=0
print(f"\nSizning buyurtmangiz: {buyurtma}")
mahsulotlar={'manti':7000,'norin':25000,'non':5000,'sharbat':12000}
for nomi,narxi in mahsulotlar.items():
    if nomi in buyurtma:
        print(f"{nomi.title()} narxi: {narxi}")
        s+=narxi
    else:
        print(f"Bizda {nomi} yo'q")
print(f"\nBuyurtmalaringiz jami narxi: {s} so'm")
                  
    






























