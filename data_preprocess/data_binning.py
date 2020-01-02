import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 600)

df = pd.read_csv("../data/auto-mpg.csv", header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print("df[horsepower]", "\n", df['horsepower'], '\n')

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'] = df['horsepower'].replace('?', np.nan)
df = df.dropna(subset=['horsepower'], axis=0)
df['horsepower'] = df['horsepower'].astype('float')

print("# np.histogram 함수로 3개의 bin으로 나누는 경계 값의 리스트 구하기")
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print("count = ", count)
print("bin_dividers = ", bin_dividers, '\n')

# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],   # 데이터 배열
                      bins=bin_dividers,    # 경계 값 리스트
                      labels=bin_names,     # bin 이름
                      include_lowest=True)  # 첫 경계값 포함

print("# horsepower 열, hp_bin 열의 첫 15행을 출력")
print(df[['horsepower', 'hp_bin']].head(15), '\n')

print(df['hp_bin'].cat.categories)