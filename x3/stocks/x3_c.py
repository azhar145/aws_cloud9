def t (g, strike1a, strike2a, perda, intervla):
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
    pd.options.display.max_columns=26
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)



    #g='F'
    perd=perda
    intervl=intervla

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

#    g=input("Enter Ticker :")
#    g = tickaa
    #perd=input("Enter no of days '5d','2d','1d' :")
    #intervl=input("Enter mins '5m','1m' :")


    #df=pd.DataFrame()
    #Interval required 5 minutes
    data = yf.download(g, period=perd, interval=intervl)

    df=pd.DataFrame(data)
    #print(df.tail(5))
    df.reset_index(drop=False,inplace=True)
    #df.set_index()
    #print(df.shape[0],'   ','\n\n',df.tail(5))

    #print(df.tail(6))
    df['green']=''
    df['greenby']=''
#    print(df.shape)
    for x in df.index:
        if df['Close'].loc[x]-df['Open'].loc[x] > 0:
            df['green'].loc[x]='Green'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#            print(x,'  ','Green','  ',df['ns'].loc[x])
        else:
            df['green'].loc[x]='Red'
            df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]
#            print(x,'  ','Red', '  ',df['ns'].loc[x])

  #  sys.exit()
#    print("jjjjjjj")
#    print(df.shape[0])
#    print('\n','*** ttt ******','\n')
#    print(df.tail(23))
#    print('\n\n')
#    print(df.columns,'    ', df.columns.get_loc("n"))
 #   print('Index(['Datetime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'bar', 'G_lower', 'G_Higher']')
    
#    df=df[list('Datetime', 'Open', 'High', 'Low', 'Close','Volume','bar', 'G_lower', 'G_Higher')]
#    print(df.tail(300))

    dp=pd.DataFrame()
#    print('john j')
   
    
#    print('\n\n')
#    print("john jay df, addded 2 columns green  and geenby")
#    print(df.tail(22))
#    print('\n\n')
#    print(df.columns)
#    print('test','\n\n',df.columns.get_loc('Open'))
#    print('\n\n')
 #   sys.exit()

#    print('john jay kaku   ',df.shape,'   ',df.columns)


#    print(df.column.get_loc('
   
 #   k2=0
 #   for y in df.columns:
 #      print(k2,'   ',y)
 #      k2=k2+1


    for x in range(df.shape[0]):
      #  dp=dp.append(df.iloc[x,[0,1,4,6,2,3,7,8]])
        dp=dp.append(df.iloc[x,[0,4,6,7,8,1,2,3,5]])

    #    dp[x]=pd.DataFrame([df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000])
        #dp=pd.DataFrame([df.iloc[x,0],df.iloc[x,5]])
    #  print(df.iloc[x,-1],df.iloc[x,5],df.iloc[x,6]/1000)
#    print('\n\n\n')
    #print(dp)
    dp=pd.DataFrame(dp)
#    dp.columns=['Datetime','close','Vol','green','greenby','Open','High','Low','Adj Close']
#    dp.columns=['Price','n','close','Vol','High','Low','green','greenby','Open']
    dp['Close']=dp['Close'].round(2)
#    print('\n\n','pppp',dp.columns,'\n\n')
#print(dp)

    dp['Close']=dp['Close'].round(1)
#    dp['Vol']=dp['Vol']
#    dp['Vol']=dp['Vol'].round(3) 

    d=[] ; m1=[];m2=[];m3=[]
    strike1=int(strike1a)
    strike2=int(strike2a)

 #   print('dp open  ', dp['Open'])
#    print("joji")
#    sys.exit()
    


    for x in range(dp.shape[0]):
        d.append(g)
        m1.append(strike1)
        m2.append(strike2)

    df4=pd.DataFrame([d,m1,m2])
    #print(df4)

    df4=df4.T
#    print(df4)
#    sys.exit()

    df4.columns=['Ticker','strike1','strike2']
#    print("hhhhhhhhh888888888")
#    print(df4.shape,'    ',dp.shape,'   bbbb dp shape','    ',dp.shape)



 #   sys.exit()
    df3=pd.concat([df4,dp],axis=1)
#    print(df3.head(4))
#df3=df3.T
#    sys.exit()
    df3['(from_strike1)']=df3['strike1']-df3['Close']
