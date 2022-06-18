from inspect import isclass
from operator import countOf
import requests

url='https://coderbyte.com/api/challenges/json/age-counting'

js=requests.get(url)

data_lst=js.json()['data']


str_lst=data_lst.split(',')

#print(str_lst)
age_lst=[]

for i in str_lst:
    #print(i)
    if i.strip().startswith('age'):
        a=i.strip()
        num=a[4:]
        age_lst.append(num)
count=0
print(len(age_lst))
for i in age_lst:
    if int(i)>50:
        count+=1
print(count)
    




