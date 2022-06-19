import json
from flask import Flask,render_template

app=Flask(__name__)

@app.rote('/create')
def create():
    x=open('student.json','r')
    data=json.load(x)
    student_list=data['name']
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

@app.route('/viewStudents',methods=['post','get'])
def read():
    x=open('student.json','r')
    data=json.load(x)
    return data
    
    
if __name__=='__main__':
    app.run(debug=True)