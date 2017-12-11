from functools import reduce


def invert(text):
	if text == "n":
		return "s"
	if text == "s":
		return "n"
	if text == "ne":
		return "sw"
	if text == "nw":
		return "se"
	if text == "se":
		return "nw"
	if text == "sw":
		return "ne"

def remove_one_pair_of_inverts(vector):
	for x in vector:
		inv = invert(x)
		if inv in vector:
			vector.remove(x)
			vector.remove(inv)
			return vector
	return vector
			

def task1(vectors):
	res = vectors
	for i in range(len(vectors)):
		res = remove_one_pair_of_inverts(res)
		
	return len(res)


def task2():
	print()
