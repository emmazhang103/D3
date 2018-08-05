# -*- coding: utf-8 -*-
import pandas as pd
xl = pd.ExcelFile('数据.xlsx')
df=xl.parse('工作表1')
df1=df.fillna(method='pad')
node={"name":"","children":[]}
leaf={"name":"","size":0}
result=[]
name_list=[]

for i in df1.index:
    if df1.iloc[i][0] not in name_list:
        name_list.append(df1.iloc[i][0])
        node={"name":df1.iloc[i][0],"children":[]}
        result.append(node)
    else:
        pass

name_list2=[]
for i in df1.index:
    name1=df1.iloc[i][0]
    name2=df1.iloc[i][1]
    if name2 not in name_list2:
        name_list2.append(name2)
        node={"name":name2,"children":[]}
        for i in result:
            if i['name']==name1:
                i["children"].append(node)
            else:
                pass
    else:
        pass

name_list3=[]
for i in df1.index:
    name1=df1.iloc[i][0]
    name2=df1.iloc[i][1]
    name3=df1.iloc[i][2]
    if name3 not in name_list3:
        if name3=='无':
            name3=name2
        name_list3.append(name3)
        node={"name":name3,"children":[]}
        for i in result:
            if i['name']==name1:
                for j in i["children"]:
                    if j["name"]==name2:
                        j["children"].append(node)
            else:
                pass
    else:
        pass


name_list4=[]
for i in df1.index:
    name1=df1.iloc[i][0]
    name2=df1.iloc[i][1]
    name3=df1.iloc[i][2]
    name4=df1.iloc[i][3]
    if name4 not in name_list4:
        if name4=='无':
            if name3=='无':
                name4=name2
                name3=name2
            else:
                name4=name3
        name_list4.append(name4)
        leaf={"name":name4,"size":df1.iloc[i][4]}
        print(leaf)
        print('name:',(name1,name2,name3,name4))
        for i in result:
            if i['name']==name1:
                for j in i["children"]:
                    if j["name"]==name2:
                        for k in j['children']:
                            if k['name']==name3:
                                k["children"].append(leaf)
                                print('add:',leaf)
            else:
                pass
    else:
        pass


out=str(result[0])
out=out.replace("'","\"")
with open('flare.json', 'w',encoding='utf8') as fout:
    fout.write(out)
    