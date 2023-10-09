# Analyze Financial Data with Python Capstone Project

In this project, I used Python Markowitz Portfolio Theory (1952) to find the efficient frontiner and the optimal portfolios with the 10 most biggest companies in the US by market cap. The companies included are Apple, Microsoft, Google, Amazon, Nvidia, Tesla, Meta, Berkshire Hathaway, Eli Lilly And Co, and Visa. I used data from 1st of January 2018 to 1st of January 2023. 

## Packages 
+ [Pandas](https://pypi.org/project/pandas/) - Data manipulation and to create and manipualte dataframes
+ [Numpy](https://pypi.org/project/numpy/) - Multidimensional arrays and matrices
+ [Datetime](https://docs.python.org/3/library/datetime.html) - To Manipulate dates and times, specifically used when scraping yahoo Finance
+ [Matplotlib](https://matplotlib.org/) - Visuals of stock performance and the efficient frontier
+ [Random](https://docs.python.org/3/library/random.html) - To create pseudo random weights for the portfolios
+ [Cvxopt](https://pypi.org/project/cvxopt/) - Used for matrices
+ [Pandas_datareader](https://pandas-datareader.readthedocs.io/en/latest/) - For scraping Yahoo Finance
+ [Yfinance](https://pypi.org/project/yfinance/) - pandas datareader has a bug for scraping yahoo finance data specifically. Therefore, the yfinance package is needed to get around this problem. 

## Note
To scrape Yahoo Finance using Pandas datareader, you need an extra package, yfinance. To be able to scrape you need to run this `code` before scraping. 
``` python
yf.pdr_override()
```

## Improvements
+ Reusability - Currently, the stock were lazely handpicked by me and the code is made with the sole purpose of finding the efficient frontier for this specific csv file. If I wanted to find the efficient frontier for other stocks, some manual labour is needed. There is much improvements that can be done when it comes to reusability. Ideally, the only input needed are the stocks(tickers) you want in your portfolio. The output should be the weights of the stocks for the difference optimal portfolios given your current risk preference. 
+ Completeness - The project is not fully completed as the tangent portfolio is not found. The tangent portfolio is the portfolio on the efficient frontier that has the highest sharpe ratio (highest return for each unit of risk). The program should be able to find the tangent portfolio and use the Capital Market Line (CML) to adjust the your risk preference. 


## Final notes
I will likely come back to this project and improve on it at a later date. I did scrape 2 other csv file with expands upon the Base csv file. The first file includes the top 10 stock in the EU by market cap. The second file further includes 5 handpicked stocks of mine. 