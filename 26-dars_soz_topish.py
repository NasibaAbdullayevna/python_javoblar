"""
python 26-dars "So'z topish o'yini"
Nasiba Abdulloyevna
27.06.2024
"""

import random as r
from uzwords import words

def top():
    word=r.choice(words)
    while '-' in word or ' ' in word:
        word=r.choice(words)
    return word.upper()

def bor(kiritildi,word):
    javob=""
    for h in word:
        if h in kiritildi:
            javob+=h
        else:
            javob+='-'
    return javob
def oyin():
    word=top()
    harflar=set(word)
    kiritilganlar=''
    print(f"Мен {len(word)} хонали сон ўйладим. Топа оласизми?\n{kiritilganlar}")
    print(word)
    while len(harflar)>0:
        print(bor(kiritilganlar,word))
        if len(kiritilganlar)>0:
            print(f"Шу пайтгача киритган харфларингиз {kiritilganlar}")
        kiritildi=input("Харф киритинг: ").upper()
        if kiritildi in kiritilganlar:
            print("Сиз аввал бу харфни киритгансиз. Бошка харф киритинг: ")
            continue
        elif kiritildi in word:
            harflar.remove(kiritildi)
            print(f"{kiritildi} харфи тугри.")
        else:
            print("Бундай харф йук.")
        kiritilganlar+=kiritildi
    print(f"абриклайман! {word} сузини {len(kiritilganlar)} та уринишда топдингиз.")
    










































