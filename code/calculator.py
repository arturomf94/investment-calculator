import portfolio as portfolio_module
import pprint

# DECLARE INPUTS:

# Initial Investment Amount

investment_amount = 1000

# Accepted Grades

accepted_grades = {
	'A':1,
	'B':1,
	'C':1,
	'D':1,
	'E':1,
	'F':1
}

# Accepted Loan Length

accepted_lengths = {
	'6':1,
	'12':1,
	'18':1
}

# Accepted Loan Frequency

accepted_frequencies = {
	'Semanal':1,
	'Catorcenal':1,
	'Mensual':1
}

portfolio = portfolio_module.Portfolio(accepted_lengths = accepted_lengths, \
									 	accepted_frequencies = accepted_frequencies, \
									 	accepted_grades = accepted_grades)

portfolio_data = portfolio.get_data()

portfolio_summary = portfolio.get_summary(investment_amount = investment_amount)

# TEST
print('PORTFOLIO')
pprint.pprint(portfolio_data)
print('MONTHLY CASH FLOW')
pprint.pprint(portfolio_summary)

