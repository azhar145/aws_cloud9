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
#print(gt.get_tickers(NYSE=True, NASDAQ=True, AMEX=True))
#print(gt.get_tickers(NASDAQ=True))

from get_all_tickers import get_tickers as gt

list_of_tickers = gt.get_tickers()
# or if you want to save them to a CSV file
get.save_tickers()
