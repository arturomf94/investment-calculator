import portfolio as portfolio_module
import pprint
import loan as loan_module

# DECLARE INPUTS:

# Initial Investment Amount

investment_amount = 1000

# Accepted Grades

accepted_grades = {
	'A':0,
	'B':0,
	'C':0,
	'D':0,
	'E':0,
	'F':1
}

# Accepted Loan Length

accepted_lengths = {
	'6':1,
	'12':0,
	'18':0
}

# Accepted Loan Frequency

accepted_frequencies = {
	'Semanal':1,
	'Catorcenal':1,
	'Mensual':0
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
print('CAPITAL RETURNED')
capital_returned_list = []
for i in range(0,18):
	capital_returned_list.append(portfolio_summary[i][2])
print(capital_returned_list)
print(sum(capital_returned_list))

# test_loan = loan_module.Loan(portfolio_data[0][1], portfolio_data[0][2], portfolio_data[0][3], portfolio_data[0][4])

# print('### TEST LOAN ###')
# print('# CASH FLOW #')
# pprint.pprint(test_loan.cash_flow())
# print('# MONTHLY CASH FLOW #')
# pprint.pprint(test_loan.monthly_cash_flow())
# print('# STANDARDIZED CASH FLOW #')
# pprint.pprint(test_loan.standardize_monthly_cash_flow())

