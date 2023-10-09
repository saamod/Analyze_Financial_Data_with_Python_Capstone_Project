###### Analyze Financial Data with Python Capstone Project ######

# Import packages
import pandas as pd
import numpy as np
from datetime import datetime
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()

# Stock picks - Amazon, Nvidia, Apple, and Microsoft are huge companies which are a part of S&P 500, hench companies that are 
# largerly invested in and will continue to be largerly invested due to the fact of being in several popular mutual funds and 
# ETF that covers the S&P 500, tech, and more. Constellation Software and Air Liquide are two personal favorites of mine as
# they are companies that are extremely consistent at generating return every year. They do have a high do have a high P/E ratio,
# espceially Constellation Software, but that just speaks to how well the company is run and how consistent it generates returns
base_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "BRK-B", "LLY", "V"]
expanded_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "BRK-B", "LLY", "V", "NVO", "MC.PA", "ASML", "OR.PA", "ACN", "RMS.PA", "SAP", "TTE", "SNY", "CDI.PA"]
Personal_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "META", "BRK-B", "LLY", "V", "NVO", "MC.PA", "ASML", "OR.PA", "ACN", "RMS.PA", "SAP", "TTE", "SNY", "CDI.PA", "CSU.TO", "AI.PA", "WKL.AS", "SALM.OL", "EQNR"]


# Scrape the Base Stocks using pandas-datareader and saving the Adjusted Closing price to a CSV file that will be used in Main.py
# The Base stocks consists of the 10 companies with the highest market cap in the US
start = datetime(2018, 1, 1)
end = datetime(2023, 1, 1)
df = web.get_data_yahoo(base_symbols, start, end)
df = df['Adj Close']
df.to_csv("Base_stocks.csv", sep=',', index=False, encoding='utf-8')

# Scraping Expanded list of stocks. The purpose of the expanded list is to if adding more stocks will increase our potential return for each unit of risk. 
# The Expanded list included the 10 companies in the US and the 10 companies in the EU with the highest market cap
df = web.get_data_yahoo(expanded_symbols, start, end)
df = df['Adj Close']
df.to_csv("Expanded_stocks.csv", sep=',', index=False, encoding='utf-8')

#Scrapeing all above stock plus 5 handpicked stocks of mine
df = web.get_data_yahoo(Personal_symbols, start, end)
df = df['Adj Close']
df.to_csv("Personal_stocks.csv", sep=',', index=False, encoding='utf-8')