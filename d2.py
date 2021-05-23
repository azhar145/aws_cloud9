import pandas as pd
pd.options.display.max_rows=9999
pd.options.display.max_columns=15
pd.set_option("display.max_columns", 100)
pd.set_option('display.width', 1000)
tickers_list=input("Enter ticker: ").upper()


#tickers_list = ['NDX']
##########################################################################################################

import numpy,datetime
import sys
import calendar
# Fetch the data
import yfinance as yf
import textwrap
wrapper = textwrap.TextWrapper(width=100)
import yahoo_fin
#from yahoo_fin import stock_info
#from yahoo_fin.stock_info import get_data
#import yahoo_fin.stock_info 
#from yahoo_fin.stock_info import get_data




data = yf.download(tickers_list,'2020-10-1')[['Open','Close','Volume']]
df=pd.DataFrame(data)
#print(df.head)
df.reset_index(drop=False,inplace=True)
#df.style.set_properties(subset=['text'], **{'width': '300px'})


d1=[]
for x in range(df.shape[0]):
    d1[x]=d1.append("X")

df['ticker']=tickers_list
#df['ticker']=tickers_list[0]
df['up_down']=df['Close']-df['Open']
#df['z']=calendar.day_name[df['Date'].weekday()]
df['day']=df['Date'].dt.day_name()
df['Datea']=df['Date'].dt.date


#df=df.iloc[1:]
#tt=df.shape[0]+1
#df.loc[len(df)]=['8','8','5','ttt','0']

#df.reset_index(drop=False,inplace=True)
#print(df.tail(4))

#df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
#df['Datea']=pd.to_datetime(df['Date'])

#df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')
#print(df['Date'])
#ts = pd.to_datetime(pd.Series(str(df['Date']))) 
#print(ts)
#d = ts.strftime('%m.%d')
#b1=d
#print(b1)
#b1=(pd.Series(df['Date']))
b1=df['Datea']
b2=df['ticker']
b3=df['up_down'].astype(int)
b4=df['Open'].astype(int)
b5=df['Close'].astype(int)
#b6=df['Date'].dt.weekday_name
b6=df['day']
#b6['p']=b6['Date'].split()[1]
b7=df['Volume']
#print(b1,'******',b6)
'''
print(type(pd.Series(df['Date'].dtype)))
print(type(df['ticker']))
print(type(df['up_down'].astype(int)))
print(type(df['Open'].astype(int)))
print(type(df['Close'].astype(int)))
'''
aa=pd.concat([b1,b6,b2,b3,b4,b5,b7],axis=1)
aa.loc[len(aa)]=['','','8','8','5','ttt','0']
aa=aa[1:]
#print(aa.columns)

#print(aa)
#aa=pd.concat(pd.Series(df['Date'].dtype),df['ticker'])
#aa=pd.concat(([pd.Series(df['Date'].dtype)),df['Date'].dt.weekday_name,df['ticker'],df['up_down'].astype(int),df['Open'].astype(int),df['Close'].astype(int)])
#print(aa)
#######################################################################################################






#bb2=df['Close'].astype(int)
bb2=df
bb=bb2.iloc[0:]
#bb2.drop(bb2.index[:0],inplace=True)
bb.reset_index(inplace=True,drop=True)
#print(bb.head(3))
#bb.append([['','','test','','','','']],ignore_index=True)
#bb=bb.T
#bb[rowsa]=["z","z","dd","2","2","2","2"]
#bb=bb.T
#print(bb.index)
##bb=pd.DataFrame([['','','mmm','','','','']],columns=['Date','Date','ticker','up_down','Open','Close','Volume'])
#bb.append("",'test','x','','','',''])
#print(bb)
bb=bb['Close'].astype(int)
#print(bb)
#print(aa.head(4))

#gg=pd.concat([aa,bb],axis=1)
#gg=pd.concat([aa[1:],bb['Close'][0:]],axis=1)
#print(gg)        







#print(aa.head(4),bb[1:].head(4))
#aa=aa[1:]
aa.reset_index(inplace=True,drop=True)

