"""
python 37-dars "Klassni tekshirish" 
Nasiba Abdulloyevna
31.07.2024
"""
from datetime import datetime
class Shaxs:
        """Shaxslar haqida ma'lumot"""
        def __init__(self,ism,familiya,passport,tyil):
                self.ism = ism
                self.familiya = familiya
                self.passport = passport
                self.tyil = tyil
                
        def get_info(self):
                """Shaxs haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"Passport: {self.passport}, {self.tyil}-yilda tug`ilgan"
                return info
        def get_age(self):
                """Shaxsning yoshini qaytaruvchi metod"""
                yil=datetime.now().year
                return yil - self.tyil      
        
#talaba1=Shaxs('Nasiba','Muxtorova','NM0770077',1989)
#print(talaba1.get_info())
#print(talaba1.get_age(2024))

class Talaba(Shaxs):
        """Talaba klassi"""
        def __init__(self,ism,familiya,passport,tyil,idraqam):
                """Talabaning xususiyatlari"""
                super().__init__(ism, familiya, passport, tyil)
                self.idraqam = idraqam
                self.bosqich = 1
                
        def get_id(self):
                """Talabaning ID raqami"""
                return self.idraqam

        def get_bosqich(self):
                """Talabaning o'qish bosqichi"""
                return self.bosqich

        def get_info(self):
                """Talaba haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
                return info



"""

talaba2=Talaba('Anvar','Toshev','AT0770077',1988,'N0000007')
print(talaba2.get_info())

"""
                
































