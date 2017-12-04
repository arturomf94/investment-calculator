from __future__ import division
from misc import portfolio
import loan as loan_module
import datetime

class Portfolio:

	def __init__(self, accepted_lengths = {}, accepted_frequencies = {}, accepted_grades = {}):
		self.accepted_lengths = accepted_lengths
		self.accepted_frequencies = accepted_frequencies
		self.accepted_grades = accepted_grades

	def get_data(self):
		accepted_lengths = self.accepted_lengths
		accepted_frequencies = self.accepted_frequencies
		accepted_grades = self.accepted_grades

		filtered_lengths = [
			length
			for length in accepted_lengths
			if accepted_lengths[length] == 1
		]

		filtered_frequencies = [
			frequency
			for frequency in accepted_frequencies
			if accepted_frequencies[frequency] == 1
		]

		filtered_grades = [
			grade 
			for grade in accepted_grades 
			if accepted_grades[grade] == 1
		]

		filtered_data = [
			row
			for row in portfolio
			if row[4] in filtered_grades
			if row[2] in filtered_lengths
			if row[3] in filtered_frequencies
		]

		return filtered_data

	def get_summary(self, investment_amount):
		summary = []
		data = self.get_data()
		portfolio_length = len(data)
		individual_investment_amount = investment_amount / portfolio_length

		for i in range(1,19):
			summary.append([datetime.date.today() + datetime.timedelta((i-1)*365/12),0,0,0,0])

		for row in data:
			loan = loan_module.Loan(amount = row[1], length = row[2], frequency = row[3], grade = row[4])
			loan_proportion = individual_investment_amount / float(loan.amount)
			cash_flow = loan.standardize_monthly_cash_flow()
			for month in cash_flow:
				summary[cash_flow.index(month)][1] = summary[cash_flow.index(month)][1] + month[0] * loan_proportion # Payment
				summary[cash_flow.index(month)][2] = summary[cash_flow.index(month)][2] + month[1] * loan_proportion # Capital
				summary[cash_flow.index(month)][3] = summary[cash_flow.index(month)][3] + month[2] * loan_proportion # Interest
				summary[cash_flow.index(month)][4] = summary[cash_flow.index(month)][4] + month[3] * loan_proportion # VAT

		return summary
