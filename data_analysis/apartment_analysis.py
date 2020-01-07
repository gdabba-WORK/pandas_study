import seaborn as sns
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothicCoding'  # '맑은 고딕' 으로 설정

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 20)  # 출력할 최대 열의 개수
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비
matplotlib.rcParams['axes.unicode_minus'] = False

# 파일 불러오기
pre_sale = pd.read_csv('../data/전국 평균 분양가격(2015년 10월부터 2019년 11월).csv', encoding='euc-kr')
print("pre_sale.shape :", pre_sale.shape, '\n', sep='\n')
print("pre_sale.head() :", pre_sale.head(), '\n', sep='\n')
print("pre_sale.tail() :", pre_sale.tail(), '\n', sep='\n')

print("# 분양가격이 숫자 타입이 아님, 숫자 타입으로 변경")
print("pre_sale.info() :", pre_sale.info(), '\n', sep='\n')
print("pre_sale.dtypes :", pre_sale.dtypes, '\n', sep='\n')

print("# 결측지 확인")
print("pre_sale.isnull().sum() :")
print(pre_sale.isnull().sum(), '\n\n')

print("pre_sale['분양가격(㎡)'].value_counts(dropna=False) :")
print(pre_sale['분양가격(㎡)'].value_counts(dropna=False), '\n\n')

print("# 연도와 월은 카테고리 형태의 데이터이기 때문에 스트링 형태로 변경")
pre_sale['연도'] = pre_sale['연도'].astype(str)
pre_sale['월'] = pre_sale['월'].astype(str)
print("pre_sale.dtypes :")
print(pre_sale.dtypes, '\n\n')

print("# 분양가격의 타입을 숫자로 변경")
pre_sale_price = pre_sale['분양가격(㎡)']
# If 'coerce', then invalid parsing will be set as NaN
pre_sale['분양가격'] = pd.to_numeric(pre_sale_price, errors='coerce')
pre_sale = pre_sale.drop(['분양가격(㎡)'], axis=1)
print("pre_sale.head() :")
print(pre_sale.head(), '\n\n')

print("# 평당 분양가격 계산")
pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3
print("pre_sale['평당분양가격'] = pre_sale['분양가격'] * 3.3")
print("pre_sale.head() :")
print(pre_sale.head(), '\n\n')

print("# 수치형 자료만 요약하여 보기")
print("pre_sale.describe()")
print(pre_sale.describe(), end='\n\n')

print("# 문자열 요약하여 보기")
print("pre_sale.describe(include=[np.object])")
print(pre_sale.describe(include=[np.object]), '\n\n')

print("# 2017년 데이터보기")
pre_sale_2017 = pre_sale.loc[pre_sale['연도'] == '2017']
print("pre_sale_2017 = pre_sale.loc[pre_sale['연도'] == '2017']")
print("pre_sale_2017.shape")
print(pre_sale_2017.shape, '\n\n')

print("pre_sale['규모구분'].value_counts()")
print(pre_sale['규모구분'].value_counts(), '\n\n')

print("pre_sale['지역명'].value_counts()")
print(pre_sale['지역명'].value_counts(), '\n\n')

pd.options.display.float_format = '{:,.0f}'.format  # 실수 출력 양식 지정. 천단위 ','구분, 소수점 이하 '0'개출력.
print("pre_sale.groupby([pre_sale.연도, pre_sale.규모구분]).describe() :\n",
      pre_sale.groupby([pre_sale.연도, pre_sale.규모구분]).describe(), '\n\n')

print("pre_sale.pivot_table(values='평당분양가격', index='규모구분', columns='연도')")
print(pre_sale.pivot_table(values='평당분양가격', index='규모구분', columns='연도'),
      '\n\n')  # pivot_table() 함수 인자 'argfunc='를 지정하지 않으면 defult로 'mean' 전달

print("# 규모 구분에서 전체로 되어 있는 데이터만 가져오기")
region_year_all = pre_sale.loc[pre_sale['규모구분'] == '전체']
print("region_year_all = pre_sale.loc[pre_sale['규모구분'] == '전체']")
print(region_year_all, '\n\n')

print("region_year_all.pivot_table(values='평당분양가격', index='지역명', columns='연도') :")
print(region_year_all.pivot_table(values='평당분양가격', index='지역명', columns='연도'), '\n\n')

print("# reset_index")
region_year = region_year_all.pivot_table('평당분양가격', '지역명', '연도').reset_index()
print("region_year = region_year_all.pivot_table('평당분양가격', '지역명', '연도').reset_index()")
print(region_year, '\n\n')

