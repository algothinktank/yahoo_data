import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from mpl_finance import candlestick_ohlc


# Function to calculate VWAP (Volume Weighted Average Price)
def calculate_vwap(data):
    data['Volume'] = data['Volume'].astype(float)
    data['Cumulative Volume'] = data['Volume'].cumsum()
    data['Cumulative Value'] = (data['Adj Close'] * data['Volume']).cumsum()
    data['VWAP'] = data['Cumulative Value'] / data['Cumulative Volume']
    return data['VWAP']


# Function to calculate Hull Moving Average (HMA)
def calculate_hma(data, period):
    wma_half = data['Adj Close'].rolling(window=period // 2).mean()
    wma_full = data['Adj Close'].rolling(window=period).mean()
    hma = (wma_half * 2 - wma_full).rolling(window=int(period ** 0.5)).mean()
    return hma


# Function to plot Japanese candlestick chart, VWAP, and HMA
def plot_candlestick_vwap_hma(data, ticker_symbol, hma_period):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.xaxis_date()  # Display dates on the x-axis

    # Plot Japanese candlesticks
    from mpl_finance import candlestick_ohlc
    ohlc = data[['Open', 'High', 'Low', 'Adj Close']].reset_index()
    ohlc['Date'] = ohlc['Date'].map(matplotlib.dates.date2num)  # Convert dates to a format matplotlib understands
    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r', alpha=0.7)

    plt.plot(data.index, data['VWAP'], label=f'{ticker_symbol} VWAP', color='b', linestyle='--')
    plt.plot(data.index, data['HMA'], label=f'{ticker_symbol} HMA ({hma_period})', color='purple', linestyle='-.')
    plt.title(f'{ticker_symbol} Japanese Candlesticks, VWAP, and HMA (Past 90 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Main function
def main():
    # Request the user for the ticker symbol of the asset
    ticker_symbol = input("Enter the ticker symbol of the asset (e.g., AAPL): ")

    # Calculate the start date as 90 days ago from the current date
    end_date = datetime.today()
    start_date = end_date - timedelta(days=90)

    # Fetch historical data from Yahoo Finance
    data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Calculate VWAP
    data['VWAP'] = calculate_vwap(data)

    # Calculate and set HMA period (adjust as needed)
    hma_period = 14

    # Calculate HMA
    data['HMA'] = calculate_hma(data, hma_period)

    # Plot Japanese candlestick chart, VWAP, and HMA
    plot_candlestick_vwap_hma(data, ticker_symbol, hma_period)


if __name__ == "__main__":
    main()
