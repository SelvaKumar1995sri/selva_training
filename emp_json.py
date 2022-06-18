import json

# with open("employee_details.json",'r') as json_emp:
#     data = json.load(json_emp)
data = json.load(open("employee_details.json",'r'))
print(data)
