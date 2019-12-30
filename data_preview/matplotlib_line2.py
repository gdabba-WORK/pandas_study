import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', fillna=0, header=0)

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)  # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드 사용 너비 조정
pd.set_option('display.width', 600)  # 콘솔 출력 너비

print(df.head())

# 누락값(Nan)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')
print(df.head())

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별': '전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')

print(df_seoul.head())

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
print(type(sr_one.values))
print(sr_one.head())

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동')

# 축 이름 추가
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수', size=20)

# 범례 표시
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)

# 스타일 지정
plt.style.use('ggplot')

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation=45)

# 변경사항 저장하고 그래프 출력
plt.show()

# 스타일 리스트 출력
[print(style) for style in plt.style.available]