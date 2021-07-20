import numpy as np
import pandas as pd
import numpy,datetime
import sys
import calendar
from datetime import time
from numerize import numerize
from get_all_tickers import get_tickers as gt
from datetime import datetime
import pytz

#_EXCHANGE_LIST = ['nyse', 'nasdaq', 'amex']
#def get_tickers_filtered(mktcap_min=None, mktcap_max=None, sectors=None):
#        tickers_list = []
#        for exchange in _EXCHANGE_LIST:
#            tickers_list.extend(__exchange2list_filtered(exchange, mktcap_min=mktcap_min, mktcap_max=mktcap_max, sectors=sectors)
#            return tickers_list


#`print(tickers_list.get_tickers_filtered)           
print(gt.get_tickers(NYSE=True, NASDAQ=True, AMEX=True))  



tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)

tz_LA = pytz.timezone('US/Pacific') 
datetime_LA = datetime.now(tz_LA)
print("LA time:", datetime_LA.strftime("%H:%M:%S"))
print("NY time:", datetime_NY.strftime("%H:%M:%S"))
#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

pd.options.display.max_rows=9999
pd.options.display.max_columns=15
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)


#g='F'
#perd=perda
intervl='1m'
perda='3d'
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

df['timea']=df['Datetime'].dt.time
df['daya']=df['Datetime'].dt.day_name()
df['datea']=df['Datetime'].dt.date

b=pd.Series(df['Volume'])
#a = numerize.numerize(b[0])


for x in df.index:
    df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())
#    print(x,'              ',numerize.numerize(np.float32(df['Volume'].loc[x]).item()))
#    df['Volume']=df.loc[x]


#print(df)

df2=df[['datea','daya','timea','Volume']]
#print(df2.head(4))
df2a=df[['datea','daya','timea','Close']]
df2a['Close']=df2a['Close'].round(2)

print('\n','     ',g.upper(),' Volume                 Time now ',datetime_NY.strftime("%H:%M:%S"),'/',datetime_LA.strftime("%H:%M:%S"),'   \n')
df3=df2.pivot(index=['datea','daya'], columns='timea', values='Volume')
print(df3.iloc[:,11:20])



print('\n','     ',g.upper(),' Close               Time now   ',datetime_LA.strftime("%H:%M:%S"),'  \n')
df3a=df2a.pivot(index=['datea','daya'], columns='timea', values='Close')
print(df3a.iloc[:,11:20])


