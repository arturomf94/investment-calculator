from misc import portfolio

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

filtered_grades = [
	grade 
	for grade in accepted_grades 
	if accepted_grades[grade] == 1
]

# Accepted Loan Length

accepted_lengths = {
	'6':1,
	'12':0,
	'18':0
}

filtered_lengths = [
	length
	for length in accepted_lengths
	if accepted_lengths[length] == 1
]

# Accepted Loan Frequency

accepted_frequencies = {
	'Semanal':0,
	'Catorcenal':0,
	'Mensual':1
}

filtered_frequencies = [
	frequency
	for frequency in accepted_frequencies
	if accepted_frequencies[frequency] == 1
]

# FILTER DATA:

filtered_data = []

filtered_data = [
	row
	for row in portfolio
	if row[4] in filtered_grades
	if row[2] in filtered_lengths
	if row[3] in filtered_frequencies
]
