import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

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

# 한글 설정(case1)
# matplotlib.rcParams['font.family'] = 'NanumGothic'
# matplotlib.rcParams['axes.unicode_minus'] = False

# matplotlib 한글 폰트 오류 문제 해결(case2)
font_path = '../data/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values)
plt.xticks(rotation=45)
# plt.show()

# 판다스 객체를 plot 함수에 입력
# plt.plot(sr_one)
# plt.show()

# 차트 제목 추가
plt.title('서울 -> 경기 인구 이동')

# 축 이름 추가
plt.xlabel('기간')
plt.ylabel('이동 인구수')
# plt.show()


# 범례 표시
plt.legend(labels=['서울 -> 경기'], loc='best')
plt.show()