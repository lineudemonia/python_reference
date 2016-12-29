# -*- coding: utf-8 -*-

'''
	CHAPTER ONE OF UDACITY MACHINE LEARNING FINANCE
													'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def get_max_close(symbol):
	''' Return the maximum closing value for stock indicated by symbol.
	Data is saved in dta/<symbol>.csv
	'''
	df = pd.read_csv("data/{}.csv".format(symbol))
	return df["Close"].mean()

def plot_stock(df, title = 'Stock prices'):
	"""Prints out the stock price in a chart"""
	ax = df.plot(title = title, fontsize = 10)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def symbol_to_path(symbol, base_dir = "data"):
	"""Return CSV file path given ticker symbol"""
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(dates, symbols):
	# Create data frame given dates
	df = pd.DataFrame(index = dates)

	# Add benchmark 'SPY'
	if 'SPY' not in symbols:
		symbols.insert(0, 'SPY')

	# AUTOMATE FILES FROM LIST
	for symbol in symbols:
		# Load second data frame from file, need to REINDEX other wise the indices wont match
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col = 'Date',
		                      parse_dates = True, usecols = ['Date', 'Adj Close'],
		                      na_values = ['nan'])
		# Rename column name otherwise it will all be 'Adj Close'
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df = df.join(df_temp)
 
	# Drop "NA"
	df = df.dropna()
	return df

def normalize_data(df):
	""" Normalize stock prices use the first row of data frame"""
	return df / df.ix[0,:]

def get_daily_returns(df):
	daily_returns = df.copy()
	daily_returns = (df / df.shift(1) - 1)
	daily_returns.ix[0, :] = 0
	return daily_returns

def get_bollinger_bands(rm, rstd):
	return rm + 2 * rstd, rm - 2 * rstd

def get_rolling_mean(df, symbol, window):
	return pd.Series.rolling(df[symbol], window = window).mean()

def get_rolling_rstd(df, symbol, window):
	return pd.Series.rolling(df[symbol], window = window).std()

def plot_bollinger(df, symbol, window):

	''' GET data from df, and plot bollinger charts.
		Currently needs to manually set symbol[1] to locate the desired ticker because
		in the get_data function, symbol was changed, not sure why as it's a local variable. 

		FIXED IN THE SEPARTE BOLLINGER.PY FUNCTION'''

	rm = get_rolling_mean(df, symbol[1], window)
	rstd = get_rolling_rstd(df, symbol[1], window)
	upper_band, lower_band = get_bollinger_bands(rm, rstd)
	ax = df[symbol[1]].plot(title = symbol[1] + " bollinger", label = symbol[1])
	rm.plot(label = str(window) + "d rolling mean", ax = ax)
	upper_band.plot(label = "Upper band", ax = ax)
	lower_band.plot(label = "Lower band", ax = ax)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.legend(loc = "upper left")
	plt.show()

def plot_histogram(df, ticker):
	df.hist(bins = 20)
	mean = df[ticker].mean()
	std = df[ticker].std()
	plt.axvline(mean, color = 'w', linestyle = 'dashed', linewidth = 2)
	plt.axvline(std, color = 'r', linestyle = 'dashed', linewidth = 2)
	plt.axvline(-std, color = 'r', linestyle = 'dashed', linewidth = 2)
	plt.show()

def plot_scatterplot(daily_returns):
	daily_returns.plot(kind = "scatter", x = 'SPY', y = "GOOG")
	beta_goog, alpha_goog = np.polyfit(daily_returns['SPY'], daily_relturns['GOOG'], 1)
	plt.plot(daily_returns['SPY'], beta_goog * daily_returns['SPY'] + alpha_goog, '.', color = 'r')
	print(daily_returns.corr(method = 'pearson'))
	plt.show()


def test_run():
	# Specify date range
	start_date = "2009-01-01"
	end_date = "2016-10-31"
	window = 20
	# Create date range
	dates = pd.date_range(start_date, end_date)
	# symbols = ['GOOG', 'IBM', 'GLD']
	symbols = ['GOOG']
	df = get_data(dates, symbols)
	# plot_bollinger(df, symbols, window)
	# plot_stock(normalize_data(df))
	daily_returns = get_daily_returns(df)
	# plot_stock(df)
	#plot_histogram(daily_returns, symbols[0])
	plot_scatterplot(daily_returns)

def f(x):
	y = (x - 1.5) ** 2 + 0.5
	print("X = {}, Y = {}".format(x, y))
	return y

def error(line, data):
	err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)


def test_run2():
	x_guess = 2.0
	min_result = spo.minimize(f, x_guess, method = 'SLSQP', options = {'disp': True})
	print("Minima found at:")
	print("X = {}, Y = {}".format(min_result.x, min_result.fun))

if __name__ == "__main__":
	test_run2()