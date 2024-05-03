"""
python 5-dars "String, Input"
Nasiba Abdulloyevna
20.04.2024
"""
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
#kocha=input("ko'changiz nomi?  ")
#mahalla=input("mahallangiz nomi?  ")
#tuman=input("tuman nomi?  ")
#viloyat=input("viloyat nomi?  ")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
print(f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")
manzil=f"{kocha} {mahalla} {tuman} {viloyat}"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
print(kocha+ " ko'chasi, "+mahalla+" mahallasi, "+
      tuman+" tumani, "+viloyat+" viloyati")
