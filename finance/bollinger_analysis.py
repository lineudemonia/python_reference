# -*- coding: utf-8 -*-

'''
	bollinger analysis of a certain stock given date range
															'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import time

def ticker_to_path(ticker, base_dir = "data"):
	"""Return CSV file path given ticker ticker"""
	return os.path.join(base_dir, "{}.csv".format(str(ticker)))

def get_data(dates, tickers):
	# Create data frame given dates
	df = pd.DataFrame(index = dates)

	# AUTOMATE FILES FROM LIST
	for ticker in tickers:
		# Load second data frame from file, need to REINDEX other wise the indices wont match
		df_temp = pd.read_csv("data/{}.csv".format(ticker), index_col = 'Date',
		                      parse_dates = True, usecols = ['Date', 'Adj Close'],
		                      na_values = ['nan'])
		# Rename column name otherwise it will all be 'Adj Close'
		df_temp = df_temp.rename(columns={'Adj Close': ticker})
		df = df.join(df_temp)

	# Drop "NA"
	df = df.dropna()
	return df

def get_bollinger_bands(rm, rstd):
	return rm + 2 * rstd, rm - 2 * rstd

def get_rolling_mean(df, ticker, window):
	return pd.Series.rolling(df[ticker], window = window).mean()

def get_rolling_rstd(df, ticker, window):
	return pd.Series.rolling(df[ticker], window = window).std()

def get_daily_returns(df):
	daily_returns = df.copy()
	# have to do .value because otherwise panda will automatically align same column headers
	daily_returns[1:] = df[1:] / df[:-1].values - 1
	daily_returns.ix[0, :] = 0
	# alternatively:
	daily_returns = (df / df.shift(1) - 1)
	daily_returns.ix[0, :] = 0
	print(daily_returns)

def plot_bollinger(df, ticker, window):

	''' GET data from df, and plot bollinger charts.'''
	rm = get_rolling_mean(df, ticker, window)
	rstd = get_rolling_rstd(df, ticker, window)
	upper_band, lower_band = get_bollinger_bands(rm, rstd)
	ax = df[ticker].plot(title = ticker + " bollinger", label = ticker)
	rm.plot(label = str(window) + "d rolling mean", ax = ax)
	upper_band.plot(label = "Upper band", ax = ax)
	lower_band.plot(label = "Lower band", ax = ax)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.legend(loc = "upper left")
	plt.show()

def test_run():
	# Specify date range
	start_date = "2012-01-01"
	end_date = time.strftime("%Y-%m-%d")
	window = 20
	# Create date range
	dates = pd.date_range(start_date, end_date)
	# tickers = ['GOOG', 'IBM', 'GLD']
	tickers = ['TSLA', 'GOOG', 'BGNE', 'NVDA']
	for ticker in tickers:
		df = get_data(dates, tickers)
		plot_bollinger(df, ticker, window)

if __name__ == "__main__":
	test_run()