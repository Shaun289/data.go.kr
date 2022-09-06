import matplotlib.pyplot as plt
import pandas as pd

# https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
df = pd.read_csv("./seoul_gangseo_data_20200930.utf-8.csv", parse_dates=[['이벤트발생연도','이벤트발생월','이벤트발생일','이벤트발생시간']])
df.rename(columns={"이벤트발생연도_이벤트발생월_이벤트발생일_이벤트발생시간":"이벤트발생시간"}, inplace=True); 

# 이벤트발생시간     이벤트분류  지구코드  발생건수

#df[df["이벤트분류"]=="FCLFT101"].plot(x="이벤트발생시간", y="발생건수")
df.plot(x="이벤트발생시간", y="발생건수")
plt.show()


#plt.savefig('cctv_event_metadata_20200930.png');
