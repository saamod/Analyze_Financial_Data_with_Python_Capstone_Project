###### Analyze Financial Data with Python Capstone Project ######

# Import packages
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import random
import cvxopt as opt
from cvxopt import blas, solvers

#Getting the data from Base_stock.csv which includes the adjusted closing prices of the stocks I picked

stock_data = pd.read_csv("Base_stocks.csv")
#print(stock_data)

# Calculate the expected returns and standard deviation for each stock

pct_return = stock_data.pct_change()
#print(pct_return)

# Calculate the Average Expected Returns
avg_return = pct_return.mean()
#print(avg_return)


# Plot of stock prices
stock_data.plot()
plt.xlabel('Time')
plt.ylabel('Stock price')
plt.title('Stock prices')
#plt.show()
plt.savefig('Base Stock Prices.png')

# Creating a covariance matrix of the stock returns
cov_returns = pct_return.cov()
#print(cov_returns)

# Creating a function to make 5000 portfolios with random weights
def return_portfolios(expected_returns, cov_matrix):
  np.random.seed(1)
  port_returns = []
  port_volatility = []
  stock_weights = []
    
  selected = (expected_returns.axes)[0]
    
  num_assets = len(selected) 
  num_portfolios = 5000
    
  for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    returns = np.dot(weights, expected_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)
    
    portfolio = {'Returns': port_returns,
                 'Volatility': port_volatility}
    
  for counter,symbol in enumerate(selected):
    portfolio[symbol +' Weight'] = [Weight[counter] for Weight in stock_weights]
    
  df = pd.DataFrame(portfolio)
    
  column_order = ['Returns', 'Volatility'] + [stock+' Weight' for stock in selected]
    
  df = df[column_order]
   
  return df

# Creating 5000 random portfolio
random_portfolios = return_portfolios(avg_return, cov_returns)
#print(random_portfolios)

# Creating a function for the optimal portfolio for each unit of risk
def optimal_portfolio(returns):
    n = returns.shape[1]
    returns = np.transpose(np.matrix(returns))

    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))
    pbar = opt.matrix(np.mean(returns, axis=1))

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)

    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] for mu in mus]
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios]
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']
    return np.asarray(wt), returns, risks

# Creating weights, returns, risks, for the optimal portfolios
weights, returns, risks = optimal_portfolio(pct_return[1:])

# Creating the standard deviation for each stock in the portfolio
single_asset_std = np.sqrt(np.diagonal(cov_returns))

# Plotting the random portfolios
random_portfolios.plot.scatter(x='Volatility', y='Returns')
try: 
  plt.plot(risks, returns, 'y-o')
except: 
  pass
plt.scatter(single_asset_std, avg_return, marker='X', color='red', s=200)
for xc in single_asset_std:
    plt.axvline(x=xc, color='red')
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
#plt.savefig('Efficient Frontier.png')
plt.show()
