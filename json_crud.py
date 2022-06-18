
import json
x='''{"students":[
    {"name":"John", "age":"23", "city":"Agra"},
    {"name":"Steve", "age":"28", "city":"Delhi"},
    {"name":"Peter", "age":"32", "city":"Chennai"},
    {"name":"Chaitanya", "age":"28", "city":"Bangalore"}
]}'''

y=json.loads(x)

stu_lst=y["students"]

student_det={}
count=1
while count<4:
        key=input()
        value=input()
        student_det[key]=value
        count+=1
stu_lst.append(student_det)
        
print(stu_lst)