cc=pd.merge(aa,bb, left_index=True, right_index=True)
#cc=bb.join(aa)
#cc=pd.merge([aa,bb],right,how='inner',on=None,left_index=True,right_index=False, left_on=None, right_on=None)

cc['nxtday_delta']=cc['Open'].astype(int)-cc['Close_y'].astype(int)
cc.drop(cc.index[cc.shape[0]-1],inplace=True) 
cc['cl_cl_delta']=cc['Close_x'].astype(int)-cc["Close_y"].astype(int)

p=10
#cc=cc.query('abs(nxtday_delta) < abs(20)' and 'abs(cl_cl_delta) < abs(20)' and 'abs(up_down) < abs(20)')
#cc=cc.query('abs(nxtday_delta)  < 300')
#cc=cc.query('abs(up_down)  < 300')
#cc=cc.query('abs(cl_cl_delta)  < 300')

print(cc)
###########################################################
dd=cc.tail(14)
print(dd)
Next_day_delta_close_to_open=abs(dd['nxtday_delta']).sort_values(axis=0, ascending=True)
print('Next_day_delta_close_to_open (yesterday close,todays open delta','\n')
print('Mean ',Next_day_delta_close_to_open.mean())
print('Max  ',Next_day_delta_close_to_open.max())
print('min  ',Next_day_delta_close_to_open.min())
print('count ',Next_day_delta_close_to_open.count())  
##########################################################
daily_up_down=abs(dd['up_down']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',daily_up_down.mean())
print('Max ',daily_up_down.max())
print('min ',daily_up_down.min())
print('count ',daily_up_down.count())
print('###########################################################################################################') 
print('cl_cl_delta')
#print(b2,'   ',b1,'   ',abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
cl_cl_delta=abs(dd['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',cl_cl_delta.mean())
print('Max ',cl_cl_delta.max())
print('min ',cl_cl_delta.min())
print('count ',cl_cl_delta.count())
print('###########################################################################################################') 
########################################################################################################################
########################################################################################################################


dedented_text = textwrap.dedent(str(cc))
#print(cc.query=('cl_cl_delta' < 300))
print("marker")

 #print(cc)
#print(dedented_text)
 #print(df)
 
print('\n\n\n')
#print(abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
print('###########################################################################################################')
print('Next_day_delta_close_to_open (yesterday close, todays open delta')
#print(pd.concat(b2,abs(cc['nxtday_delta']),axis=0))
#print(type(b2))
#b2=b2.astype('Int64')
#Next_day_delta_close_to_open=Next_day_delta_close_to_open.astype('Int64')
Next_day_delta_close_to_open=abs(cc['nxtday_delta']).sort_values(axis=0, ascending=True)
#print(type(Next_day_delta_close_to_open))
print('Next_day_delta_close_to_open (yesterday close,todays open delta','\n')
print('Mean ',Next_day_delta_close_to_open.mean())
print('Max  ',Next_day_delta_close_to_open.max())
print('min  ',Next_day_delta_close_to_open.min())
print('count ',Next_day_delta_close_to_open.count())  
print('###########################################################################################################')   
print('\n\n\n')

print('up_down (same day)')
#print(b2,'   ',b1,'    ', abs(cc['up_down']).sort_values(axis=0, ascending=True, inplace=False))
daily_up_down=abs(cc['up_down']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',daily_up_down.mean())
print('Max ',daily_up_down.max())
print('min ',daily_up_down.min())
print('count ',daily_up_down.count())
print('###########################################################################################################')  
print('\n\n\n')
print('cl_cl_delta')
#print(b2,'   ',b1,'   ',abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False))
cl_cl_delta=abs(cc['cl_cl_delta']).sort_values(axis=0, ascending=True, inplace=False)
print('\n','daily_up_down (same day): ','\n')
print('Mean ',cl_cl_delta.mean())
print('Max ',cl_cl_delta.max())
print('min ',cl_cl_delta.min())
print('count ',cl_cl_delta.count())
print('###########################################################################################################')  
#html = cc.to_html()
#print(html)
#print(cc[:cc.shape[0]-1i
