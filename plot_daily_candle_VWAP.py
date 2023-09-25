import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


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


# Function to plot daily closing prices, VWAP, and HMA
def plot_prices_vwap_hma(data, ticker_symbol, hma_period):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Adj Close'], label=f'{ticker_symbol} Daily Closing Price', color='b')
    plt.plot(data.index, data['VWAP'], label=f'{ticker_symbol} VWAP', color='g', linestyle='--')
    plt.plot(data.index, data['HMA'], label=f'{ticker_symbol} HMA ({hma_period})', color='r', linestyle='-.')
    plt.title(f'{ticker_symbol} Daily Closing Prices, VWAP, and HMA (Past 90 Days)')
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

    # Plot daily closing prices, VWAP, and HMA
    plot_prices_vwap_hma(data, ticker_symbol, hma_period)


if __name__ == "__main__":
    main()
