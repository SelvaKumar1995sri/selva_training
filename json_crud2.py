import json



def delete(student_list,data):
    del_name=input("Entetr name to delete : ")
    for i in student_list:
        if i["name"]==del_name:
            i.pop("name")
            i.pop("age")
            i.pop("city")
            print(del_name,"successfully deleted")
            



def update(student_list):
    field_s=input("enter the field u want to change : ")
    
    
    for i in student_list:
        if field_s=="name":
            name=input("enter which one u want to change : ")
            change_name=input("update new name : ")
            i["name"]=change_name
            break
           
        elif field_s=="age":
            age=input("enter old age : ")
            new_age=input("give new age : ")
            i["age"]=new_age
            break

        elif field_s=="city":
            city=input("enter old city : ")
            new_city=input("give new city : ")
            i["city"]=new_city
            break
        return i

    
    

def create(student_list,data):
    student_det={}
    count=1
    while count<4:
            key=input()
            value=input()
            student_det[key]=value
            count+=1
            student_list.append(student_det)
            print(type(student_list))
            data.append(student_list)
            return data




def read(student_list):
    stu_name=input("Enter name u need to find : ")
    for i in student_list:
        if i["name"]==stu_name:
            return i

     
def crud():
    x=open('emp_crud.json','r')
    data=json.load(x)
    student_list=data["students"]

   
    option=input("which one u want to do : ")
    if option=="R":
        print(read(student_list))
    elif option=="C":
        print(create(student_list,data))
    elif option=="U":
        print(update(student_list))
    elif option=="D":
        print(delete(student_list,data))


crud()