import random
import re
import operator
import string

data = {}

i=130000
while i > 0:
    data[len(data)] = {
        'start':(random.gauss(100, 10)),
        'end':(random.gauss(100, 10)),
        'random':round(random.gauss(1000, 1000)),
        'rnd':''.join(random.choice(string.ascii_lowercase) for i in range(7))
    }
    i-=1

#print (data)

#for key, value in data.items(): print(key, value)

#Стоит делать так!
for key in data:
    data[key]['start'] = int(data[key]['start'])
    data[key]['end'] = int(data[key]['end'])


#Работает!
for key in tuple(data):
    if data[key]['start'] < 100 or data[key]['end'] < 100 :
        del data[key]

#TODO multidimensional sort!
data = {k: v for k,v in sorted(data.items(), reverse=False, key=lambda item: item[1].get('rnd', 0)) } #Работает!!!

i=0
for key in data:
    i+=1
    print(key, data[key])
    if i>100:
        break

#print(data.keys())
#print(str(data).replace("}, ", "}, \n"))

