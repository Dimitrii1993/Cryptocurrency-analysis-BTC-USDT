import numpy as np 
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import seaborn as sns 
import plotly.express as px

btc_1 = pd.read_csv('btcusd.csv')

btcusd = btc_1.copy()

btc_1

ser_date = pd.Series(data = btcusd['date'])
ser_open = pd.Series(data = btcusd['open'], dtype = 'int64')
ser_close = pd.Series(data = btcusd['close'], dtype = 'int64')
ser_volume = pd.Series(data = btcusd['Volume USD'], dtype = 'int64')

btc = pd.DataFrame({
    'date' : ser_date,
    'open': ser_open,
    'close': ser_close,
    'volume': ser_volume 
})

btc['date'] = pd.to_datetime(btc['date'])
btc.head()
