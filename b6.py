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




pd.options.display.max_rows=9999
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

df=pd.DataFrame(data)
df.reset_index(drop=False,inplace=True)
df['ticker']=g
#df['Open']=df['Open']
df['5day']=df['Close']-df['Close'].shift(5)
df['5day_gain']=df['5day'].round(2)
df['1day']=df['Close']-df['Close'].shift(1)
df['1day_gain']=df['1day'].round(2)

#print(df.columns)
mm=input('Enter no of days / will also compute minimum low/high for last no of days: ')

df5=df.tail(int(mm))
df5_low = df5['Low'].min()
df5_high=df5['High'].max()

print('\n\n**************************************************************************************************')

print('\n',"Today's/yesterday close",df['Close'].tail(1))
print(mm,'days low=',df5_low.round(2))
print(mm,'days High=',df5_high.round(2))
print('Low-High gap with  ',mm,' days = ',(df5_high.round(2)-df5_low.round(2)).round(2))
print('\n',"Today's/yesterday close",df['Close'].tail(1))
print('Low Yesterday close, how far from ',mm,' days low: ',df['Close'].tail(1)-df5_low.round(2))
print('High Yesterday close, how far from ',mm,' days high: ',df['Close'].tail(1)-df5_high.round(2))
print('*******************************************************************************************************','\n\n')
#sleep(5)

for x in df.index:
            df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())




df2=df

df['Opena']=''
df['green']=''
df['greenby']=''

for x in df.index:
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:



        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:

        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#print(df)
#print('\n',' 1-day    ',g,'\n')

df2['direct']=''
df2['down']=''
df2['a_Close']=''
df2['a_High']=''
df2['a_Low']=''
df2['a_Open']=''
df2['HA']=''
df2['Opena']=''
df2['green']=''
df2['greenby']=''


for x in df.index:

    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

   # df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
   # df2['a_High']=max(df['High'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Low']=min(df['Low'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
#    df2['a_Open'].loc[x]=1/2*(df2['Open'].loc[x].shift(1)+df2['Close'].loc[x].shift(1))
   # df2['cx'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x] 
    
    df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
    df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['High'].loc[x]=df2['High'].loc[x]
    df2['Low'].loc[x]=df2['Low'].loc[x]
    df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
    df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
 #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]



#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
    if df2['HA'].loc[x] > 0:    
        df2['direct'].loc[x]='HA_Green'
    elif df2['HA'].loc[x] < 0:
        df2['direct'].loc[x]='HA_Red'

df2['x1']=0
df2['x2']=0
#df2['x1']=input("Enter break1 ")
#df2['x2']=input("Enter break2 ")
df2['x1_d']=''
df2['x2_d']=''

u1=5
u2=7

for x in df2.index:
    df2['x1'].loc[x]=u1
    df2['x2'].loc[x]=u2
    df2['x1_d'].loc[x]=(df2['Close'].loc[x]-df2['x1'].loc[x])
    df2['x2_d'].loc[x]=(df2['Close'].loc[x]-df2['x2'].loc[x])


    df2['greenby'].loc[x]=df2['greenby'].loc[x].round(2)
    df2['HA'].loc[x]=df2['HA'].loc[x].round(2)
    df2['a_High'].loc[x]=df2['a_High'].loc[x].round(2)
    df2['a_Low'].loc[x]=df2['a_Low'].loc[x].round(2)
    df2['a_Close'].loc[x]=df2['a_Close'].loc[x].round(2)
    df2['a_Open'].loc[x]=df2['a_Open'].loc[x].round(2)

#for x in df2.index:
#        df2['x1_d'].loc[x]=(str(df2['Close'].loc[x])-str(df2['x1'].loc[x]))
#        df2['x2_d'].loc[x]=(df2['Close'].loc[x]-df2['x2'].loc[x])

#df2=df2[['Date','Volume', 'ticker', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]

df2=df2[['ticker','Date','Volume','Close', 'direct', 'HA','green', 'greenby','Opena','a_High','a_Low', 'High', 'a_Close', 'a_Open','1day_gain','5day_gain',
    'x1','x2','x1_d','x2_d']]




