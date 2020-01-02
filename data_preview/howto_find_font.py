import matplotlib
import matplotlib.font_manager as fm

# matplotlib 출력 한글 설정 방법

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')   # .ttf 확장자를 갖는 모든 폰트 리스트를 가져온다.
[print(_) for _ in font_list]       # 여기서 출력되는 폰트 리스트 중 한글 관련 폰트의 경로를 찾는다.
a = fm.FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothic.ttf')  # 위에서 찾은 폰트의 경로 full name을 파라미터로 던져준다.
print(a.get_name()) # a.get_name() 으로 폰트의 이름을 확인한다.

matplotlib.rcParams['font.family'] = 'NanumGothic'  # 적용할 폰트 이름을 우변에 대입한다.
matplotlib.rcParams['axes.unicode_minus'] = False   # ???