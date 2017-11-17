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

# Accepted Loan Length

accepted_length = {
	'6':1,
	'12':0,
	'18':0
}

# FILTER DATA:

filtered_data = []

filtered_grades = [
	grade 
	for grade in accepted_grades 
	if accepted_grades[grade] == 1
]

filtered_lengths = [
	length
	for length in accepted_length
	if accepted_length[length] == 1
]

filtered_data = [
	row
	for row in portfolio
	if row[4] in filtered_grades
	if row[2] in filtered_lengths
]