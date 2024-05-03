"""
python 7-dars "List(ro'yxat)"
Nasiba Abdulloyevna
21.04.2024
"""
#ismlar=['Gulsun','Zulxumor','Zilola','Nargiza']
#print('Salom',ismlar[0]+',', 'bugun ko\'rishamizmi?\
#\n'+'Apa',ismlar[1],'apa',ismlar[3]+'ga tel qiling!')
#sonlar=[5,-2,4.3]
#print(f"{sonlar[0]}*({sonlar[1]})={sonlar[0]*sonlar[1]}")
#sonlar[1]=sonlar[1]+3
#sonlar[2]=int(sonlar[2]//1)
#print(sonlar)
#t_shaxslar=['G\'azzoliy','Navoiy']
#z_shaxslar=['Anvar Narzullayev','Ustozlarim']
#print(f"Men tarixiy shaxslardan {t_shaxslar[0]} bilan,\
#\nzamonaviy shaxslardan {z_shaxslar[0]} bilan\nsuhbat qilishni istardim")
friends=[]
friends.append('Gulsun')
friends.append('Yulduz')
friends.append('Madina')
friends.append('Roziya')
friends.append('Gulnoz')
print(friends)
friends.remove('Madina')
friends.remove('Roziya')
print(friends)
friends.insert(-1,'Dilovar')
friends.insert(4,'Roziya')
friends.insert(0,'Gulnoza')
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
print(mehmonlar)
