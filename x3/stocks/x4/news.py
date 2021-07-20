from yahoo_fin import news as g
ticker=input("enter ticker: ")
#print(g.get_yf_rss('AMZn'))
m=g.get_yf_rss(ticker)
i=0

for x in (m):
    print('\n')
    print(i)
    for v in x.keys():
        print(v,'  ',x[v])
    i=i+1



# 'summary', 'summary_detail', 'id', 'guidislink', 'links', 'link', 'published', 'published_parsed', 'title', 'title_detail'
