import csv
import os

# Import Data

with open('/Users/Arturo/Desktop/GitHub/investment-calculator/portfolio.csv', 'rb') as portfolio_csv:
	portfolio_reader = csv.reader(portfolio_csv, delimiter=',')
	portfolio = list(portfolio_reader)