#df2['greenby']=df2['greenby'].round(2)
df2['Close']=df2['Close'].round(2)
#df2['a_Open']=df2['a_Open'].round(2)
#df2['a_Close']=df2['a_Close'].round(2)
df2['High']=df2['High'].round(2)
#df2['a_High']=df2['a_High'].round(2)


print(df2.tail(30))

print('\n','=================> 1- day    ',g,'\n')

########################################################################################################################################
########################################################## Hourly ##################################################

#perda='1d'
perda=input("Enter no of days (only enter number do not enter days): ")
perda=perda+'d'
#intervla='60m'
intervla=input("Enter minutes 5min, 10min, 15 min, 60min (only enter number, do not enter min): ")
intervla=intervla+'m'

#g=input("Enter ticker: ")
perd=perda
intervl=intervla

# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]



#df=pd.DataFrame()
#Interval required 5 minutes
data = yf.download(g, period=perd, interval=intervl,prepost = True)

df=pd.DataFrame(data)
df.reset_index(drop=False,inplace=True)
df['ticker']=g

df['x']=df['Datetime'].dt.time
df['d']=df['Datetime'].dt.day_name()
df['u']=df['Datetime'].dt.date



#df['Open']=df['Open']


df2=df


#print('\n',df2,'\n')
df['Opena']=''
df['green']=''
df['greenby']=''

for x in df.index:
    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:



        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
                                        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:

        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#print(df)
#print('\n',' 1-day    ',g,'\n')

df2['direct']=''
df2['down']=''
df2['a_Close']=''
df2['a_High']=''
df2['a_Low']=''
df2['a_Open']=''
df2['HA']=''
df2['Opena']=''
df2['green']=''
df2['greenby']=''


for x in df.index:

    df['Opena'].loc[x]=int(df['Open'].loc[x])
    if df['Close'].loc[x]-df['Open'].loc[x] > 0:
        df['green'].loc[x]='Green'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
        #            print(x,'  ','Green','  ',df['ns'].loc[x])
    else:
        df['green'].loc[x]='Red'
        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]

   # df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
   # df2['a_High']=max(df['High'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Low']=min(df['Low'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])
   # df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
#    df2['a_Open'].loc[x]=1/2*(df2['Open'].loc[x].shift(1)+df2['Close'].loc[x].shift(1))
   # df2['cx'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x] 
    
    df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])
    df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['High'].loc[x]=df2['High'].loc[x]
    df2['Low'].loc[x]=df2['Low'].loc[x]
    df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
    df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])
 #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])
    df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]



#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:
    if df2['HA'].loc[x] > 0:    
        df2['direct'].loc[x]='HA_Green'
    elif df2['HA'].loc[x] < 0:
        df2['direct'].loc[x]='HA_Red'


for x in df2.index:
    df2['greenby'].loc[x]=df2['greenby'].loc[x].round(2)
    df2['HA'].loc[x]=df2['HA'].loc[x].round(2)
    df2['a_High'].loc[x]=df2['a_High'].loc[x].round(2)
    df2['a_Low'].loc[x]=df2['a_Low'].loc[x].round(2)
    df2['a_Close'].loc[x]=df2['a_Close'].loc[x].round(2)
    df2['a_Open'].loc[x]=df2['a_Open'].loc[x].round(2)

#df2=df2[['x','d','u','Volume', 'ticker', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]
df2=df2[['ticker','x','d','u','Volume','Close', 'direct', 'HA','green', 'greenby','Opena','a_High','a_Low', 'High', 'a_Close', 'a_Open']]




#df2['greenby']=df2['greenby'].round(2)
df2['Close']=df2['Close'].round(2)
#df2['a_Open']=df2['a_Open'].round(2)
#df2['a_Close']=df2['a_Close'].round(2)
df2['High']=df2['High'].round(2)
#df2['a_High']=df2['a_High'].round(2)


#print(df2.tail(215))
#print(df2.columns)

