import portfolio as portfolio_module
import pprint
import loan as loan_module
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

# DECLARE INPUTS:

# Initial Investment Amount

investment_amount = 10000

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
	'6':0,
	'12':0,
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

# Extract Payments, Capital, Interest and VAT

payment = []
capital = []
interest = []
vat = []
mes = []

for i in range(0,18):
	payment.append(portfolio_summary[i][1])
	capital.append(portfolio_summary[i][2])
	interest.append(portfolio_summary[i][3])
	vat.append(portfolio_summary[i][4])
	mes.append(i + 1)


# Plot Capital

plt.bar(mes, capital, align='center', alpha=0.5)
plt.xlabel('Mes')
plt.xticks(mes,mes)
plt.ylabel('$')
plt.title('Capital')

plt.show()


# # TEST
# print('PORTFOLIO')
# pprint.pprint(portfolio_data)
# print('MONTHLY CASH FLOW')
# pprint.pprint(portfolio_summary)
# print('CAPITAL RETURNED')
# capital_returned_list = []
# for i in range(0,18):
# 	capital_returned_list.append(portfolio_summary[i][2])
# print(capital_returned_list)
# print(sum(capital_returned_list))

# test_loan = loan_module.Loan(portfolio_data[1][1], portfolio_data[1][2], portfolio_data[1][3], portfolio_data[1][4])

# print('### TEST LOAN ###')
# print('# CASH FLOW #')
# pprint.pprint(test_loan.cash_flow())
# print('# MONTHLY CASH FLOW #')
# pprint.pprint(test_loan.monthly_cash_flow())
# print('# STANDARDIZED CASH FLOW #')
# pprint.pprint(test_loan.standardize_monthly_cash_flow())

