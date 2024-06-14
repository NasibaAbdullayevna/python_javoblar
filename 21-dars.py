"""
python 20-dars "QIYMAT QAYTARUVCHI FUNKSIYA"
Nasiba Abdulloyevna
15.06.2024
"""

"""def bosh_harfda_chiqar(oilam):
    for azo in range(len(oilam)):
        oilam[azo]=oilam[azo].title()
    return oilam
oila=['xolida','husniya','abdullo','begmurod','anvar','kamola','akbarali','sarvar','nasiba']
print(bosh_harfda_chiqar(oila))"""

"""def bosh_harfda_chiqar(oilam):
    for azo in range(len(oilam)):
        oilam[azo]=oilam[azo].title()
    return oilam
oila=['xolida','husniya','abdullo','begmurod','anvar','kamola','akbarali','sarvar','nasiba']
family=oila[:]
print(bosh_harfda_chiqar(family))
print(oila)"""

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)



































