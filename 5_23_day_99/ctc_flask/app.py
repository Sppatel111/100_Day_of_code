from flask import Flask,render_template
import pandas as pd
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import math
app=Flask(__name__)
class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
app.config['SECRET_KEY']='3434FFWERTWER'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ctc.db'


# engine=create_engine('sqlite:///ctc.db')
# print(data)
# table_name = 'ctc_table'
# data.to_sql(table_name, engine, if_exists='replace', index=False)

# def provident_fund(ctc,present,total):
#     fgw=0
#     if ctc > 24299:
#         fgw =ctc-1800
#     elif ctc > 15000:
#         fgw = ((ctc-7500)/1.12)+7500
#     else:
#         fgw=ctc/1.06
#
#     prov= (ctc-fgw) * (present/total)
#     print(prov)
#     with24= prov * 2
#     return round(with24,2)

def provident_fund(pf,ctc,present,total):
    fgw=0
    if pf == 'Y':
        if ctc > 24299:
            fgw =ctc-1800
        elif ctc > 15000:
            fgw = ((ctc-7500)/1.12)+7500
        else:
            fgw=ctc/1.06
    elif pf == 'N':
        fgw=ctc
    else:
        print('incorrect value')

    prov= (ctc-fgw) * (present/total)
    print(prov)
    with24= prov * 2
    return round(with24,2)

def calculate_present_day(hours):
    full =hours // 9
    print(full)
    r=hours % 9
    print(r)
    if r >= 4.5:
        return full + 0.5
    return full


def data_to_dict():
    data = pd.read_csv('employee_data(in).csv')

    print(data)
    data['Present']=data.apply(lambda row:calculate_present_day(row['Working Hours']),axis=1)
    data['Leaves']=data['Working Days']-data['Present']
    #start
    data['Basic']=data['Salary']/2
    data['HRA']=data.apply(lambda row : min(row['Salary'] - row['Basic'],7500),axis=1)
    #not usable
    data['hra']=data['Salary'] - data['Basic']

    data['DA']=0
    data['OA']=data['Salary'] - data['Basic']-data['HRA']-data['DA']
    data['PFC']=data.apply(lambda row:provident_fund(row['PF'][0],row['Salary'],row['Present'],row['Working Days']),axis=1)
    # remaining
    data['LD']=round((data['Salary']/data['Working Days']) * data['Leaves'],2)
    data['NS']=round(data['Basic']+ data['HRA']+data['DA']+data['OA']-data['PFC']-data['LD'],2)

    return data.to_dict(orient='records')


@app.route('/',methods=['GET','POST'])
def home():
    data = pd.read_csv('employee_data(in).csv')
    employers=data_to_dict()
    print(employers)
    return render_template('home.html',employers=employers,data=data)

if __name__ =='__main__':
    app.run(debug=True)