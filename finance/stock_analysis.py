# -*- coding: utf-8 -*-

'''
	CHAPTER ONE OF UDACITY MACHINE LEARNING FINANCE
													'''
import os
import pandas as pd
import matplotlib.pyplot as plt

def get_max_close(symbol):
	''' Return the maximum closing value for stock indicated by symbol.
	Data is saved in dta/<symbol>.csv
	'''
	df = pd.read_csv("data/{}.csv".format(symbol))
	return df["Close"].mean()

def plot_stock(df, title = 'Stock prices'):
	"""Prints out the stock price in a chart"""
	ax = df.plot(title = title, fontsize = 2)
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

def test_run():
	# Specify date range
	start_date = "2010-01-01"
	end_date = "2016-10-30"

	# Create date range
	dates = pd.date_range(start_date, end_date)
	symbols = ['GOOG', 'IBM', 'GLD']
	df = get_data(dates, symbols)
	print(df[0:3])
	print(df.values[:10])
	print(df.values[0:3, 1:3])

	'''
	Plot stock price
	'''
	#plot_stock(normalize_data(df))



if __name__ == "__main__":
	test_run()