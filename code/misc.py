import csv

f = open('../portfolio.csv')

with open('../portfolio.csv', 'rb') as portfolio_csv:
	portfolio_reader = csv.reader(portfolio_csv, delimiter=' ', quotechar='|')
	portfolio = list(portfolio_reader)