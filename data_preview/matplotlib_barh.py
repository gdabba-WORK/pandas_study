import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "../data/malgun.ttf"  # 폰트 파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', fillna=0, header=0)
df = df.fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')    # 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별': '전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')

col_years = list(map(str, range(2010, 2018)))   # 서울에서 '충청남도', '경상북도', '강우너도', '전라남도'로 이동한 인구 데이터 값만 선택
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

df_4['합계'] = df_4.sum(axis=1)   # 2010-2017년 이동 인구 수를 합계하여 새로운 열로 추가
df_total = df_4[['합계']].sort_values(by='합계', ascending=True)    # 가장 큰 값부터 정렬

# 스타일 서식(배경) 지정
plt.style.use('ggplot')

# 막대 그래프 그리기
df_total.plot(kind='barh', figsize=(10, 5), width=0.5, color='cornflowerblue')

plt.title('서울 -> 타시도 인구 이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')

plt.show()