#df3=df2[['ticker', 'x', 'd', 'u', 'Volume', 'Close', 'direct', 'HA', 'green', 'greenby']]
df3=df2[['ticker', 'x', 'd', 'u', 'Volume', 'Close', 'direct', 'HA']]
df3['Volume_delta_1']=df3['Volume']-df3['Volume'].shift(1)
df3['Close_delta_1']=df3['Close']-df3['Close'].shift(1)

for x in df3.index:
    df3['Volume'].loc[x]=numerize.numerize(np.float32(df3['Volume'].loc[x]).item())
#    df3['Volume_delta_1'].loc[x]=numerize.numerize(np.float32(df3['Volume_delta_1'].loc[x]).item())


print(df3.tail(30000))


print('\n','=========>  1- min    ',g,'\n')

########################################################################################################################################


print('\n\n')

#ticker=input("Enter ticker: ")

ticker=g

#ticker='^ndx'
x="calls"
y="puts"

##########################################################################################################
print('\n\n')
print(" haha more to the story")
print('Ticker -----> ',f.get_quote_data(ticker)['symbol'],'           Industry: ',yf.Ticker(ticker).info['industry'])   
print('Shortname -----> ',f.get_quote_data(ticker)['shortName'])
print('stock live  price ------ >  ',(f.get_live_price(ticker)).round(2),'      ', 'Prev Yesterday Cloe :',yf.Ticker(ticker).info['regularMarketPreviousClose'],
       '   Change:',(f.get_live_price(ticker)-yf.Ticker(ticker).info['regularMarketPreviousClose']))
#print('stock postmarket price ------ >  ',yf.Ticker(ticker).info['postMarketPrice'])
print('Day Low ---->   ',(yf.Ticker(ticker).info['dayLow']),'    Day High ',(yf.Ticker(ticker).info['dayHigh']))

#print('stock pre market price ---> ',f.get_premarket_price(ticker).round(2))
#print('stock post market price ----> ',f.get_postmarket_price(ticker))
print('stock market status ---> ',f.get_market_status())
print('dd regularMarketVolume----> ', (f.get_quote_data(ticker)['regularMarketVolume']/1000000), 'Million')
print('dd averageDailyVolume10Day----> ', f.get_quote_data(ticker)['averageDailyVolume10Day']/1000000, 'Million')
print('dd averageDailyVolume3Mont ----> ', f.get_quote_data(ticker)['averageDailyVolume3Month']/1000000, 'Million')
#print('dd averageAnalystRating ----> **************** ', f.get_quote_data(ticker)['averageAnalystRating'])

#print('dd averageAnalystRating ----> **************** ', f.get_quote_data(ticker)['averageAnalystRating'])



#print('EarningsQuarterlyGrowth---> ',yf.Ticker(ticker).info['earningsQuarterlyGrowth'])

#print(si.get_next_earnings_date(ticker))

#print(si.get_earnings(ticker))
#earnings_in_week = si.get_earnings_in_date_range("07/16/2021", "07/23/2021")
#print(earnings_in_week)
#print(help(f))

print('\n\n')
#print(help(si))
print(yf.Ticker(ticker).info['longBusinessSummary'])
#for x in yf.Ticker(ticker).info:
#    print(x)
#    print('\n')

#print(gg.getQuotes('AAPL'))

print('\n\n**************************************************************************************************')
print('\n\n','****************************************************************************************************','\n\n')
print(' Low / Put  or High / Call value for Call/Put selection based on previous ',mm, ' days' )
print('\n\n')
print('**************************************************************************************************************')
print('\n\n')
print('\n',"Today's/yesterday close",df['Close'].tail(1))
print(mm,'days low=',df5_low.round(2))
print(mm,'days High=',df5_high.round(2))
print('Low-High gap with  ',mm,' days = ',(df5_high.round(2)-df5_low.round(2)).round(2))
print('\n',"Today's/yesterday close",df['Close'].tail(1))
print('Low Yesterday close, how far from ',mm,' days low: ',df['Close'].tail(1)-df5_low.round(2))
print('High Yesterday close, how far from ',mm,' days high: ',df['Close'].tail(1)-df5_high.round(2))

