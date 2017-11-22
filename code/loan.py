from __future__ import division
import math

FREQUENCIES = {
	'Semanal': 52,
	'Catorcenal': 26,
	'Mensual': 12
}

INTEREST_RATES = {
	'A': .14,
	'B': .17,
	'C': .21,
	'D': .25,
	'E': .30,
	'F': .30
}

class Loan:

	def __init__(self, amount = 0, length = 0, frequency = '', grade = ''):
		self.amount = amount
		self.length = length
		self.frequency = frequency
		self.grade = grade

	def number_of_payments(self):
		duration_in_years = int(self.length) / 12

		return int(math.floor(FREQUENCIES[self.frequency] * duration_in_years))


	def cash_flow(self):
		cash_flow = []
