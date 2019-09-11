# coding=utf-8
# Caner Aydin - Importing Temp Data from Mac Pro to JSON File, appended with random data

import requests
import json
import random

f = open("macpro_temp.json", "w")


api_data = requests.get('http://192.168.2.202:4027/api/sensors')

# print(api_data.text)

y = json.loads(api_data.text)  # type: object

# datayı load edip list olarak kaydetmis mi test etmek icin kullandim
# z = y["PCH Die"]
# print(z)

# surekli degisen bi dataya sahip olmak icin random nr generator ekledim
rastgele = random.randint(1,9999)
# print(rastgele) # test

y ["rastgele"]= rastgele

l = json.dumps(y)

f.write(l)

f.close()