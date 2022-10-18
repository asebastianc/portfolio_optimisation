import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime as dt

df = pd.DataFrame({"Name": ["Berkshire Hathaway Inc", "Alphabet Inc", "Apple Inc", "Yahoo Japan Corporation", "Hargreaves Lansdown", "Realty Income Corporation", "Meta Platforms", "Amazon.com", "Legal & General Group", "Intuitive Surgical", "Block", "Tesco", "BP", "Lloyds Banking Group", "Barclays", "Unilever", "National Grid", "WisdomTree Investments", "Glencore", "Phoenix Group Holdings"],
	"Ticker": ["BRK-B", "GOOG", "AAPL", "YAHOF", "HL.L", "O", "META", "AMZN", "LGEN.L", "ISRG", "SQ", "TSCO.L", "BP", "LLOY.L", "BARC.L", "ULVR.L", "NG.L", "WETF", "GLEN.L", "PHNX.L"]})

start = dt.datetime(2019, 10, 5)
end = dt.datetime(2022, 10, 5)

# time difference between start and end dates
months = (end.year - start.year) * 12 + (end.month - start.month)

# set risk free rate
rfr = 0

# annualized returns
annualized_returns = []

# sharpe ratios
sharpe_ratios = []

daily_returns = pd.DataFrame()

# compute annualized return and sharpe ratio for each stock
for ticker in df["Ticker"]:
	# download data from yahoo
	df_stock = web.DataReader(ticker, 'yahoo', start, end)

	# store daily returns per stock
	daily_returns["{}".format(ticker)] = df_stock["Adj Close"]

	df_stock = df_stock["Adj Close"]

	# annualized return
	total_return = (df_stock[-1] - df_stock[0]) / df_stock[0]
	annualized_return = ((1 + total_return) ** (12 / months)) - 1
	annualized_returns.append(annualized_return)

	# sharpe ratio
	returns = df_stock.pct_change()
	# calculate volatility using 250 trading days
	volatility = returns.std() * np.sqrt(250)
	sharpe_ratio = ((annualized_return - rfr)  / volatility)
	sharpe_ratios.append(sharpe_ratio)

df["Annualized Return"] = annualized_returns
df["Sharpe Ratio"] = sharpe_ratios

daily_returns = daily_returns.pct_change()

df.to_csv("../data/stocks_info.csv", index = False)
daily_returns.to_csv("../data/daily_returns.csv")