import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 사용을 위해서 세팅
# https://bskyvision.com/entry/python-matplotlibpyplot%EB%A1%9C-%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B7%B8%EB%A6%B4-%EB%95%8C-%ED%95%9C%EA%B8%80-%EA%B9%A8%EC%A7%90-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95
from matplotlib import font_manager, rc
font_path = "/home/sjpark/.local/share/fonts/D2Coding-Ver1.3.2-20180524.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
df = pd.read_csv("./seoul_gangseo_data_20200930.utf-8.csv", parse_dates=[['이벤트발생연도','이벤트발생월','이벤트발생일','이벤트발생시간']])
df.rename(columns={"이벤트발생연도_이벤트발생월_이벤트발생일_이벤트발생시간":"이벤트발생시간"}, inplace=True); 

# 이벤트발생시간     이벤트분류  지구코드  발생건수

#df[df["이벤트분류"]=="FCLFT101"].plot(x="이벤트발생시간", y="발생건수")
# figure size https://financedata.github.io/posts/faq_matplotlib_default_chart_size.html
plt.rcParams["figure.figsize"] = (16, 12)
df.plot(x="이벤트발생시간", y="발생건수")
#plt.show()

plt.savefig('seoul_gangseo_20200930.png');
