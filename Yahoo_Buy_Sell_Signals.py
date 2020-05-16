import yfinance as yf
import plotly.graph_objects as go
import pandas as pd


# download dataframe
#    # use "period" instead of start/end
#         # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# fetch data by interval (including intraday if period < 60 days)
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

#df = yf.download("SPY AMZN", period='1mo', interval = '5m', group_by= 'ticker')
data = yf.download("SPY", period='1y')
print(data)
fname = 'yahoo_plot.csv'
data.to_csv(fname)
df = pd.read_csv(fname)
#print(df)
num_periods = 9
df['sma_indicator'] = df['Close'].rolling(num_periods).mean()

#df.to_csv('sma.csv')
#print(df)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['sma_indicator'],
        name="SMA"
    ))


#fig.add_trace(
#    go.Scatter(
#        x=df['Date'],
#        y=df['Close'],
#        name="Price"
#    ))

fig.show()
