"""
python 30-dars "Vorislik va polimorfizm" 
Nasiba Abdulloyevna
4.07.2024
"""

class Shaxs:
        """Shaxslar haqida ma'lumot"""
        def __init__(self,ism,familiya,passport,tyil):
                self.ism = ism
                self.familiya = familiya
                self.passport = passport
                self.tyil = tyil
                self.fanlar=[]
        def get_info(self):
                """Shaxs haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
                return info
        def get_age(self,yil):
                """Shaxsning yoshini qaytaruvchi metod"""
                return yil - self.tyil      
        
talaba1=Shaxs('Nasiba','Muxtorova','NM0770077',1989)
#print(talaba1.get_info())
#print(talaba1.get_age(2024))

class Fan:
        def __init__(self,nomi):
                self.nomi = nomi
               
class Talaba(Shaxs):
        """Talaba klassi"""
        def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
                """Talabaning xususiyatlari"""
                super().__init__(ism, familiya, passport, tyil)
                self.idraqam = idraqam
                self.bosqich = 1
                self.manzil=manzil
                self.fanlar=[]

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
                 
class Manzil:
        """Manzil saqlash uchun klass"""
        def __init__(self, uy, kocha, tuman, viloyat):
                """Manzil xususiyatlari"""
                self.uy = uy
                self.kocha = kocha
                self.tuman = tuman
                self.viloyat = viloyat

        def get_manzil(self):
                """Manzilni ko'rish"""
                manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
                manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
                return manzil

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, pasport, tyil, email):
        super().__init__(ism, familiya, pasport, tyil)
        self.email = email
    def get_info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Email: {self.email}, Fanlar: {self.fanlar}"

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, pasport, tyil, email):
        super().__init__(ism, familiya, pasport, tyil, email)
    def ban_user(self, user):
        print(f"{user.ism} {user.familiya} bloklandi.")


talaba2_manzil=Manzil(77,'Hazortut','Romitan','Buxoro')
talaba2=Talaba('Anvar','Toshev','AT0770077',1988,'N0000007',talaba2_manzil)

matematika = Fan("Oliy Matematika")
informatika = Fan("Dasturlash asoslari")
xorijiy_til = Fan("Ingliz tili")

talaba2.fanga_yozil(matematika)
talaba2.fanga_yozil(xorijiy_til)

print(talaba2.get_info())

print(talaba2.manzil.get_manzil())

print(talaba2.manzil.tuman)
talaba2.remove_fan(matematika)
print(talaba2.get_info())

foydalanuvchi1 = Foydalanuvchi("Nasiba", "Muxtorova", "AA3101434", 1989, "akan@gmail.com")
admin1 = Admin("Kamola", "Anvarovna", "AD0707121", 2012, "kamolaxon@gmail.com")

print(foydalanuvchi1.get_info())
admin1.ban_user(foydalanuvchi1)
                
































