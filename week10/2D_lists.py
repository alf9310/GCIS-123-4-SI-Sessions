"""
Activities for Session 10A: 2D lists
@author: Audrey Fuller
@author: Zoe Bingham
"""

def make_board(size):
	"""
	Make a board of size. Store O and X in every other tile
	"""
	a_list = []
	return a_list

def print_board(a_list):
	"""
	Print the board.
	"""
	return


def main():
	# use list comprehension to make a list of values from 1-50
	num_list = [x for x in range(1, 51)]
	print(num_list)
	# use list comprehension to make a list of values A-Z
	print([char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
	print(['char' for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])

	# use list comprehension to make a list of lists that hold increasing values
	num_list = [[i for i in range(5)] for j in range(5)]
	print(num_list)

	# make a board
	board = make_board(4)
	print_board(board)


if __name__ == "__main__":
	main()