import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'    # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

# read_csv() 함수로 df 생성
df = pd.read_csv('../data/auto-mpg.csv')

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
              'weight', 'acceleration', 'model year', 'origin', 'name']