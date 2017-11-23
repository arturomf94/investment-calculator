from __future__ import division
import math

FREQUENCIES = {
	'Semanal': 52,
	'Catorcenal': 26,
	'Mensual': 12
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

		return int(math.floor(FREQUENCIES[self.frequency] * duration_in_years))

	def interest_rate_with_vat(self, interest_rate):

		return interest_rate * (1 + VAT)

	def interest_rate(self):

		return ANNUAL_INTEREST_RATES[self.grade] / FREQUENCIES[self.frequency]

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
