import json
from pprint import pprint
from re import I

x='''{"students":[
        {"id":1,"name":"John", "age":"23", "city":"Agra"},
        {"id":2,"name":"Steve", "age":"28", "city":"Delhi"},
        {"id":3,"name":"Peter", "age":"32", "city":"Chennai"},
        {"id":4,"name":"Chaitanya", "age":"28", "city":"Bangalore"}
    ]}'''

student_obj=json.loads(x)
cur_student_lst=student_obj["students"]

def max_id():
    max=0
    for i in cur_student_lst:
        if i["id"]>max:
            max=i["id"]
    return max+1 

def Create():
    try:
        name=input("\tenter name : ")
        age=input("\tEnter age : ")
        city=input("\tEnter city :")
        new_student={"id":max_id(),"name":name,"age":age,"city":city}
        print("\n New Record Given below :")
        pprint(new_student)

        cur_student_lst.append(new_student)
    except Exception as e:
        print("Some thing went wrong on student adding",str(e))
def Read():
    try:
        print("\nEnter uniq ID to find student details :")
        uniq_id=int(input())
        for i in cur_student_lst:
            if i["id"]==uniq_id:
                print(i)
    except Exception as e:
        print("Some thing went wrong on read student details",str(e))
def update():
    try:
        print("Enter ID to update :")
        update_id=int(input())
        print("""What field u need to change.
                    1.name
                    2.age
                    3,city
                """)
        field=int(input())
        for i in cur_student_lst:
            if update_id==i["id"]:
                print("selected student details given below:\n",i)
                if field==1:
                    new_name=input("Enter the new name :")
                    i["name"]=new_name
                elif field==2:
                    new_age=int(input("Enter new age :"))
                    i["age"]=new_age
                elif field==3:
                    new_city=input("Enter new city : ")
                    i["city"]=new_city
        print("updated student details :\n",i)

        cur_student_lst.append(i)      

    
    except Exception as e:
        print("Some thing went wrong on student details updating",str(e))
    
def delete():
    try:
        print("Which student detials u want to delete give ID :")
        removing_stu_id=int(input())
        for i in cur_student_lst:
            if i["id"]==removing_stu_id:
                cur_student_lst.remove(i)
                print("Choosen Student details succesfully dleted ")
                
    except Exception as e:
        print("Some thing went wrong on student adding",str(e))
    

not_false=True
while not_false:
    try:
        print("Welcome to student registry...\n Current student list :")
        for i in cur_student_lst:
            print(i)
        print("What do u want to do select from below option:")
        print("""
            1."create",
            2."read",
            3."update",
            4."delete",
        """)
        opt=int(input())
        if opt==1:
            Create()
        elif opt==2:
            Read()
        elif opt==3:
            update()
        elif opt==4:
            delete()
        else:
            print("Invalid option")
        

        print("\nFinal Student list")
        print(student_obj)

        
        json.dump(student_obj)
    

        ch=input("Do u want to continue y/n: ")
        if ch.lower()=="n":
            not_false=False

        
    except Exception as e:
        print("Something went wrong",str(e))