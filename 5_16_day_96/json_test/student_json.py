# find total, percentage, grade of the students
# find Top 3 students
# find top 3 subjects
# generate csv file for student details
# generate JSON file for top 3 students and top 3 subjects

# A+: 90–100
# A: 80–89
# B: 70–79
# C: 60–69
# D: 50–59
# F: below 5

import json
import csv
import pandas as pd
with open('student.json','r') as f:
    data=json.load(f)
# print(data)
# print(data[0]['subjects'])

#total
list1=[]
for i in range(len(data)):
    subject=data[i]['subjects']
    # print(subject)
    total=0
    count=0
    for k,v in subject.items():
        # print(v)
        total +=v
        count +=1
        # print(total)
    # print(count)
    per=total/count
    data[i]['total']=total
    data[i]['percentage']=per

    if per < 50:
        data[i]['grade']='F'
    elif 50 <= per <= 59:
        data[i]['grade']='D'
    elif 60 <= per <= 69:
        data[i]['grade']='C'
    elif 70 <= per <= 79:
        data[i]['grade']='B'
    elif 80 <= per <= 89:
        data[i]['grade']='A'
    else:
        data[i]['grade'] = '+A'

    list1.append(per)
    print(data)
    with open('students1.csv','w') as f:
        csv1=csv.writer(f)

        # if data:
        #     header = data[0].keys()
        #     csv1.writerow(header)
        #     for row in data:
        #         csv1.writerow(row.values())
        if data:
            header = data[0].keys()
            csv1.writerow(header)
            for row in data:
                csv1.writerow(row.values())
        # dm=data[0]
        # for i in data:
        #     for k,v in i.items():
        #         # if k !='subjects':
        #         csv1.writerow([v])


    with open('student1.json','w') as write:
        json.dump(data,write)



# print(list1)
#top 3 students
with open('student1.json','r') as read:
    data1=json.load(read)

    dict={}
    for i in range(len(list1)):
        dict[i] = list1[i]
    print(dict)

    list1.sort(reverse=True)
    print(list1)

    list2=[]
    for i in range(len(list1)):
        if i<3:
            list2.append(list1[i])

    top_keys=[]
    for i in list2:
        for k,v in dict.items():
            if i == v:
                top_keys.append(k)
    print(top_keys)



    with open('top_students.json', 'w') as write:
        top_students=[]
        for i in top_keys:
            top_students.append(data1[i])

        json.dump(top_students, write)

print(top_students)
with open('top_students.json','r') as r1:
    new = json.load(r1)
    top1= []
    sub=[]
    dict2={}
    sub_dict={}
    for i in range(len(new)):
        print(new[i]['subjects'])
        first=new[i]['subjects']
        # print(first)

        for i in first.values():
            top1.append(i)
        for j in first.keys():
            sub.append(j)

    print(top1)
    print(sub)
    for i in range(len(top1)):
        dict2[i]=top1[i]

    for j in range(len(sub)):
        sub_dict[j]=sub[j]

    top1.sort(reverse=True)
    print(top1)
    print(dict2)
    print(sub_dict)

    top2 = []
    for i in range(len(top1)):
        if i < 3:
            top2.append(top1[i])

    top_s_keys = []
    for i in top2:
        for k, v in dict2.items():
            if i == v:
                top_s_keys.append(k)
    print(top_s_keys)

    with open('top_students_top_subject.json', 'w') as last:
        t={}
        for i in top_s_keys:
            t[sub_dict[i]]=dict2[i]
        final_dict={}
        final_dict['top_students']=top_students
        final_dict['top_subjects']=t
        json.dump(final_dict, last)












