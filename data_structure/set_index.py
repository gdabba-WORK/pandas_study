import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print()

print("# 특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정")
ndf = df.set_index(['이름'])
print(ndf)
print()

ndf2 = ndf.set_index(['음악'])
print(ndf2)
print()

ndf3 = ndf.set_index(['수학', '음악'])
print(ndf3)
print()

print("수학 음악 (80, 95) 선택1 : ndf3.loc[(80, 95)]")
print(ndf3.loc[(80, 95)])
print(type(ndf3.loc[(80, 95)]))
print()

print("수학 음악 (80, 95) 선택2 : ndf3.loc[80]")
print(ndf3.loc[80])
print(type(ndf3.loc[80]))
print()

print("수학 음악 (80, 95) 선택3 : ndf3.iloc[1]")
print(ndf3.iloc[1])
print(type(ndf3.iloc[1]))
print()

ndf4 = ndf3.set_index(['영어'])
print(ndf4)
print()

ndf5 = ndf4.set_index(['체육'])
print(ndf5)
print(type(ndf5))