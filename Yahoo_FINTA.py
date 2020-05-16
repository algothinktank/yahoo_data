import math
import numpy
import pandas as pd
from FINTA import TA
import plotly.graph_objects as go
import yfinance as yf

num_periods = 9
periods_half = numpy.round(num_periods / 2)
periods_sqrt = numpy.round(math.sqrt(num_periods))

data = yf.download("SPY", period='1y')
#print(data)
fname = 'yahoo_plot.csv'
data.to_csv(fname)
df = pd.read_csv(fname)
df['sma_indicator'] = df['Close'].rolling(num_periods).mean()
df["ema_slow"] = TA.EMA(df, num_periods, "Close")
df["ema_fast"] = TA.EMA(df, periods_half, "Close")
df['ema_indicator'] = df['Close'].ewm(span = num_periods, adjust = False).mean()
df["wma"] = TA.WMA(df, num_periods, "Close")
#df["hma"] = TA.HMA(df, num_periods, "Close")

#print(df)
df.to_csv('ema.csv')

#select what you want to work with
#print(df.columns)
#dfobj = df[['Date', 'Close', 'ema_fast']].tail(tail_int)
print(df)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x = df['Date'],
        y = df['ema_slow'],
        name="ema_TA"
    ))

fig.add_trace(
    go.Scatter(
        x = df['Date'],
        y = df['sma_indicator'],
        name="SMA"
    ))


fig.add_trace(
    go.Scatter(
        x = df['Date'],
        y = df['ema_indicator'],
        name="ema"
    ))

fig.add_trace(
    go.Scatter(
        x = df['Date'],
        y = df['wma'],
        name="wma"
    ))


fig.add_trace(
    go.Scatter(
        x = df['Date'],
        y = df['Close'],
        name="price"
    ))

fig.show()
