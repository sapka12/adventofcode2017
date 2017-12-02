import csv

def read_tab_file():
	with open('input.txt', 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		return [row for row in list(reader)]
        
def check_sum(data):
	return sum([ (max(map(int, row)) - min(map(int, row)))  for row in data])

print(check_sum(read_tab_file()))
