import loan as loan_module
import portfolio as portfolio_module
import pprint

# DECLARE INPUTS:

# Accepted Grades

accepted_grades = {
	'A':1,
	'B':1,
	'C':0,
	'D':0,
	'E':0,
	'F':0
}

# Accepted Loan Length

accepted_lengths = {
	'6':1,
	'12':0,
	'18':0
}

# Accepted Loan Frequency

accepted_frequencies = {
	'Semanal':0,
	'Catorcenal':1,
	'Mensual':0
}

portfolio = portfolio_module.Portfolio(accepted_lengths = accepted_lengths, \
									 	accepted_frequencies = accepted_frequencies, \
									 	accepted_grades = accepted_grades)

portfolio_data = portfolio.get_data()

# TEST

print(portfolio_data)

for row in portfolio_data:
	test = loan_module.Loan(amount = row[1], length = row[2], frequency = row[3], grade = row[4])
	pprint.pprint(test.monthly_cash_flow())
	pprint.pprint(test.standardize_monthly_cash_flow())
