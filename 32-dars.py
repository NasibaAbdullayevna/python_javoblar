"""
python 32-dars "DUNDER METODLAR" 
Nasiba Abdulloyevna
18.07.2024
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
        def __repr__(self):
                return f"{self.ism} shaxsi"
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

        def __repr__(self):
                return f"{self.ism} ismli talaba"

        def get_id(self):
                """Talabaning ID raqami"""
                return self.idraqam

        def get_bosqich(self):
                """Talabaning o'qish bosqichi"""
                return self.bosqich

        def add_bosqich(self):
                self.bosqich+=1
                return self.bosqich

        def __lt__(self,boshqa_talaba):
                if isinstance(boshqa_talaba,Talaba):
                        return self.bosqich<boshqa_talaba.bosqich

        def __eq__(self,boshqa_talaba):
                if isinstance(boshqa_talaba,Talaba):
                        return self.bosqich==boshqa_talaba.bosqich

        def get_info(self):
                """Talaba haqida ma'lumot"""
                info = f"{self.ism} {self.familiya}. "
                info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}, yozilgan fanlar: {self.fanlar}"
                return info

        @classmethod
        def get_num_student(cls):
                return cls.__talabalar_soni

class Fan:
        def __init__(self,fan_nomi):
                self.fan_nomi=fan_nomi
                self.talabalar=[]

        def __repr__(self):
                return f"{self.fan_nomi} fani"

        def add_student(self,*student):
                for talaba in student:
                        if isinstance(talaba,Talaba):
                                self.talabalar.append(talaba)
                        else:
                                print("Bu talaba Talabalar ro'yxatida mavjud emas")
                        
        def __getitem__(self,index):
                return self.talabalar[index]
        
        def __setitem__(self,index,boshqa_student):
                self.talabalar[index]=boshqa_student
                
        def __len__(self):
                return len(self.talabalar)

        def __add__(self,yangi):
                if isinstance(yangi,Talaba):
                        self.add_student(yangi)
                        return self
                elif isinstance(yangi,Fan):
                        yangi_fan=Fan(f"{self.fan_nomi} {yangi.fan_nomi}")
                        return yangi_fan
                else:
                        print(f"{type(yangi)} ni qo'shib bo'lmaydi")

        def __sub__(self,eski):
                if isinstance(eski,Talaba):
                        self.talabalar.remove(eski)
                        return self
                elif isinstance(eski,Fan):
                        return f"{eski} {self.fan_nomi} fanida mavjud emas"
                else:
                        print(f"{type(eski)} ni olib tashlab bo'lmaydi")
                        return self

        def __call__(self,*parametr):
                if parametr:
                        for talaba in parametr:
                                self.add_student(talaba)
                else:
                        return [talaba for talaba in self.talabalar]                     
        

shaxs1=Shaxs('Nasiba','Muxtorova','NM0770077',1989)
shaxs2=Shaxs('Anvar','Toshev','AD2707707',1988)
talaba1=Talaba('Kamola','Begmurodova','KB0707777',2012,'AA0000007','Buxoro')
talaba2=Talaba('Akbarali','Begmurodov','AB0704155',2015,'AA0000004','Romitan')
talaba3=Talaba('Sarvar','Begmurodov','SB0204222',2022,'AA0000002','Buxoro')

#print(talaba1.get_bosqich())
#print(talaba2.get_bosqich())

talaba2.add_bosqich()

#print(talaba2.get_bosqich())
#print(shaxs1)
#print(talaba1<talaba2)
#print(talaba1==talaba3)

matematika=Fan("Matematika")
informatika=Fan("Dasturlash")
xorijiy_til=Fan("Ingliz tili")

matematika.add_student(talaba1)
informatika.add_student(talaba1)
matematika.add_student(talaba2)
xorijiy_til.add_student(talaba3)
xorijiy_til.add_student(talaba3)
#print(matematika)
#print(matematika[:])

talaba4=Talaba('Abdullo','Muxtorov','AM0708588',1958,'AA0000008','Losha')
matematika=matematika+talaba4
print(matematika[:])
matematika=matematika-talaba1
print(matematika[:])
































