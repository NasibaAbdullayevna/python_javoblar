"""
python 33-dars "FAYLLAR BILAN ISHLASH. PICKLE" 
Nasiba Abdulloyevna
24.07.2024
"""

import pickle
with open("learn.txt") as file:
        matn=file.read()

#print(matn)

with open("pi_million_digits.txt") as fayl:
        pi=fayl.read()

pi=pi.rstrip()
pi=pi.replace('\n','')
pi=pi.replace(' ','')
tkunim='31011989'
        
#print(pi)
print(tkunim in pi)

pi=float(pi)
with open('pi_son.pkl','wb') as file:
        pickle.dump(pi,file)

while True:
        sevimli_taomlar=input("Sevimli taomingizni kiriting: ")
        with open('sevimli_taomlar.txt','a') as file:
                file.write(sevimli_taomlar+'\n')
        javob=input('Yana ovqat nomini kiritasizmi? (y/n)')
        if javob=='n':
                break




