print('\n')
if not yf.Ticker(ticker).info['earningsGrowth'] is  None:
    print('earningsGrowth :',yf.Ticker(ticker).info['earningsGrowth']*100,' %')
else:
    print('earningsGrowth :',yf.Ticker(ticker).info['earningsGrowth'])

if not yf.Ticker(ticker).info['revenueGrowth'] is None:
    print('revenueGrowth :',yf.Ticker(ticker).info['revenueGrowth']*100,' %')
else:
    print('revenueGrowth :',yf.Ticker(ticker).info['revenueGrowth'])


print('revenueQuarterlyGrowth : ',yf.Ticker(ticker).info['revenueQuarterlyGrowth'])
#print('earningsGrowth :',yf.Ticker(ticker).info['earningsGrowth']*100,' %')
#print('revenueGrowth :',yf.Ticker(ticker).info['revenueGrowth']*100,' %')

# df['Volume'].loc[x]=numerize.numerize(np.float32(df['Volume'].loc[x]).item())
t3=yf.Ticker(ticker).info['totalDebt']
t3a=numerize.numerize(np.float32(t3).item())
print('totalDebt :',t3a)


t3=yf.Ticker(ticker).info['totalRevenue']
t3a=numerize.numerize(np.float32(t3).item())
print('totalRevenue :',t3a)
#print('totalRevenue :',yf.Ticker(ticker).info['totalRevenue'])



t3=yf.Ticker(ticker).info['grossProfits']
t3a=numerize.numerize(np.float32(t3).item())
print('grossProfits :',t3a)
#print('grossProfits: ',yf.Ticker(ticker).info['grossProfits'])



print('profitMargins: ',yf.Ticker(ticker).info['profitMargins']*100,' %')
print('grossMargins: ',yf.Ticker(ticker).info['grossMargins']*100,' %')



t3=yf.Ticker(ticker).info['operatingCashflow']
t3a=numerize.numerize(np.float32(t3).item())
print('operatingCashflow :',t3a)
#print('operatingCashflow: ',yf.Ticker(ticker).info['operatingCashflow'])





t3=yf.Ticker(ticker).info['fullTimeEmployees']
t3a=numerize.numerize(np.float32(t3).item())
print('fullTimeEmployees :',t3a)

#print('fullTimeEmployees: ',yf.Ticker(ticker).info['fullTimeEmployees'])

print('*******************************************************************************************************','\n\n')



#sleep(5)


'''


earningsQuarterlyGrowth
revenueQuarterlyGrowth
earningsGrowth
revenueGrowth
totalDebt
totalRevenue
totalCatotalRevenuetotalRevenueshPerShare
revenuePerShare
grossProfits

fullTimeEmployees
profitMargins
grossMargins
operatingCashflow


freeCashflow

numberOfAnalystOpinions
targetMeanPrice









print('dd Next Earning Date --------> ',f.get_next_earnings_date(ticker))
print('dd Days range ------> ',f.get_quote_data(ticker)['regularMarketDayRange'])
############# below is long
print('dd quote table -----> ',f.get_quote_data(ticker))
m=f.get_holders(ticker)
print('dd holders ----> ',m)
print('\n\n\n')
#########################################################################
#########################################################################
print("Volume up or down - (current volume vs 10 days volume),(current volume vs last 3 months)")

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) < 0:
    print('22 ----> 10 days (volume low yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) >  0:
        print('22 ----> 10 days (volume high yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) < 0:
        print('22 ----> 3 mnths (volume low yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) >  0:
                    print('22 ----> 3 mnths (volume high yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))
####################################################
################################################
print('\n')
print('23 ----> ',f.get_stats(ticker))
print('\n')
print('24 ----> ',f.get_stats_valuation(ticker))
print('\n')
print('Analysts ---->  ',f.get_analysts_info(ticker))
print(f.info)
print('\n\n')
###########################################################################################################
'''

