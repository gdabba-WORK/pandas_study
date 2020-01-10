import pandas as pd

name=pd.Series({0:'Potter',1:'Elsa',2:'Gates',3:'Wendy',4:'Ben'})
gender=pd.Series({0:'Female',1:'male',2:'Female',3:'male',4:'Female'})
math=pd.Series({0:85,1:76,2:99,3:88,4:40})
num=pd.Series({0:0,1:1,2:2,3:3,4:4})

# print(name,type(name),sep='\n')#,gender,math,sep='\n\n')

df = pd.DataFrame([name,gender,math])
df_t=df.transpose()

columns = ['name','gender','math']
df_t.columns = columns
print(df_t['name'],df_t['gender'],df_t['math'],sep='\n\n')
df_t = df_t.set_index('name')
df_t['name']='a'
for i in range(len(name)):
    df_t['name'][i]=name[i]#[i]
    df_t['gender'][i],df_t['name'][i] =df_t['name'][i],df_t['gender'][i]
    df_t['name'][i], df_t['math'][i] =df_t['math'][i],df_t['name'][i]
df_t.columns = columns
print('\n',df_t)

