{"filter":false,"title":"x5_c.py","tooltip":"/x3/stocks/x5_c.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":308,"column":0},"end":{"row":388,"column":0},"action":"remove","lines":["#################################################################################################################","## Section2","","import numpy as np","import pandas as pd","import numpy,datetime","import sys","import calendar","from datetime import time","from numerize import numerize","","#Data Source","import yfinance as yf","","#Data viz","import plotly.graph_objs as go","","pd.options.display.max_rows=9999","pd.options.display.max_columns=15","pd.set_option(\"display.max_columns\", 100)","pd.set_option('display.width', 1000)","","","","","intervl='1d'","perda='10d'","#intervl='60m'","# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]","perd=perda","# g=input(\"Enter Ticker :\")","","","#g = 'T'","#perd=input(\"Enter no of days '5d','2d','1d' :\")","#intervl=input(\"Enter mins '5m','1m' :\")","","","#df=pd.DataFrame()","#Interval required 5 minutes","data = yf.download(g, period=perd, interval=intervl)","","df=pd.DataFrame(data)","df.reset_index(inplace=True)","#df['Volume']=numerize.numerize(np.float32(df['Volume']).item())","","df['timea']=df['Datetime'].dt.time","df['daya']=df['Datetime'].dt.day_name()","df['datea']=df['Datetime'].dt.date","","b=pd.Series(df['Volume'])","#a = numerize.numerize(b[0])","","print('\\n\\n')","","for x in df.index:","        df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())","        #    print(x,'              ',numerize.numerize(np.float32(df['Volume'].loc[x]).item()))","        #    df['Volume']=df.loc[x]","","","        print(df)","","        df2=df[['datea','daya','timea','Volume']]","        #print(df2.head(4))","        df2a=df[['datea','daya','timea','Close']]","        df2a['Close']=df2a['Close'].round(2)","","        print('\\n','     ',g.upper(),'                   ','\\n')","        df3=df2.pivot(index=['datea','daya'], columns='timea', values='Volume')","        print(df3)","","","","        print('\\n','     ',g.upper(),'                   ','\\n')","        df3a=df2a.pivot(index=['datea','daya'], columns='timea', values='Close')","        print(df3a)","#############################################################################################################################        ","","",""],"id":2}]]},"ace":{"folds":[],"scrolltop":6577.5,"scrollleft":0,"selection":{"start":{"row":308,"column":0},"end":{"row":308,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":296,"state":"qstring3","mode":"ace/mode/python"}},"timestamp":1624744312828,"hash":"9f4fb52d925544dbe2dcb9e8fa35291b64b12eb7"}