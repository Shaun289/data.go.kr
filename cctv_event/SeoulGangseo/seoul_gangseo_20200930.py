import matplotlib.pyplot as plt
import pandas as pd

# https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python
pd_data = pd.read_csv("./seoul_gangseo_data_20200930.utf-8.csv")
print(pd_data)

pd_data.plot(

#plt.plot([1,2,3,4]);
#plt.show()

#plt.savefig('cctv_event_metadata_20200930.png');
