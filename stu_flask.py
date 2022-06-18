import json

x=open('emp_crud.json')
data=json.load(x)
print(data["students"])