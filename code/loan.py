from __future__ import division
import math

FREQUENCIES = {
	'Semanal': [52,4],
	'Catorcenal': [26,2],
	'Mensual': [12,1]
}

ANNUAL_INTEREST_RATES = {
	'A': .14,
	'B': .17,
	'C': .21,
	'D': .25,
	'E': .30,
	'F': .30
}

VAT = .16

class Loan:

	def __init__(self, amount = 0, length = 0, frequency = '', grade = ''):
		self.amount = amount
		self.length = length
		self.frequency = frequency
		self.grade = grade

	def number_of_payments(self):
		duration_in_years = int(self.length) / 12

		return int(math.floor(FREQUENCIES[self.frequency][0] * duration_in_years))

	def interest_rate_with_vat(self, interest_rate):

		return interest_rate * (1 + VAT)

	def interest_rate(self):

		return ANNUAL_INTEREST_RATES[self.grade] / FREQUENCIES[self.frequency][0]

	def period_payment(self):
		amount = float(self.amount)
		number_of_payments = self.number_of_payments()
		interest_rate_with_vat = self.interest_rate_with_vat(self.interest_rate())

		return (amount * interest_rate_with_vat) / (1 - math.pow(1 + interest_rate_with_vat, -number_of_payments))

	def cash_flow(self):
		cash_flow = []
		initial_balance = float(self.amount)
		period_balance = initial_balance
		period_payment = self.period_payment()
		number_of_payments = self.number_of_payments()
		interest_rate = self.interest_rate()
		interest_rate_with_vat = self.interest_rate_with_vat(interest_rate)

		for i in range(1, number_of_payments + 1):
			period_interest = interest_rate * period_balance
			period_interest_with_vat = interest_rate_with_vat * period_balance
			period_vat = period_interest_with_vat - period_interest
			period_capital = period_payment - period_interest_with_vat
			period_flow = [period_payment, period_capital, period_interest, period_vat]
			period_balance = period_balance * (1 + interest_rate_with_vat) - period_payment
			cash_flow.append(period_flow)

		return cash_flow

	def monthly_cash_flow(self):
		cash_flow = self.cash_flow()
		number_of_payments = self.number_of_payments()
		monthly_periods = FREQUENCIES[self.frequency][1]

		if self.frequency != 'Mensual':
			new_cash_flow = []
			months = number_of_payments // monthly_periods

			for i in range(1, months + 1):
				period_counter = i * monthly_periods
				monthly_payment = 0
				monthly_capital = 0
				monthly_interest = 0
				monthly_vat = 0

				for k in range(1, monthly_periods + 1):
					monthly_payment = monthly_payment + cash_flow[period_counter - k][0]
					monthly_capital = monthly_capital + cash_flow[period_counter - k][1]
					monthly_interest = monthly_interest + cash_flow[period_counter - k][2]
					monthly_vat = monthly_vat + cash_flow[period_counter - k][3]

				monthly_cash_flow = [monthly_payment, monthly_capital, monthly_interest, monthly_vat]
				new_cash_flow.append(monthly_cash_flow)

				if (i == months and period_counter < number_of_payments):
					monthly_payment = 0
					monthly_capital = 0
					monthly_interest = 0
					monthly_vat = 0

					for j in range(period_counter, number_of_payments):
						monthly_payment = monthly_payment + cash_flow[j][0]
						monthly_capital = monthly_capital + cash_flow[j][1]
						monthly_interest = monthly_interest + cash_flow[j][2]
						monthly_vat = monthly_vat + cash_flow[j][3]

					monthly_cash_flow = [monthly_payment, monthly_capital, monthly_interest, monthly_vat]
					new_cash_flow.append(monthly_cash_flow)

			cash_flow = new_cash_flow

		return cash_flow


	# NOTE: 
	# The length of the monthly cash flow of a loan may not match its actual
	# loan length if the loan frequency is not monthly. For example, if a loan
	# is made for 3 months with weekly payments, there will actually be 13 payments, 
	# instead of 12 (4 * 3). Thus, this function 'standardizes' monthly cash flows
	# in order for them to have the same length as the actual loan.

	def standardize_monthly_cash_flow(self):
		monthly_cash_flow = self.monthly_cash_flow()
		real_length = int(self.length)
		cash_flow_length = len(monthly_cash_flow)

		if cash_flow_length != real_length:
			length_difference = cash_flow_length - real_length
			payment_difference = 0
			capital_difference = 0
			interest_difference = 0
			vat_difference = 0
			
			for i in range(1, length_difference + 1):
				payment_difference = payment_difference + monthly_cash_flow[cash_flow_length - i][0]
				capital_difference = capital_difference + monthly_cash_flow[cash_flow_length - i][1]
				interest_difference = interest_difference + monthly_cash_flow[cash_flow_length - i][2]
				vat_difference = vat_difference + monthly_cash_flow[cash_flow_length - i][3]

			payment_difference = payment_difference / real_length
			capital_difference = capital_difference / real_length
			interest_difference = interest_difference / real_length
			vat_difference = vat_difference / real_length

			for j in range(0, real_length):
				monthly_cash_flow[j][0] = monthly_cash_flow[j][0] + payment_difference
				monthly_cash_flow[j][1] = monthly_cash_flow[j][1] + capital_difference
				monthly_cash_flow[j][2] = monthly_cash_flow[j][2] + interest_difference
				monthly_cash_flow[j][3] = monthly_cash_flow[j][3] + vat_difference

			del monthly_cash_flow[real_length:]

		return monthly_cash_flow