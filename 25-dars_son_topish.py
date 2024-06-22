"""
python 22-dars "*args va **kwargs (O'ZGARUVCHAN FUNKSIYA"
Nasiba Abdulloyevna
15.06.2024
"""

import random as r
print("Keling, o'ylagan sonni topish o'ynaymiz!")
def son_top_f(x):
    k_son=r.randint(1,x)
    f=0
    while True:
        javob=int(input(f"1 dan {x} gacha oraliqda son o'yladim topa olasizmi?: "))
        f+=1
        if javob==k_son:
            print(f"Topdingiz! {k_son} ni o'ylagan edim. {f} ta taxmin bilan topdingiz, tabriklayman.")
            break
        elif javob<k_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana urinib ko'ring: ")
        else:
            print("Xato, men o'ylagan son bundan kichikroq. Yana urinib ko'ring: ")
    return f

def son_top_k(n):
    print(f"1 dan {n} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing")
    start=1
    stop=10
    k=0
    while True:
        f_son=r.randint(start,stop)
        k+=1
        print(f"Siz {f_son} sonini o'yladingiz: to'g'ri (t), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)? ")
        a=input()
        if a=='t':
            print(f"O'ylagan soningizni {k} ta taxmin bilan topdim")
            break
        elif a=='+':
            start=f_son+1
        elif a=='-':
            stop=f_son-1
    return k

foydalanuvchi=son_top_f(10)
kompyuter=son_top_k(10)
if foydalanuvchi<kompyuter:
    print(f"Siz {foydalanuvchi} ta taxmin bilan topdingiz, men {kompyuter} ta taxmin bilan topdim. Siz yutdingiz!")
elif foydalanuvchi>kompyuter:
    print(f"Siz {foydalanuvchi} ta taxmin bilan topdingiz, men {kompyuter} ta taxmin bilan topdim. Men yutdim!")
else:
    print(f"Siz {foydalanuvchi} ta taxmin bilan topdingiz, men ham {kompyuter} ta taxmin bilan topdim. Durrang!")
            
            
     
    

    