#    print(df3.head(4))
#    sys.exit()
    if 'd' in perda:
        df3['x']=df3['Datetime'].dt.time
        df3['d']=df3['Datetime'].dt.day_name()
        df3['u']=df3['Datetime'].dt.date
    else:
        df3['x']='-'
        df3['d']=df3['Date'].dt.day_name()
        df3['u']=df3['Date'].dt.date
#    sys.exit()

#    del df3['n']
 #   del df3['close']
    df3['p_Price']=df3['Close'].shift(1)
    df3['price_delta']=-1*(df3['p_Price']-df3['Close'])
    df3['price_delta']=df3['price_delta'].round(3)
    df3['p_Vol']=df3['Volume'].shift(1)
    df3['vol_delta']=-1*(df3['p_Vol']-df3['Volume'])
    df3['vol_delta']=df3['vol_delta'].round(3)




 #   print('kaku')
 #   print('\n\n\n')
 #   print('df3_columnsbbbbbbbbbb  ',df3.columns)
 #   print('\n\n\n')
#    df3a=df3.loc['x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta']

 #   df3.columns=[['x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta']]

 #   df3=df3[list('x','d','u','Ticker','Price', 'Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta')]
    print(df3.columns)




#    df3=df3[['Ticker', 'strike1', 'strike2', 'Adj Close', 'Close', 'Datetime', 'High', 'Low', 'Open', 'Volume', 'green', 'greenby',
#        '(from_strike1)', 'x', 'd', 'u', 'p_Price', 'price_delta', 'p_Vol', 'vol_delta']]

#    df3=df3[['x','d','u','Ticker', 'price_delta','Close', 'Volume','green','greenby','strike1', 'strike2', 'Adj Close', 'Datetime', 'High'
#        , 'Low', 'Open', '(from_strike1)', 'p_Price', 'p_Vol', 'vol_delta']]

#    df3=df3[['x','d','u','Ticker', 'price_delta','Close', 'Volume','green','greenby','strike1', 'strike2', 'Adj Close', 'Datetime', 'High'        , 'Low', 'Open', '(from_strike1)', 'p_Price', 'p_Vol', 'vol_delta']]

    df3=df3[['x','d','u','Ticker', 'price_delta','Close', 'Volume','green','greenby','strike1' ]]

#    df3=df3[['d','u','x','Ticker','Price','Vol','green', 'greenby','price_delta', 'p_Vol', 'vol_delta','Low','High','Close']]
#    print('mmmm')


    if '1m' in intervl:

        print("\033[1;32;40m Bright Green \n")
        for x in df3.index:
                df3['Volume'].loc[x]=numerize.numerize(np.float32(df3['Volume'].loc[x]).item())
        print(df3.tail(4))
      #  if df3['greenby']>0:
      #      print("\033[1;32;40m Bright Green \n")

    elif '60m' in intervl:
        for x in df3.index:
                df3['Volume'].loc[x]=numerize.numerize(np.float32(df3['Volume'].loc[x]).item())
        print(df3.tail(34))
    else:
        for x in df3.index:
                df3['Volume'].loc[x]=numerize.numerize(np.float32(df3['Volume'].loc[x]).item())
        print(df3)
  #  print(df3.tail(34))
    return(df3)





#tick,strike1a,strike2a,perda,intervla
#t ('^NDX',13400,13410,'5d','1d')
#t ('TSLA',627,635,'5d','1d')

###################################################################
###################################################################
xx='^NDX'
#xx='BIIB'
g=input("Enter Ticker :").upper()
#xx=input("Enter ticker: ")
strike_1=280
strike_2=290
####################################################################
###################################################################
#t ('^NDX',13420,13430,'1d','1m')
#t ('^NDX',13400,13410,'1d','60m')
print('\n\n\n')
print('                           ',g,'                         ')
print('\n')
t (g,strike_1,strike_2,'1mo','1d')
print('-- daily ----')
print('\n\n')

t (g,strike_1,strike_2,'3d','60m')
print('-- hourly ---')
print('\n\n')
t (g,strike_1,strike_2,'3d','1m')
print('-- last 2 hours (evey minute)  --')

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