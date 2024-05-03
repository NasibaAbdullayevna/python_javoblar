"""
python 8-dars "Ro'yxatlar bilan ishlash"
Nasiba Abdulloyevna
23.04.2024
"""
davlatlar=['O\'zbekiston','Rossiya','Koreya','AQSH','Kanada']
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
#sonlar=list(range(120,1200,2))
#print(sonlar)
#print('....................')
#print(sum(sonlar))
#print('....................')
#print(max(sonlar)-min(sonlar))
#print('....................')
#print(len(sonlar))
#print('......boshidagi 20ta........')
#print(sonlar[:20])
#print('....................')
#print('Mani usulim o\'rtasi:')
#urtasi=sonlar[(len(sonlar)//2)-10:(len(sonlar)//2)+10]
#print(urtasi)
#print('....................')
#print('Ustozni usullari o\'rtasi:')
#print(sonlar[530:550])
#print('.......oxirgi 20ta.......')
#print(sonlar[-20:])
taomlar=['kabob','osh','manti','sho\'rbo','chuchvara']
nonushta=taomlar[:]
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.append('sharbat')
nonushta.append('tvorog')
print('Taomlar: ',taomlar)
print('Nonushta:',nonushta)
nonushta=tuple(nonushta)


