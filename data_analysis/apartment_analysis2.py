import pandas as pd

# 파일 불러오기
df_2013_2015 = pd.read_csv('../data/전국 평균 분양가격(2013년 9월부터 2015년 9월까지).csv',
                           encoding='euc-kr',
                           skiprows=1,
                           header=0,
                           engine='python')
print(df_2013_2015.shape, '\n', df_2013_2015.head(), '\n', df_2013_2015.tail())


# 24열 이후 삭제(통계정보)
df_2013_2015 = df_2013_2015.drop(columns=df_2013_2015.columns[24:])
print("df_2013_2015.columns")
print(df_2013_2015.columns, '\n\n')

year = df_2013_2015.iloc[0]
year = year.fillna(method='ffill')  # 결측지를 전의 값으로 채워줌

month = df_2013_2015.iloc[1]
print("year :")
print(year, '\n\n')
print("month :")
print(month)

for i, y in enumerate(year):
    if i > 1:
        year[i] = ' '.join([str(year[i]), '{:,.0f}'.format(month[i])])
year[1] = '시군구'

print("year :")
print(year, '\n\n')

df_2013_2015.columns = year
print("df_2013_2015 :")
print(df_2013_2015, '\n\n')

# 통계정보 제거
df_2013_2015 = df_2013_2015.drop(df_2013_2015.index[[0, 1, 2, 10, 12, 22]])
print(df_2013_2015, '\n\n')

df_2013_2015.loc[4, '구분'] = ''
df_2013_2015.loc[14, '구분'] = ''
print(df_2013_2015, '\n\n')

# '지역명' 컬럼을 새로 만들어 시도와 시군구를 병합
# 결측지 빈문자로
df_2013_2015['구분'] = df_2013_2015['구분'].fillna('')
df_2013_2015.시군구 = df_2013_2015.시군구.fillna('')
print(df_2013_2015, '\n\n')

df_2013_2015['지역명'] = df_2013_2015.구분 + df_2013_2015.시군구
print(df_2013_2015, '\n\n')
print(df_2013_2015.drop(['구분', '시군구'], axis=1))