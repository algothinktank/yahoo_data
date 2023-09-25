from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import yfinance as yf

ticker_symbol = input("Enter the ticker symbol of the asset (e.g., AAPL): ")

end_date = datetime.today()
start_date = end_date - timedelta(days=360)

data = yf.download(ticker_symbol, start=start_date, end=end_date)

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'], label=f'{ticker_symbol} Daily Closing Price', color='b')
plt.title(f'{ticker_symbol} Daily Closing Prices (Past {start_date} - {end_date} Days)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
