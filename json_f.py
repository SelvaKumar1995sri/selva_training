import json
op=open('initial.json','r')
d=json.load(op)

role_file=d['data']["user_groups"][0]['role_details']

name_lst=[]
for j in role_file:
    name_lst.append(j['name'])
uniq_name=set(name_lst)
res=[]
for k in uniq_name:
    role_id=[x['id'] for x in role_file if x['name']==k]
    res.append({'name':k,'roles': role_id})

op.close()
d['data']["user_groups"][0]['role_details']=res

data_file=open('initial.json','w')
# data_object=json.load(data_file)
json.dump(d,data_file)

data_file.close()


