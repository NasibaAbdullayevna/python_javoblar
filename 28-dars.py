"""
python 28-dars "Class and Object" 
Nasiba Abdulloyevna
2.07.2024
"""

class user:
        def __init__(self,name,surename,nickname,email,bornyear,phonenumber):
                self.name=name
                self.surename=surename
                self.nickname=nickname
                self.email=email
                self.bornyear=bornyear
                self.phonenumber=phonenumber
                
        def get_age(self,yil):
                return yil-self.bornyear
        
        def get_email(self):
                return self.email
        
        def get_info(self):
                return f"Foydalanuvchi: {self.nickname}, ismi: {self.name} {self.surename}, email: {self.email}"

user1=user('Nasiba','Muxtorova','akan','nasiba@gmail.com',1989,993334433)
user2=user('Anvar','Toshev','anvar2707','anvar2707@gmil.com',1988,977770077)
user3=user('Kamola','Begmurodova','kamolaxon','kamolaxon07@gmail.con',2012,997770707)

#print(user1.nickname)






































