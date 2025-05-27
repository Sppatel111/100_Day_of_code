import pandas as pd

data=pd.read_csv('employee_data(in).csv')
print(data)

for i in data:
    print(i)

print(data[1])