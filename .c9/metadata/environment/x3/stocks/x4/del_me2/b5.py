{"filter":false,"title":"b5.py","tooltip":"/x3/stocks/x4/del_me2/b5.py","undoManager":{"mark":55,"position":55,"stack":[[{"start":{"row":122,"column":0},"end":{"row":231,"column":0},"action":"insert","lines":["########################################################## daily ##################################################","","perda='55d'","intervla='1d'","","","g=input(\"Enter ticker: \")","perd=perda","intervl=intervla","","# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]","","","","#df=pd.DataFrame()","#Interval required 5 minutes","data = yf.download(g, period=perd, interval=intervl,prepost = True)","","df=pd.DataFrame(data)","df.reset_index(drop=False,inplace=True)","df['ticker']=g","#df['Open']=df['Open']","","","df2=df","","df['Opena']=''","df['green']=''","df['greenby']=''","","for x in df.index:","    df['Opena'].loc[x]=int(df['Open'].loc[x])","    if df['Close'].loc[x]-df['Open'].loc[x] > 0:","","","","        df['green'].loc[x]='Green'","        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]","                                        #            print(x,'  ','Green','  ',df['ns'].loc[x])","    else:","","        df['green'].loc[x]='Red'","        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]","#print(df)","#print('\\n',' 1-day    ',g,'\\n')","","df2['direct']=''","df2['down']=''","df2['a_Close']=''","df2['a_High']=''","df2['a_Low']=''","df2['a_Open']=''","df2['HA']=''","df2['Opena']=''","df2['green']=''","df2['greenby']=''","","","for x in df.index:","","    df['Opena'].loc[x]=int(df['Open'].loc[x])","    if df['Close'].loc[x]-df['Open'].loc[x] > 0:","        df['green'].loc[x]='Green'","        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]","        #            print(x,'  ','Green','  ',df['ns'].loc[x])","    else:","        df['green'].loc[x]='Red'","        df['greenby'].loc[x]=df['Close'].loc[x]-df['Open'].loc[x]","","   # df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])","   # df2['a_High']=max(df['High'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])","   # df2['a_Low']=min(df['Low'].loc[x],df2['Open'].loc[x],df2['Close'].loc[x])","   # df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])","#    df2['a_Open'].loc[x]=1/2*(df2['Open'].loc[x].shift(1)+df2['Close'].loc[x].shift(1))","   # df2['cx'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x] ","    ","    df2['a_Close'].loc[x]=1/4*(df['Open'].loc[x]+df2['High'].loc[x]+df2['Low'].loc[x]+df['Close'].loc[x])","    df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])","    df2['High'].loc[x]=df2['High'].loc[x]","    df2['Low'].loc[x]=df2['Low'].loc[x]","    df2['a_High'].loc[x]=max(df['High'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])","    df2['a_Low'].loc[x]=min(df['Low'].loc[x],df2['a_Open'].loc[x],df2['a_Close'].loc[x])"," #   df2['a_Open'].loc[x]=1/2*(df2['Open'].shift(1).loc[x]+df2['Close'].shift(1).loc[x])","    df2['HA'].loc[x]=df2['a_Close'].loc[x]-df2['a_Open'].loc[x]","","","","#   if df2['a_Close'].loc[x] > df2['a_Open'].loc[x]:","    if df2['HA'].loc[x] > 0:    ","        df2['direct'].loc[x]='HA_Green'","    elif df2['HA'].loc[x] < 0:","        df2['direct'].loc[x]='HA_Red'","","","df2=df2[['Date','Volume', 'ticker', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]","","#df2['greenby']=df2['greenby'].round(2)","df2['Close']=df2['Close'].round(2)","#df2['a_Open']=df2['a_Open'].round(2)","#df2['a_Close']=df2['a_Close'].round(2)","df2['High']=df2['High'].round(2)","#df2['a_High']=df2['a_High'].round(2)","","","print(df2.tail(5))","","print('\\n',' 1- day    ',g,'\\n')","","########################################################################################################################################",""],"id":2}],[{"start":{"row":124,"column":7},"end":{"row":124,"column":8},"action":"insert","lines":["x"],"id":3}],[{"start":{"row":124,"column":10},"end":{"row":124,"column":11},"action":"remove","lines":["d"],"id":4},{"start":{"row":124,"column":9},"end":{"row":124,"column":10},"action":"remove","lines":["5"]},{"start":{"row":124,"column":8},"end":{"row":124,"column":9},"action":"remove","lines":["5"]},{"start":{"row":124,"column":7},"end":{"row":124,"column":8},"action":"remove","lines":["x"]}],[{"start":{"row":124,"column":7},"end":{"row":124,"column":8},"action":"insert","lines":["1"],"id":5},{"start":{"row":124,"column":8},"end":{"row":124,"column":9},"action":"insert","lines":["d"]}],[{"start":{"row":125,"column":11},"end":{"row":125,"column":12},"action":"remove","lines":["d"],"id":6}],[{"start":{"row":125,"column":11},"end":{"row":125,"column":12},"action":"insert","lines":["5"],"id":7}],[{"start":{"row":125,"column":11},"end":{"row":125,"column":12},"action":"remove","lines":["5"],"id":8},{"start":{"row":125,"column":10},"end":{"row":125,"column":11},"action":"remove","lines":["1"]}],[{"start":{"row":125,"column":10},"end":{"row":125,"column":11},"action":"insert","lines":["6"],"id":9},{"start":{"row":125,"column":11},"end":{"row":125,"column":12},"action":"insert","lines":["0"]},{"start":{"row":125,"column":12},"end":{"row":125,"column":13},"action":"insert","lines":["m"]}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"insert","lines":["i"],"id":10}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["i"],"id":11}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"insert","lines":["p"],"id":12},{"start":{"row":147,"column":1},"end":{"row":147,"column":2},"action":"insert","lines":["r"]},{"start":{"row":147,"column":2},"end":{"row":147,"column":3},"action":"insert","lines":["o"]},{"start":{"row":147,"column":3},"end":{"row":147,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":147,"column":3},"end":{"row":147,"column":4},"action":"remove","lines":["m"],"id":13},{"start":{"row":147,"column":2},"end":{"row":147,"column":3},"action":"remove","lines":["o"]}],[{"start":{"row":147,"column":2},"end":{"row":147,"column":3},"action":"insert","lines":["i"],"id":14},{"start":{"row":147,"column":3},"end":{"row":147,"column":4},"action":"insert","lines":["n"]},{"start":{"row":147,"column":4},"end":{"row":147,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":147,"column":5},"end":{"row":147,"column":7},"action":"insert","lines":["()"],"id":15}],[{"start":{"row":147,"column":6},"end":{"row":147,"column":7},"action":"insert","lines":["d"],"id":16},{"start":{"row":147,"column":7},"end":{"row":147,"column":8},"action":"insert","lines":["f"]},{"start":{"row":147,"column":8},"end":{"row":147,"column":9},"action":"insert","lines":["2"]}],[{"start":{"row":147,"column":6},"end":{"row":147,"column":7},"action":"insert","lines":["'"],"id":17},{"start":{"row":147,"column":7},"end":{"row":147,"column":8},"action":"insert","lines":["\\"]},{"start":{"row":147,"column":8},"end":{"row":147,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":147,"column":9},"end":{"row":147,"column":10},"action":"insert","lines":["'"],"id":18},{"start":{"row":147,"column":10},"end":{"row":147,"column":11},"action":"insert","lines":[","]}],[{"start":{"row":147,"column":14},"end":{"row":147,"column":15},"action":"insert","lines":[","],"id":19}],[{"start":{"row":147,"column":15},"end":{"row":147,"column":17},"action":"insert","lines":["''"],"id":20}],[{"start":{"row":147,"column":16},"end":{"row":147,"column":17},"action":"insert","lines":["\\"],"id":21},{"start":{"row":147,"column":17},"end":{"row":147,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":128,"column":0},"end":{"row":128,"column":1},"action":"insert","lines":["#"],"id":22,"ignore":true},{"start":{"row":147,"column":0},"end":{"row":149,"column":0},"action":"insert","lines":["","",""]}],[{"start":{"row":142,"column":14},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":143,"column":0},"end":{"row":144,"column":0},"action":"insert","lines":["",""]},{"start":{"row":144,"column":0},"end":{"row":145,"column":0},"action":"insert","lines":["",""]},{"start":{"row":145,"column":0},"end":{"row":146,"column":0},"action":"insert","lines":["",""]},{"start":{"row":146,"column":0},"end":{"row":147,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":144,"column":0},"end":{"row":147,"column":34},"action":"insert","lines":["    df.reset_index(inplace=True)","    df['x']=df['Datetime'].dt.time","    df['d']=df['Datetime'].dt.day_name()","    df['u']=df['Datetime'].dt.date"],"id":24}],[{"start":{"row":144,"column":31},"end":{"row":144,"column":32},"action":"remove","lines":[")"],"id":25},{"start":{"row":144,"column":30},"end":{"row":144,"column":31},"action":"remove","lines":["e"]},{"start":{"row":144,"column":29},"end":{"row":144,"column":30},"action":"remove","lines":["u"]},{"start":{"row":144,"column":28},"end":{"row":144,"column":29},"action":"remove","lines":["r"]},{"start":{"row":144,"column":27},"end":{"row":144,"column":28},"action":"remove","lines":["T"]},{"start":{"row":144,"column":26},"end":{"row":144,"column":27},"action":"remove","lines":["="]},{"start":{"row":144,"column":25},"end":{"row":144,"column":26},"action":"remove","lines":["e"]},{"start":{"row":144,"column":24},"end":{"row":144,"column":25},"action":"remove","lines":["c"]},{"start":{"row":144,"column":23},"end":{"row":144,"column":24},"action":"remove","lines":["a"]},{"start":{"row":144,"column":22},"end":{"row":144,"column":23},"action":"remove","lines":["l"]},{"start":{"row":144,"column":21},"end":{"row":144,"column":22},"action":"remove","lines":["p"]},{"start":{"row":144,"column":20},"end":{"row":144,"column":21},"action":"remove","lines":["n"]},{"start":{"row":144,"column":19},"end":{"row":144,"column":20},"action":"remove","lines":["i"]},{"start":{"row":144,"column":18},"end":{"row":144,"column":19},"action":"remove","lines":["("]},{"start":{"row":144,"column":17},"end":{"row":144,"column":18},"action":"remove","lines":["x"]},{"start":{"row":144,"column":16},"end":{"row":144,"column":17},"action":"remove","lines":["e"]},{"start":{"row":144,"column":15},"end":{"row":144,"column":16},"action":"remove","lines":["d"]},{"start":{"row":144,"column":14},"end":{"row":144,"column":15},"action":"remove","lines":["n"]},{"start":{"row":144,"column":13},"end":{"row":144,"column":14},"action":"remove","lines":["i"]}],[{"start":{"row":144,"column":12},"end":{"row":144,"column":13},"action":"remove","lines":["_"],"id":26},{"start":{"row":144,"column":11},"end":{"row":144,"column":12},"action":"remove","lines":["t"]},{"start":{"row":144,"column":10},"end":{"row":144,"column":11},"action":"remove","lines":["e"]},{"start":{"row":144,"column":9},"end":{"row":144,"column":10},"action":"remove","lines":["s"]},{"start":{"row":144,"column":8},"end":{"row":144,"column":9},"action":"remove","lines":["e"]},{"start":{"row":144,"column":7},"end":{"row":144,"column":8},"action":"remove","lines":["r"]},{"start":{"row":144,"column":6},"end":{"row":144,"column":7},"action":"remove","lines":["."]},{"start":{"row":144,"column":5},"end":{"row":144,"column":6},"action":"remove","lines":["f"]},{"start":{"row":144,"column":4},"end":{"row":144,"column":5},"action":"remove","lines":["d"]},{"start":{"row":144,"column":0},"end":{"row":144,"column":4},"action":"remove","lines":["    "]},{"start":{"row":143,"column":0},"end":{"row":144,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":144,"column":0},"end":{"row":144,"column":4},"action":"remove","lines":["    "],"id":27}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"remove","lines":["    "],"id":28}],[{"start":{"row":146,"column":0},"end":{"row":146,"column":4},"action":"remove","lines":["    "],"id":29}],[{"start":{"row":225,"column":13},"end":{"row":225,"column":14},"action":"remove","lines":["e"],"id":30},{"start":{"row":225,"column":12},"end":{"row":225,"column":13},"action":"remove","lines":["t"]},{"start":{"row":225,"column":11},"end":{"row":225,"column":12},"action":"remove","lines":["a"]},{"start":{"row":225,"column":10},"end":{"row":225,"column":11},"action":"remove","lines":["D"]}],[{"start":{"row":225,"column":10},"end":{"row":225,"column":11},"action":"insert","lines":["x"],"id":31}],[{"start":{"row":225,"column":13},"end":{"row":225,"column":14},"action":"insert","lines":[","],"id":32}],[{"start":{"row":225,"column":14},"end":{"row":225,"column":16},"action":"insert","lines":["''"],"id":33}],[{"start":{"row":225,"column":15},"end":{"row":225,"column":16},"action":"insert","lines":["d"],"id":34}],[{"start":{"row":225,"column":17},"end":{"row":225,"column":18},"action":"insert","lines":[","],"id":35}],[{"start":{"row":225,"column":18},"end":{"row":225,"column":19},"action":"insert","lines":["i"],"id":36}],[{"start":{"row":225,"column":18},"end":{"row":225,"column":19},"action":"remove","lines":["i"],"id":37}],[{"start":{"row":225,"column":18},"end":{"row":225,"column":19},"action":"insert","lines":["u"],"id":38}],[{"start":{"row":225,"column":18},"end":{"row":225,"column":19},"action":"insert","lines":["'"],"id":39}],[{"start":{"row":225,"column":21},"end":{"row":225,"column":22},"action":"insert","lines":[","],"id":40},{"start":{"row":225,"column":22},"end":{"row":225,"column":23},"action":"insert","lines":["'"]}],[{"start":{"row":225,"column":13},"end":{"row":225,"column":14},"action":"remove","lines":[","],"id":41}],[{"start":{"row":122,"column":63},"end":{"row":122,"column":64},"action":"remove","lines":["y"],"id":42},{"start":{"row":122,"column":62},"end":{"row":122,"column":63},"action":"remove","lines":["l"]},{"start":{"row":122,"column":61},"end":{"row":122,"column":62},"action":"remove","lines":["i"]},{"start":{"row":122,"column":60},"end":{"row":122,"column":61},"action":"remove","lines":["a"]},{"start":{"row":122,"column":59},"end":{"row":122,"column":60},"action":"remove","lines":["d"]}],[{"start":{"row":122,"column":59},"end":{"row":122,"column":60},"action":"insert","lines":["H"],"id":43},{"start":{"row":122,"column":60},"end":{"row":122,"column":61},"action":"insert","lines":["o"]},{"start":{"row":122,"column":61},"end":{"row":122,"column":62},"action":"insert","lines":["u"]},{"start":{"row":122,"column":62},"end":{"row":122,"column":63},"action":"insert","lines":["t"]}],[{"start":{"row":122,"column":62},"end":{"row":122,"column":63},"action":"remove","lines":["t"],"id":44}],[{"start":{"row":122,"column":62},"end":{"row":122,"column":63},"action":"insert","lines":["r"],"id":45},{"start":{"row":122,"column":63},"end":{"row":122,"column":64},"action":"insert","lines":["l"]},{"start":{"row":122,"column":64},"end":{"row":122,"column":65},"action":"insert","lines":["y"]}],[{"start":{"row":225,"column":0},"end":{"row":225,"column":1},"action":"insert","lines":["#"],"id":46,"ignore":true},{"start":{"row":226,"column":0},"end":{"row":230,"column":0},"action":"insert","lines":["df2=df2[['ticker','x','d','u','Volume', 'Opena', 'green', 'greenby', 'direct', 'HA','a_High','a_Low', 'High', 'a_Close', 'a_Open','Close']]","","","",""]}],[{"start":{"row":226,"column":39},"end":{"row":226,"column":46},"action":"remove","lines":[" 'Opena"],"id":47,"ignore":true},{"start":{"row":226,"column":39},"end":{"row":226,"column":45},"action":"insert","lines":["'Close"]},{"start":{"row":226,"column":84},"end":{"row":226,"column":92},"action":"insert","lines":["Opena','"]},{"start":{"row":226,"column":136},"end":{"row":226,"column":144},"action":"remove","lines":[",'Close'"]}],[{"start":{"row":226,"column":48},"end":{"row":226,"column":63},"action":"insert","lines":["'direct', 'HA',"],"id":48,"ignore":true},{"start":{"row":226,"column":82},"end":{"row":226,"column":98},"action":"remove","lines":[" 'direct', 'HA',"]}],[{"start":{"row":156,"column":0},"end":{"row":156,"column":1},"action":"insert","lines":["#"],"id":49}],[{"start":{"row":108,"column":0},"end":{"row":108,"column":1},"action":"insert","lines":["i"],"id":50}],[{"start":{"row":108,"column":0},"end":{"row":108,"column":1},"action":"remove","lines":["i"],"id":51}],[{"start":{"row":108,"column":0},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""]},{"start":{"row":110,"column":0},"end":{"row":111,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":109,"column":0},"end":{"row":111,"column":0},"action":"insert","lines":["df2=df2[['ticker','x','d','u','Volume','Close', 'direct', 'HA','green', 'greenby','Opena','a_High','a_Low', 'High', 'a_Close', 'a_Open']]","",""],"id":53}],[{"start":{"row":109,"column":27},"end":{"row":109,"column":28},"action":"remove","lines":["u"],"id":54},{"start":{"row":109,"column":26},"end":{"row":109,"column":28},"action":"remove","lines":["''"]},{"start":{"row":109,"column":25},"end":{"row":109,"column":26},"action":"remove","lines":[","]},{"start":{"row":109,"column":24},"end":{"row":109,"column":25},"action":"remove","lines":["'"]},{"start":{"row":109,"column":23},"end":{"row":109,"column":24},"action":"remove","lines":["d"]},{"start":{"row":109,"column":22},"end":{"row":109,"column":23},"action":"remove","lines":["'"]},{"start":{"row":109,"column":21},"end":{"row":109,"column":22},"action":"remove","lines":[","]},{"start":{"row":109,"column":20},"end":{"row":109,"column":21},"action":"remove","lines":["'"]},{"start":{"row":109,"column":19},"end":{"row":109,"column":20},"action":"remove","lines":["x"]}],[{"start":{"row":109,"column":19},"end":{"row":109,"column":20},"action":"insert","lines":["D"],"id":55},{"start":{"row":109,"column":20},"end":{"row":109,"column":21},"action":"insert","lines":["a"]},{"start":{"row":109,"column":21},"end":{"row":109,"column":22},"action":"insert","lines":["t"]},{"start":{"row":109,"column":22},"end":{"row":109,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":109,"column":23},"end":{"row":109,"column":24},"action":"insert","lines":["'"],"id":56}],[{"start":{"row":107,"column":0},"end":{"row":107,"column":1},"action":"insert","lines":["#"],"id":57}]]},"ace":{"folds":[],"scrolltop":2266,"scrollleft":0,"selection":{"start":{"row":109,"column":16},"end":{"row":109,"column":16},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":102,"state":"start","mode":"ace/mode/python"}},"timestamp":1625163451620,"hash":"5fa5f591e3af1109a77f9351cabb26d7c59539b9"}