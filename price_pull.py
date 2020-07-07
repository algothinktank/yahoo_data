#import schedule
import time
import numpy as np
import yfinance as yf
import pandas as pd
import math
#import plotly.graph_objects as go

#ticker = input('What ticker do you want?: ')
ticker = 'SPY'
#fname = input('What is the name of the yahoo file?')
fname = 'yahoo.csv'
#px_history = input('How far back for the historical price data?: ')
px_history = '1mo'
#fname1 = input('What is the name of the output file?')
#fname1 = 'betterHMA.csv'
#window_inp = input("How many periods for the gooseline?: ")
window_inp = int(6)
#tail_inp = input('How many data points should print out?: ')
#tail_int = int(tail_inp)
tail_int = int(25)

    # input questions

data = yf.download(ticker, period = px_history, interval = '5m')
#print(data)

data.to_csv(fname)
df = pd.read_csv(fname)
print (df)
