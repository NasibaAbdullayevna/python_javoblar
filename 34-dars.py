"""
python 34-dars "JSON" 
Nasiba Abdulloyevna
25.07.2024
"""

import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json=json.dumps(data)
print(data_json)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")

with open("car_info.json",'w') as file:
        json.dump(data,file)

with open("student.json",'w') as file:
        json.dump(talaba,file)

with open ("students.json") as file:
        talabalar=json.load(file)

for n in talabalar['student']:
        print(f"{n['name']} {n['lastname']}, {n['year']}-kurs, {n['faculty']} talabasi")

with open('api-result.json') as file:
        sahifa=json.load(file)

title=sahifa['query']['pages']['13801']['title']
extract=sahifa['query']['pages']['13801']['extract']
print(f"title: {title} \nextract: {extract}")































