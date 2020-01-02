import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = '../data/malgun.ttf'  # 폰트 파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('ggplot')     # 스타일 서식 지정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 부호 출력 설정

df = pd.read_excel('korea_power.xlsx', convert_float=True)  # Excel 데이터를 데이터프레임 변환
df = df.loc[5:9]
df = df.drop('전력량 (억㎾h)', axis='columns')
df = df.set_index('발전 전력별')
df = df.T

df = df.rename(columns={'합계': '총발전량'})  # 증감률(변동률) 계산
df['총발전량 - 1년'] = df['총발전량'].shift(1)
df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100
print(df.head())

# 2축 그래프 그리기
ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True, color=['blue', 'red'])
ax2 = ax1.twinx()
ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=20, color='green', label='전년대비 증감율 label(%)')

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 kWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
ax1.legend(loc='upper left')
ax2.legend(loc='best')

plt.show()