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
	'Catorcenal':0,
	'Mensual':0
}

portfolio = portfolio_module.Portfolio(accepted_lengths = accepted_lengths, \
									 	accepted_frequencies = accepted_frequencies, \
									 	accepted_grades = accepted_grades)

portfolio_data = portfolio.get_data()

portfolio_summary = portfolio.get_summary(investment_amount = investment_amount)

# Extract Payments, Capital, Interest and VAT

payment = []
accumulated_payment = []
capital = []
accumulated_capital = []
interest = []
accumulated_interest = []
vat = []
accumulated_vat = []
mes = []

for i in range(0,18):
	payment.append(portfolio_summary[i][1])
	capital.append(portfolio_summary[i][2])
	interest.append(portfolio_summary[i][3])
	vat.append(portfolio_summary[i][4])
	mes.append(i + 1)
	accumulated_payment.append(sum(payment))
	accumulated_capital.append(sum(capital))
	accumulated_interest.append(sum(interest))
	accumulated_vat.append(sum(vat))


# Plot Accumulated Capital and Interest 
accumulated_capital_subplot = plt.bar(mes, accumulated_capital, align = 'center', alpha = 0.5)
accumulated_interest_subplot = plt.bar(mes, accumulated_interest, align = 'center', \
										bottom = accumulated_capital, alpha = 0.5)

plt.ylabel('Pesos')
plt.xlabel('Mes')
plt.title('Capital e Interes Acumulado')
plt.xticks(mes,mes)
plt.legend((accumulated_capital_subplot[0], accumulated_interest_subplot[0]), ('Capital', 'Interest'))

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

