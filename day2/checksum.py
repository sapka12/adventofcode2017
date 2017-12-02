import csv

def read_tab_file():
	with open('input.txt', 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		return [row for row in list(reader)]


def check_sum(data):
	
	def row_sum(row):
		int_row = map(int, row)
		return (max(int_row) - min(int_row))
	
	return sum([ row_sum(row)  for row in data])

#print(check_sum(read_tab_file()))


def check_sum2(data):
	
	def row_sum(row):
		int_row = map(int, row)
		row_range = range(len(row))
		
		for a in row_range:
			for b in row_range:
				if a != b and int_row[b] != 0 and int_row[a] % int_row[b] == 0:
					aa = int_row[a]
					bb = int_row[b]
					return aa // bb
	
	return sum([ row_sum(row)  for row in data])


print(read_tab_file())

print(check_sum2(read_tab_file()))

