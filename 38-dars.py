"""
python 38-dars "PYTHON KUTUBXONALARI" 
Nasiba Abdulloyevna
1.08.2024
"""

import datetime as dt
from pprint import pprint
import re

"""Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqarish"""

bugun=dt.date.today()
#print(bugun)

for sana in range(0,100,10):
        print(bugun+dt.timedelta(days=sana))

"""Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqarish"""

ramazon=dt.date(2025,3,1)-bugun
qurbon_hayiti=dt.date(2025,6,6)-bugun
print(f"Ramazongacha {ramazon.days} kun qoldi,\n"
      f"Qurbon hayitigacha {qurbon_hayiti.days} kun qoldi.")

"""Tug'ilgan kunimdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya"""

def farq(tsana):
        hozir=dt.date.today()
        yillar=hozir.year-tsana.year
        oylar=hozir.month-tsana.month
        kunlar=hozir.day-tsana.day

        if kunlar<0:
                oylar-=1
                if hozir.month>1:
                        oldingi_oy=hozir.month-1
                else:
                        oldingi_oy=-12


                if hozir.month>1:
                        oldingi_yil_oyi=hozir.year
                else:
                        oldingi_yil_oyi=hozir.year-1
                kunlar+=(hozir-dt.date(oldingi_yil_oyi,oldingi_oy,1)).days

        if oylar<0:
                yillar-=1
                oylar+=12

        return yillar, oylar, kunlar

tsana=dt.date(1989,1,31)
print(farq(tsana))

"""Foydalanuvchidan telefon raqamini kiritishni so'rab, uni andoza yordamida tekshirish"""

msg='Telefon raqamingizni namunadagi kabi kiriting: '
msg+='(+919367788755 yoki 8989829304 yoki +16308520397 yoki 786-307-3615)\n'
andoza='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
while True:
        telraqam=input(msg)
        if re.match(andoza,telraqam):
                print("Telefon raqamingiz qabul qilindi")
                break
        else:
                print("Tel raqamingizni namunalardagidek kiriting:\n(+919367788755 yoki 8989829304 yoki +16308520397 yoki 786-307-3615)")

"""Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya"""

matn="Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
andoza_url='https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
url=re.findall(andoza,matn)
print(url)

















































