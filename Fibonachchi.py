"""
python 36-dars "FUNKSIYANI TEKSHIRISH" 
Nasiba Abdulloyevna
28.07.2024
"""

def fibonachchi(sonlar):
        javob=True
        for i in range(0,len(sonlar)-2):
                if sonlar[i]+sonlar[i+1]!=sonlar[i+2]:
                        javob=False
                        break
                else:
                        javob=True
        return javob

"""
sonlar=(1,1,2,3,5,8,13,21,34,55)
fibonachchi(sonlar)
True
sonlar=(1,2,3,4,5,6,7)
fibonachchi(sonlar)
False
"""

































