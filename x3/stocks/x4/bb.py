import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import time
from numerize import numerize
from yahoo_fin import stock_info as f
import yahoo_fin.stock_info as si
from googlefinance import getQuotes as gg
import json

pd.options.display.max_columns=26
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)


########################################################## daily ##################################################

perda='55d'
intervla='1d'


g=input("Enter ticker: ")
perd=perda
intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(g, period=perd, interval=intervl,prepost = True)
print(data)
