"""
python 16-dars "NESTING"
Nasiba Abdulloyevna
01.06.2024
"""

"""shaxs1={'ism':'Abu Abdulloh Muhammad ibn Ismoil','tyili':810,\
        'tshahri':'Buxoro','yashagan':60,\
        'asarlar':["Al-jome' as-sahih","Al-adab al-mufrad"]}
shaxs2={'ism':'Abdulla Qodiriy','tyili':1894,
        'tshahri':'Toshkent','yashagan':44,\
        'asarlar':["O'tkan kunlar", 'Mehrobdan chayon']}
shaxs3={'ism':'Erkin Vohidov','tyili':1936,\
        'tshahri':'Farg\'ona','yashagan':80,\
        'asarlar':['Tong nafasi',"O'zbegim"]}
shaxs4={'ism':'Alisher Navoiy','tyili':1441,\
        'tshahri':'Hirot','yashagan':60,\
        'asarlar':['Xamsa','Lison ut-Tayr']}
mashhurlar=[shaxs1,shaxs2,shaxs3,shaxs4]"""

"""for malumot in mashhurlar:
    print(f"{malumot['ism']} {malumot['tyili']}-yilda "
          f"{malumot['tshahri']}da tavallud topgan. "
          f"{malumot['yashagan']} yil umr ko\'rgan")"""

"""for shaxs in mashhurlar:
    print(f"{shaxs['ism']}")
    for asar in shaxs['asarlar']:
        print(asar)
    print('\n')"""

"""oilam={
    'xolida':["Umr ko'chalari","Qodirxon","Otalar so'zi"],
    'abdullo':['Terminator','Abdullajon','Rembo'],
    'anvar':['Boks','Futbol','Jangari'],
    'kamola':['Artist','Ovoz','Musiqa']
    }
for ism, kino in oilam.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in oilam:
        print(kino)"""

davlatlar={
    "o'zbekiston":{'poytaxti':'toshkent','hududi':'448978 kv.km',\
                   'aholisi':33000000,'pul birligi':"so'm"},
    'rossiya':{'poytaxti':'moskva','hududi':'17098246 kv.km',\
                   'aholisi':144000000,'pul birligi':"rubl"},
    'aqsh':{'poytaxti':'washington','hududi':'9631418 kv.km',\
                   'aholisi':327000000,'pul birligi':"dollar"},\
    'malayziya':{'poytaxti':'kuala-lumpur','hududi':'329750 kv.km',\
                   'aholisi':25000000,'pul birligi':"rinngit"}}
"""for davlat, malumot in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat=davlat.upper()
    else:
        davlat=davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {malumot['poytaxti'].title()}"
          f"\nHududi: {malumot['hududi']}"
          f"\nAholisi: {malumot['aholisi']}"
          f"\nPul birligi: {malumot['pul birligi']}")"""

davlat=input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    malumot=davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {malumot['poytaxti'].title()}"
          f"\nHududi: {malumot['hududi']}"
          f"\nAholisi: {malumot['aholisi']}"
          f"\nPul birligi: {malumot['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")





























