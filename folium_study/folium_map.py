import folium

# 서울 지도 만들기
seoul_map1 = folium.Map(location=[37.55, 126.98], zoom_start=12)
seoul_map2 = folium.Map(location=[37.55, 126.98], zoom_start=15, tiles='Stamen Toner')
seoul_map3 = folium.Map(location=[37.55, 126.98], zoom_start=12, tiles='Stamen Terrain')

# 지도를 HTML 파일로 저장하기
seoul_map1.save('./seoul1.html')
seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')