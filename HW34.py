import pandas as pd 

data ={'Name':['Ivan','Petr','Alexandra'],
       'Age': [25,30,35],
       'Gender':['M','M','W'],
       'GPA':[5,4,4]
}
df= pd.DataFrame(data)
print (df)
print(df['Name'])
z_pol = df[df['Gender'] == 'W']
print(z_pol)

max_gpa_student = df[df['GPA'] == df['GPA'].max()]
print(max_gpa_student)

df['Age'] = df['Age'] + 1
print(df)

min_age = df['Age'].min()
df.loc[df['Age'] == min_age, 'GPA'] = 4.0
print(df)

new_student = {'Name': 'Olga', 'Age': 29, 'Gender': 'W', 'GPA': 5}
df = df.append(new_student, ignore_index=True)
print(df) 