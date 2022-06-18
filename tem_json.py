import json

x='''{"students":[
        {"id":1,"name":"John", "age":"23", "city":"Agra"},
        {"id":2,"name":"Steve", "age":"28", "city":"Delhi"},
        {"id":3,"name":"Peter", "age":"32", "city":"Chennai"},
        {"id":4,"name":"Chaitanya", "age":"28", "city":"Bangalore"}
    ]}'''

student_obj=json.loads(x)
cur_student_lst=student_obj["students"]

print(cur_student_lst)