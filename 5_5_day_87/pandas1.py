import pandas as pd

# load file into dataframe
# pd.options.display.max_rows=20

df=pd.read_csv('salaries_by_college_major.csv')

# print(pd.options.display.max_rows)
# print(df)
# print(df.to_string())


## Dataframe
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# df1=pd.DataFrame(mydataset)
# print(df1)

print(pd.__version__)

## series
a=[1,2,3,4]

s=pd.Series(a)
#named index with series
s1=pd.Series(a,index=['a','b','c','d'])
# print(s)
# print(s[0])
# print(s1)
# print(s1['c'])

calories={'day1':238,'day2':340,'day3':560}
s2=pd.Series(calories)
# print(s2)
# print(len(s2))

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df2=pd.DataFrame(data)
# print(df2)
#row
# print(df2.loc[[0,1]])

#named indexd with dataframe
df3=pd.DataFrame(data,index=['day1','day2','day3'])
# print(df3)
#
# print(df3.loc['day2'])


df4 = pd.read_json('titanic.json',lines=True)
# print(df4)
# print(df4.head(10).to_string())
# print(df4.tail(10).to_string())
print(df4.info())


df_new=df4.dropna()
# print(df_new)
# print(df_new.info())

# change existance
# df4.dropna(inplace=True)
# print(df4.to_string())
# df4.fillna(120,inplace=True)

# df4.fillna({'Age':22,'Cabin':'A111','Embarked':'A'},inplace=True)

# x=df4['Age'].mean()
x=df4['Age'].median()
x=df4['Age'].mode()[0]
print(x)

df4.fillna({'Age':x,'Cabin':'A111','Embarked':'A'},inplace=True)
print(df4.info())

#replacing values
df4.loc[0,'Pclass']=1
# print(df4.to_string())


# for i in df4.index:
#   if df4.loc[i,'Survived']== 0:
#     df4.loc[i,'Survived']= 11
# print(df4.to_string())

## removing rows
# for i in df4.index:
#   if df4.loc[i,'Survived']== 0:
#     df4.drop(i,inplace=True)
# print(df4.to_string())

# print(df4.duplicated().to_string())

# df4.drop_duplicates(inplace=True)


df5=pd.read_csv('data.csv')
print(df5.corr())
import matplotlib.pyplot as plt
# df5.plot()
# df5.plot(kind='scatter',x='Duration',y='Calories')
# df5.plot(kind='scatter',x='Duration',y='Maxpulse')
df5['Duration'].plot(kind='hist')
plt.show()