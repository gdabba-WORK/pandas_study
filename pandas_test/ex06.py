import pandas as pd
exam = {'시험':['중간','기말'],'수학':[95,90],'국어':[90,85],'영어':[85,80]}
df = pd.DataFrame(exam)
df = df.set_index('시험')
print(df)
print()

sum = df.sum(axis=1)
mean = df.mean(axis=1)
df['합계'] = sum
df['평균'] = mean
print(df)