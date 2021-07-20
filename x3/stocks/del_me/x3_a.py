def t (tickaa, strike1a, strike2a, perda, intervla):
    import numpy as np
    import pandas as pd
    import numpy,datetime
    import sys
    import calendar
    from datetime import time


    #Data Source
    import yfinance as yf

    #Data viz
    import plotly.graph_objs as go

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=26
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)



    #g='F'
    perd=perda
    intervl=intervla

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    #g=input("Enter Ticker :")
    g = tickaa
    #perd=input("Enter no of days '5d','2d','1d' :")
    #intervl=input("Enter mins '5m','1m' :")


    #df=pd.DataFrame()
    #Interval required 5 minutes
    data = yf.download(tickaa, period=perd, interval=intervl)

    df=pd.DataFrame(data)
    #print(df.tail(5))
    df.reset_index(drop=False,inplace=True)
    #df.set_index()
    #print(df.shape[0],'   ','\n\n',df.tail(5))

    #print(df.tail(6))
    df['n']=''
    df['ns']=''
    print(df.shape)
    for x in df.index:
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:
            df['n'].loc[x]='Green'
            df['ns'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:
            df['n'].loc[x]='Red'
            df['ns'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
            print(x,'  ','Red', '  ',df['ns'].loc[x])
#        print(x,df['Close'].loc[x]-df['Open'].loc[x])
 #       df['Close'].loc[x]
##    df['bar']=df['Close']-df['Open']

##    if df['Close']-df['Open'] > 0:
##        df['Green']='Greeb'
##    else:
##        df['Green']='Red'


  #  sys.exit()
    print("jjjjjjj")
 #   df['bar_length']=df['Close']-df['Open']



 #   df['bar']=df['bar'].round(3)
    
 #   df['G_lower']=df['Low']-df['Open']
 #   df['G_lower']=df['G_lower'].round(3)

 #   df['G_Higher']=df['High']-df['Close']
 #   df['G_Higher']=df['G_Higher'].round(3)
 #   sys.exit()

#    df['mm']=[]
    print(df.shape[0])
#    for x in range(df.shape[0]+1):
#        if df['G_lower'] < 0:
#            df['mm'].iloc[x].append('green')
#        else:
#            df['mm'].iloc[x].append('red')
 #           df['dd'].append('Green')
             

#       else:
 #           df['dd'].append('Red')
  #      df['sff']=df.iloc[x,8]
 #       print(df.iloc[x,3])

#   if df['bar'] > 0:
 #       print('jjj')
      #  df['color']='Green'
  #  elif df['bar'] < 0:
 #       df['color']=='Red'
 #   else:
  #      pass


    print('\n','*** ttt ******','\n')
    print(df.tail(23))
    print('\n\n')
    print(df.columns,'    ', df.columns.get_loc("n"))
 #   print('Index(['Datetime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'bar', 'G_lower', 'G_Higher']')
    
#    df=df[list('Datetime', 'Open', 'High', 'Low', 'Close','Volume','bar', 'G_lower', 'G_Higher')]
#    print(df.tail(300))

    dp=pd.DataFrame()
#    print('john j')
#    print(dp.tail(4))
   
    
    print('\n\n')
    print("john jay")
    print(df.tail(22))
    print('\n\n')
    print(df.columns)
    print('test','\n\n',df.columns.get_loc('Open'))
    print('\n\n')
 #   sys.exit()


    for x in range(df.shape[0]):
        dp=dp.append(df.iloc[x,[0,1,4,6,2,3,7,8]])

    #    dp[x]=pd.DataFrame([df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000])
        #dp=pd.DataFrame([df.iloc[x,0],df.iloc[x,5]])
    #  print(df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000)
    print('\n\n\n')
    #print(dp)
    dp=pd.DataFrame(dp)
    dp.columns=['Price','n','close','Vol','High','Low','green','greenby','Open']
    dp['Price']=dp['Price'].round(2)
    print('\n\n','pppp',dp.columns,'\n\n')
#print(dp)

#    dp['n']=dp['n']
    

#    dp['m']=dp['n'].dt.hour()
#    dp['m']=pd.to_datetime(dp['n'],format='%D%M')
#   dp['m']=dp['m'].dt.time



#    dp['na']=datetime.strptime(dp['n'], "%m/%j/%y %H:%M")
  #  dp['na']=dp['n'].dt.hour()
 #   dp['na'] = pd.to_datetime(dp['n'], errors='coerce')
 #   dp['na'] = dp['na'].dt.strftime('%HH:%MM')

  #  dp['na'] = pd.to_datetime(dp['n'], format='%H:%M:%S')
   # df['na'] = df['na'].dt.strftime('%H-%M-%s')
 #   dp['timea'] =dp['na'].dt.strftime('%M')

#    dp['Price']=dp['Price'].round(2)
    dp['close']=dp['close'].round(2)


    dp['Vol']=dp['Vol']/10000
    dp['Vol']=dp['Vol'].round(3) 

    d=[] ; m1=[];m2=[];m3=[]
    strike1=int(strike1a)
    strike2=int(strike2a)

 #   print('dp open  ', dp['Open'])


    for x in range(dp.shape[0]):
        d.append(g)
        m1.append(strike1)
        m2.append(strike2)

    df4=pd.DataFrame([d,m1,m2])
    #print(df4)

    df4=df4.T


    df4.columns=['Ticker','strike1','strike2']



    df3=pd.concat([df4,dp],axis=1)
    #df3=df3.T

    df3['(from_strike1)']=df3['strike1']-df3['close']
    df3['x']=df3['n'].dt.time
    df3['d']=df3['n'].dt.day_name()
    df3['u']=df3['n'].dt.date
    del df3['n']
 #   del df3['close']
    df3['p_Price']=df3['Price'].shift(1)
    df3['price_delta']=-1*(df3['p_Price']-df3['Price'])
    df3['price_delta']=df3['price_delta'].round(3)
    df3['p_Vol']=df3['Vol'].shift(1)
    df3['vol_delta']=-1*(df3['p_Vol']-df3['Vol'])
    df3['vol_delta']=df3['vol_delta'].round(3)
    print('kaku')
    print('\n\n\n')
    print('df3_columnsbbbbbbbbbb  ',df3.columns)
    print('\n\n\n')
#    df3a=df3.loc['x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta']


 #   df3.columns=[['x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta']]

 #   df3=df3[list('x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta')]
    
    df3=df3[['d','u','x','Ticker','Price','Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta','Low','High','close']]
    print('mmmm')
    print(df3.tail(34))
#    print(df3.columns)
    # Index(['Ticker', 'strike1', 'strike2', 'Price', 'Vol', '(from_strike1)', 'x', 'd', 'u', 'p_Price', 'price_delta', 'p_Vol', 'vol_delta']
#    df3x=df3[list('Ticker', 'strike1', 'strike2', 'Price', 'Vol', '(from_strike1)', 'x', 'd', 'u', 'p_Price', 'price_delta', 'p_Vol', 'vol_delta')]
#    print(df3.tail(6))
#    print(df3[['Ticker','Price','Vol','p_Price','p_Vol','price_delta','vol_delta']])
    
#    df3=df3[['u','d','x','Ticker','Price','Vol','p_Price','p_Vol','price_delta','vol_delta','Open','Low','High','Close']]
#    print(df3.tail(2))
#    print('\n',df3['(from_strike1)'].tail(60))
#    print(df3['n'].dt.time)
    return(df3)





#tick,strike1a,strike2a,perda,intervla
#t ('^NDX',13400,13410,'5d','1d')
#t ('TSLA',627,635,'5d','1d')

###################################################################
###################################################################
xx='^NDX'
#xx='BIIB'

#xx=input("Enter ticker: ")
strike_1=280
strike_2=290
####################################################################
###################################################################
#t ('^NDX',13420,13430,'1d','1m')
#t ('^NDX',13400,13410,'1d','60m')
t (xx,strike_1,strike_2,'3d','1m')




'''
print('-----t2---- 1 minute -------------')
print('\n\n')
t (xx,strike_1,strike_2,'3d','5m') 
print('----t3----- 5 minutes -------------')
print('\n\n')
#t ('MELI',1390,1395,'10d','60m')
#t ('ADSK',300,302.5,'1d','60m')
mm=t (xx,strike_1,strike_2,'3d','60m')
print('----t4---- Every hour ------------')
print('\n\n')

mm=t (xx,strike_1,strike_2,'200d','1d')
print('--t5------ Every day-last 10days ------------')
#print('\n',df3['(from_strike1)'].tail(df3.shape[0]))
print('\n\n')


# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

     #perd=input("Enter no of days '5d','2d','1d' :")
     #intervl=input("Enter mins '5m','1m' :")
'''     