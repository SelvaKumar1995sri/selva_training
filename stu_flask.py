import json
from operator import index, indexOf
from flask import Flask,render_template, request
import requests


app=Flask(__name__)

@app.route('/create',methods=['post'])
def create_operation():
    x=open('student.json','r')
    data_obj=json.load(x)
    data_list=data_obj['students']
    val = request.get_json()    
    data_list.append(val)
    with open('studen.json','w') as y:
        json.dump(data_obj,y)
    return "created successfully"

@app.route('/update',methods=['put'])
def update():
    x=open('student.json','r')
    data_obj=json.load(x)
    data_list=data_obj["students"]
    val = request.get_json()
    for i in data_list:
        if i['id']==val["id"]:
            index_i=data_list.index(i)
            data_list[index_i]=val

    with open('student.json','w') as y:
        json.dump(data_obj,y)
    return "updated successfully"

@app.route('/delete',methods=['delete'])
def delete():
    x=open('student.json','r')
    data_obj=json.load(x)
    data_list=data_obj['students']
    val = request.get_json()
    for i in data_list:
        if i['id']==val['id']:
            index_i=data_list.index(i)
            del data_list[index_i]
    
    with open('student.json','w') as y:
        json.dump(data_obj,y)
        return "successfully deleted"

@app.route('/viewStudents',methods=['post','get'])
def read():
    x=open('student.json','r')
    data=json.load(x)
    x.close()
    return data
    
    
if __name__=='__main__':
    app.run(debug=True)