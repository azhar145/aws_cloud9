from yahoo_fin import options 
import pandas as pd
from yahoo_fin import stock_info as f
import textwrap 
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import numpy as np 
from numerize import numerize 
import yfinance as yf
import time
from datetime import datetime 
import datetime as d
import calendar as b


pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
#pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)

from yahoo_fin import options as o
#print(help(o))


ticker='^ndx'
u=o.get_expiration_dates(ticker)
#print('Option expiry : ',u[0])
gg=u[0]
calls=o.get_calls(ticker, date=gg)



df = yf.download(tickers=ticker, period = '5d', interval = '1d')
c=df['Close'].tail(1)
c=c.round(2)
print(ticker,' = ',c)
print('Option expiry : ',u[0])
print('\n\n','**************************************************','\n\n') 


#o.get_puts(ticker, date=None)
#o.get_options_chain(ticker, date=None, raw=True, headers={'User-agent': 'Mozilla/5.0'})
print(calls)

calls['stocka']=int(c)
calls['u']=''
calls['m']=''
calls=pd.DataFrame(calls)
for x in calls.index:
#    calls['stocka'].loc[x]==int(c)
    calls['Volume'].loc[x]=calls['Volume'].loc[x].replace('-','0')
#    calls['u'].loc[x]=calls['u'].loc[x].replace('-','0')
    calls['u'].loc[x]=calls['Volume'].loc[x]
    if (calls['Strike'].loc[x] > int(c)):
        calls['m'].loc[x]="Out"
    else:
        calls['m'].loc[x]="In"




cc=calls.sort_values(by=['Volume'],ascending=False)
#print(cc)

g=pd.DataFrame()
for x in cc.index:
    if int(cc['Volume'].loc[x]) > int(0):
        #`print(x)

        g[x].loc[x].append(cc.loc[x])


print(g)        
