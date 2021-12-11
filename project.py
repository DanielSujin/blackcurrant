import datetime
import pandas as pd

stockcode ='RELIANCE'
ts1 = str(int(datetime.datetime(2019, 3, 16).timestamp())) 
ts2 = str(int(datetime.datetime(2021, 12, 10).timestamp()))
interval = '1d'
events = 'history'
url = 'https://query1.finance.yahoo.com/v7/finance/download/'+ stockcode + '.NS?period1=' + ts1 + '&period2=' + ts2 + '&interval='+ interval + '&events=' + events
print(url)
print (ts1, ts2)

try:
    stockdata = pd.read_csv(url)
    print(stockdata)
except:
    print("Not able to fetch value for code : "+stockcode)
    print("Either stock code is not correct or could be connectivity issue..")

stockdata = pd.read_csv(url)
stockdata