# 2015년에서 2019년 변동액 계산
region_year['변동액'] = (region_year['2019'] - region_year['2015']).astype(float)
print("region_year['변동액'] = (region_year['2019'] - region_year['2015']).astype(float)")
print(region_year, '\n\n')
print("region_year.sort_values('변동액', ascending=False)")
print(region_year.sort_values('변동액', ascending=False), '\n\n')

max_delta_price = np.max(region_year['변동액']) * 1000
min_delta_price = np.min(region_year['변동액']) * 1000
mean_delta_price = np.mean(region_year['변동액']) * 1000

print("2015년 부터 2019년까지 분양가는 계속 상승했으며, 상승액이 가장 큰 지역은 서울이며 상승액은 평당{:,.0f}원이다.".format(max_delta_price))
print("상승액이 가장 작은 지역은 울산이며 평당 {:,.0f}원이다.".format(min_delta_price))
print("하지만 나중에 살펴보겟지만 울산에는 결측지가 많다. 따라서 변동액이 가장 작다고 판단하기 어렵다.")
print("전국 평균 변동액은 평당 {:,.0f}원이다.".format(mean_delta_price), '\n\n')

# 차트그리기 속성 지정
sns.set_style('whitegrid')

# window 한글 폰트 설정
plt.rc('font', family='NanumGothic')

# Mac 한글폰트
# plt.rc('font', family='AppleGothic')

# seaborn 차트
# plt.figure(figsize=(20, 8))
# plt.title('2015-2019년 신규 민간 아파트 분양가격')
# sns.barplot(data=region_year_all, x='지역명', y='평당분양가격', hue='연도')
# plt.show()

# pandas 차트
# df_year_region = pd.pivot_table(region_year_all,
#                                 index=['지역명'],
#                                 columns='연도',
#                                 values='평당분양가격')
# print("df_year_region.sample(3)")
# print(df_year_region.sample(3), '\n\n')
# df_year_region.plot.bar(figsize=(24, 8), grid=True, fontsize=20, rot=0, title='지역, 연도별 평당 평균 분양가')
# plt.show()

# 지역별 평당 분양가격 합계
print("pre_sale.pivot_table('평당분양가격', '규모구분', '지역명')")
print(pre_sale.pivot_table('평당분양가격', '규모구분', '지역명'), '\n\n')

# 서울의 경우 전용면적 85㎡초과 102㎡이하가 분양가격이 가장 비싸게 나옵니다.
# seaborn bar plot
# plt.figure(figsize=(20, 8))
# plt.title('규모구분별 신규 민간 아파트 분양가격')
# sns.barplot(data=pre_sale, x='지역명', y='평당분양가격', hue='규모구분')
# plt.show()

# 지역별 평당 분양가격 합계
pre_sale_size = pre_sale.pivot_table(values='평당분양가격', index='지역명', columns='규모구분')
print("pre_sale_size = pre_sale.pivot_table(values='평당분양가격', index='지역명', columns='규모구분')")
print(pre_sale_size.sample(3), '\n\n')

# pandas bar plot
# pre_sale_size.plot.bar(title='지역, 규모구분 별 평당 평균 분양가',
#                        figsize=(20, 8),
#                        grid=True,
#                        fontsize=20,
#                        rot=0)
# plt.show()

print("pre_sale[(pre_sale.지역명 == '대전') & (pre_sale.규모구분 == '전용면적 102㎡초과')]")
print(pre_sale[(pre_sale.지역명 == '대전') & (pre_sale.규모구분 == '전용면적 102㎡초과')], '\n\n')

# pre_sale_size 전치
print("pre_sale_size_t = pre_sale_size.T")
pre_sale_size_t = pre_sale_size.T
print(pre_sale_size_t, '\n\n')

# 결측지 확인
print("pre_sale.평당분양가격.isnull().sum()")
print(pre_sale.평당분양가격.isnull().sum(), '\n\n')


# pandas box plot
pre_sale[['연도', '지역명', '평당분양가격']].boxplot(
    by=['지역명', '연도'],
    figsize=(18, 6),
    fontsize=12,
    rot=60
)
plt.show()

pre_sale_seoul = pre_sale[pre_sale['지역명'] == '서울']
print("pre_sale_seoul")
print(pre_sale_seoul, '\n\n')

# 2013년 12월이후 2015년 9월 까지의 데이터와 병합하기 위해 파일로 저장
df_2015_2019 = pre_sale.loc[pre_sale['규모구분'] == '전체']
df_2015_2019.to_csv('../data/전국 전체 분양가격(2015_2019).csv')