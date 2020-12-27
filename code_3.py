import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('data_2.csv')
fig = ff.create_distplot([df["Avg Rating"]], ["Average Mobile Rating"], show_hist=False)
fig.show()