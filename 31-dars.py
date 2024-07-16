"""
python 31-dars "INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI" 
Nasiba Abdulloyevna
16.07.2024
"""

class Shaxs:
        __odamlar_soni=0
        """Shaxslar haqida ma'lumot"""
        def __init__(self,ism,familiya,passport,tyil):
                self.ism = ism
                self.familiya = familiya
                self.__passport = passport
                self.tyil = tyil
                self.fanlar=[]
                Shaxs.__odamlar_soni+=1
        def get_passport(self):
                return self.__passport
        def get_info(self):
                """Shaxs haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"Passport:{get_passport()}, {self.tyil}-yilda tug`ilgan"
                return info
        def get_age(self,yil):
                """Shaxsning yoshini qaytaruvchi metod"""
                return yil - self.tyil

        @classmethod
        def get_num_person(cls):
                return cls.__odamlar_soni        
              
class Talaba(Shaxs):
        """Talaba klassi"""
        __talabalar_soni=0
        def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
                """Talabaning xususiyatlari"""
                super().__init__(ism, familiya, passport, tyil)
                self.idraqam = idraqam
                self.bosqich = 1
                self.manzil=manzil
                self.fanlar=[]
                Talaba.__talabalar_soni+=1

        def get_id(self):
                """Talabaning ID raqami"""
                return self.idraqam

        def get_bosqich(self):
                """Talabaning o'qish bosqichi"""
                return self.bosqich

        def get_info(self):
                """Talaba haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}, yozilgan fanlar: {self.fanlar}"
                return info

        def fanga_yozil(self,fan):
                self.fanlar.append(fan)

        def remove_fan(self,fan):
                if fan in self.fanlar:
                        self.fanlar.remove(fan)
                else:
                        return f"Siz {fan.nomi} faniga yozilmagansiz"
        @classmethod
        def get_num_student(cls):
                return cls.__talabalar_soni  

shaxs1=Shaxs('Nasiba','Muxtorova','NM0770077',1989)
#print(talaba1.get_info())
#print(talaba1.get_age(2024))
shaxs2=Shaxs('Anvar','Toshev','AD2707707',1988)
talaba1=Talaba('Kamola','Begmurodova','KB0707777',2012,'AA0000007','Buxoro')
print(Shaxs.get_num_person())
print(Talaba.get_num_student())

                 

                
































