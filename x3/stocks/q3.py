import numpy as np
import pandas as pd
import numpy,datetime
import sys
import calendar
from datetime import time
from numerize import numerize

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

pd.options.display.max_rows=9999
pd.options.display.max_columns=15
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)


intervl='1m'
perda='5d'
#intervl='60m'
# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
perd=perda
g=input("Enter Ticker :")
#g = 'T'
#perd=input("Enter no of days '5d','2d','1d' :")
#intervl=input("Enter mins '5m','1m' :")


#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(g, period=perd, interval=intervl)

df=pd.DataFrame(data)
df.reset_index(inplace=True)
#df['Volume']=numerize.numerize(np.float32(df['Volume']).item())
'''
df['timea']=df['Datetime'].dt.time
df['daya']=df['Datetime'].dt.day_name()
df['datea']=df['Datetime'].dt.date
'''
b=pd.Series(df['Volume'])
print(df.head(5))
