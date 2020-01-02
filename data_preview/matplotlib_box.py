import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = '../data/malgun.ttf'  # 폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name)

plt.style.use('seaborn-poster')     # 스타일 서식 지정
plt.rcParams['axes.unicode_minus'] = False      # 마이너스 부호 출력 설정

df = pd.read_csv('./auto-mpg.csv', header=None)
