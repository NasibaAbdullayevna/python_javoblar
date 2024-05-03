"""
python 11-dars "IF-ELIF-ELSE(bir nechta shartni tekshirish)"
Nasiba Abdulloyevna
28.04.2024
"""
#son=float(input('Juft son kiriting>>>'))
#if son%2==0:
#    print('Rahmat')
#else:
#    print('Bu juft son emas')
#yosh=int(input('Yoshingiz nechchida?>>> '))
#if yosh<=4 or yosh>=60:
#    narx=0
#elif yosh<=18:
#    narx=10000
#else:
#    narx=20000
#print(f"Siz uchun muzeyga chipta narxi {narx} so'm")
#a=float(input('1-sonni kiriting>>>'))
#b=float(input('2-sonni kiriting>>>'))
#if a>b:
#    print(f"{a}>{b}")
#elif a<b:
#    print(f"{a}<{b}")
#else:
#    print(f"{a}={b}")
"""mahsulotlar=['anor','uzum','apelsin','olma','nok','kivi','qulupnay','xurmo','banan','limon']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
print('Kamida 5ta mahsulot nomini kiriting')
for i in range(5):
    savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))
for meva in savat:
    if meva.lower() in mahsulotlar:
        bor_mahsulotlar.append(meva)
    else:
        mavjud_emas.append(meva)
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda mavjud emas")
    for i in mavjud_emas:
        print(i)
else:
    print("Barcha mahsulotlar bor")"""
#foydalanuvchilar=['admin','user','man','akan','kamolaxon']
#login=input('Yangi login tanlang>>>')
#if login in foydalanuvchilar:
#    print('Login band, yangi login tanlang!')
#else:
#    print(f"Xush kelibsiz, {login.title()}!")
son=int(input('Ixtiyoriy butun son kiriting>>>'))
boluvchilar=list(range(2,11))
for i in boluvchilar:
    if son%i==0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
        
