# -*- coding: utf-8 -*-

import pandas as pd
import os
import numpy as np
import datetime
import time

def get_ticker_price(tickers, dates):
	df = pd.DataFrame(index = dates)

	for ticker in tickers:
		df_temp = pd.read_csv("data/{}.csv".format(ticker), index_col = "Date",
		                      parse_dates = True, usecols = ['Date', 'Adj Close'])
		df_temp = df_temp.rename(columns = {'Adj Close': ticker})
		df = df.join(df_temp)
	df = df.dropna()
	return (df)


def test_run_price():
	tickers = ["AAPL", "GOOG", "GLD"]
	start_date = "2016-01-01"
	end_date = "2016-10-30"
	dates = pd.date_range(start_date, end_date)
	df = get_ticker_price(tickers, dates)
	print(df[:20])


def test_run():
	# Creates a numpy.ndarray object
	#print(np.array([2, 3, 4]))

	# Creates an empty array of dim 5:
	#print(np.empty(5))

	# Creates an array with all ones
	#print(np.ones((5, 4)))

	# Creates a random value between 0 and 1 for 5 * 4
	# Random is generated by uniform distribution
	#print(np.random.rand(5, 4))

	# Creates a standard distribution with mean == 0 and std == 1
	#print(np.random.normal(size = (2, 3)))

	# 
	np.random.seed(datetime.datetime.now().microsecond)
	a = np.random.randint(0, 10, size = (5, 4))
	print(a)

	# # Get sum of all elements
	# print(a.sum())


	# # Iterate over rows to get sum of each column
	# print(a.sum(axis = 0))

	# # Iterate over cols to get sum of each row
	# print(a.sum(axis = 1))

	# Mask items larger or equal to than mean
	mean = a.mean()
	print(a[a < mean])	


if __name__ == "__main__":
	test_run()