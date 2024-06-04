"""
python 19-dars "FUNKSIYA"
Nasiba Abdulloyevna
04.06.2024
"""

#def t_yil_hisobla(ism,yosh):
#    """Foydalanuvchi ismi va yoshini so'rab, \
#    uning tug'ilgan yilini hisoblaydigan funksiya"""
#    print(f"{ism.title()} siz {2024-yosh}-yilda tug'ilgansiz")
#t_yil_hisobla('nasiba',35)

#def kv_kub_hisobla(son):
#    """Foydalanuvchidan son olib, uning kvadrati va \
#    kubini konsolga chiqaruvchi funksiya """
#    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")
#kv_kub_hisobla(5)

#def juft_toq_chiqar(son):
#    """Foydalanuvchidan son olib, son juft yoki \
#    toqligini konsolga chiqaruvchi funksiya"""
#    if son%2==1:
#        print(f"{son} toq son")
#    else:
#        print(f"{son} juft son")
#juft_toq_chiqar(8)

#def kattasini_top(a,b):
#    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya.\
#    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring"""
#    if a>b:
#       print(f"{a} katta")
#    elif a<b:
#        print(f"{b} katta")
#    else:
#        print('Sonlar teng')
#kattasini_top(7,7)

#def x_darajasi_y_chiqar(x,y):
#    """Foydalanuvchidan x va y sonlarini olib, x ni y darajasini\
#    konsolga chiqaruvchi funksiya"""
#    print(x**y)
#x_darajasi_y_chiqar(2,5)

#def x_darajasi_y_chiqar(x,y=2):
#    """Foydalanuvchidan x va y sonlarini olib, x ni y darajasini\
#    konsolga chiqaruvchi funksiya"""
#    print(x**y)
#x_darajasi_y_chiqar(2)

def bolinishini_hisobla(son):
    for s in range(2,son):
        if son%s==0:
            print(f"{son} {s} ga qoldiqsiz bo'linadi")
bolinishini_hisobla(70)
        

























