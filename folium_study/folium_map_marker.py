import pandas as pd
import folium

# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('../data/서울지역 대학교 위치.xlsx')
df = df.rename({'Unnamed: 0': '학교명'}, axis=1)

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('./seoul_colleges.html')
