"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""

def get_text_title(text):
        return [matn.title() for matn in text]

texts=[]
while True:
        matn=input("Matn kiriting: (Boshqa matn kiritmoqchi bo'lmasangiz enterni bosing)\n")
        if matn:
                texts.append(matn)
        else:
                break

#print(get_text_title(texts))
                
"""
Matn kiriting: (Boshqa matn kiritmoqchi bo'lmasangiz enterni bosing)
yurtimni sevaman
Matn kiriting: (Boshqa matn kiritmoqchi bo'lmasangiz enterni bosing)
maqsadimga yetaman
Matn kiriting: (Boshqa matn kiritmoqchi bo'lmasangiz enterni bosing)

['Yurtimni Sevaman', 'Maqsadimga Yetaman']
"""        






























