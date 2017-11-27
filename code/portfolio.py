from misc import portfolio

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