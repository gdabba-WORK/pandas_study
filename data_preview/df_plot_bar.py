import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'    # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('korea_power.xlsx')  # 데이터프레임 변환

df_ns = df.iloc[[0, 5], 3:]         # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']    # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)  # 열 이름의 자료형을 정수형으로 변경

# 행, 열 전치하여 막대 그래프 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')

tdf_ns.plot(kind='bar', title="남북한 발전 전력량")

plt.show()
