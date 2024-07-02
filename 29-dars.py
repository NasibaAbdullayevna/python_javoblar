"""
python 29-dars "Obyektlar bilan ishlash" 
Nasiba Abdulloyevna
2.07.2024
"""

class Avto:
        def __init__(self,model,rang,yil,korobka,narx):
                self.model=model
                self.rang=rang
                self.yil=yil
                self.korobka=korobka
                self.narx=narx
                self.kilometr=0
                
        def get_info(self):
                return f"Avtomobil:\n{self.rang.title()} {self.model}, {self.yil}-yil, {self.korobka} korobka, {self.narx} $, kilometri {self.kilometr}"

        def set_km(self,kilometr):
                self.kilometr=kilometr
                return self.kilometr
                
        def update_km(self,son):
                self.kilometr+=son
                return self.kilometr

class Avtosalon():
        def __init__(self):
                self.nomi="Sitora"
                self.manzili="Buxoro sh."
                self.avtolar_soni=0
                self.sotuvdagi_avtolar=[]

        def add_avto(self,avto):
                self.sotuvdagi_avtolar.append(avto)
                self.avtolar_soni+=1

        def get_avto(self):
                return [avto.get_info() for avto in self.sotuvdagi_avtolar]

avto1=Avto('Lasetti','oq',2022,'avtomat',15000)
avto2=Avto('Malibu','qora',2020,'avtomat',35000)
avto3=Avto('Spark','kulrang',2021,'mexanika',8000)

avtosalon=Avtosalon()
avtosalon.add_avto(avto1)
avtosalon.add_avto(avto2)
avtosalon.add_avto(avto3)

print(avto1.get_info())
print(avto2.set_km(50000))
print(avto3.update_km(10000))

for avto in avtosalon.get_avto():
        print(avto)





 




































