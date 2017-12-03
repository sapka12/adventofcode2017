def maximum(arr):
    return max([max(a) for a in arr])

def generate_square(x):
	size = 2 * x + 1
	square = [[None] * size for i in range(size) ]
    #fill square
	return square

def manhattan_disatance(pos1, pos2):
    (pos1x, pos1y) = pos1
    (pos2x, pos2y) = pos2
    return abs(pos1x - pos2x) + abs(pos1y - pos2y)

def pos_of_val(arr, value):
    for x in range(arr):
        for y in range(arr[x]):
            if arr[x][y] == value:
                return (x, y)

def get_distance_from_1(arr, value):
    pos_1 = pos_of_val(arr, 1)
    pos_val = pos_of_val(arr, value)
    return manhattan_disatance(pos_1, pos_val)