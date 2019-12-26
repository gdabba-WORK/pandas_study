import pandas as pd
import numpy as np

df = pd.read_csv("./auto-mpg.csv", header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print("# 각 열의 자료형 확인")
print(df.dtypes, '\n')

print("# horsepower 열의 고유값 확인")
print(df['horsepower'].unique(), '\n')

print("# 누락 데이터('?') 삭제 및 결과")
ndf = df.replace('?', np.nan, subset=['horsepower'])
ndf = ndf.dropna(subset=['horsepower'], axis=0)
ndf['horsepower'] = ndf['horsepower'].astype('float')

print("# 각 열의 자료형 확인")
print(ndf.dtypes, '\n')

print("# horsepower 열의 고유값 확인")
print(ndf['horsepower'].unique(), '\n')