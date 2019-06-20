import random
import os
import time
import cProfile

# Conway's Game of Life
# Torodial Array
class Game():
	def __init__(self, n_rows, chance_zero):
		self.n_rows = n_rows
		self.chance_zero = chance_zero
		self.board = []
		self.gen = 0

	def print_board(self):
		print("Gen: " + str(self.gen))
		for row in range(len(self.board)): 
			print(self.board[row])

	def return_board(self):
		return self.board
		
	def create_board(self):
		board = []
		for row in range(self.n_rows):
			self.board.append([])
			for col in range(self.n_rows):
				rand = random.uniform(0, 1)
				val = 0
				if rand >= self.chance_zero: val = 1
				self.board[row].append(val)


	def live_helper(self, row, col, visited, i, j, num):
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		return num
	# Live neighbors
	def get_live(self, row, col, visited):
		num = 0
		i = -1
		j = -1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = -1
		j = 0
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = -1
		j = 1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = 0
		j = -1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = 1
		j = -1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = 0
		j = 1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = 1
		j = 0
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		i = 1
		j = 1
		#num = self.live_helper(row, col, visited, i, j, num)
		r = row + i
		c = col + j
		if r < 0: r += len(self.board)
		elif r > len(self.board) - 1: r -= len(self.board)
		if c < 0: c += len(self.board)
		elif c > len(self.board) - 1: c -= len(self.board)
		val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		if val == 1: num += 1
		
		# num2 = 0
		# for i in range(-1, 2):
		# 	for j in range(-1, 2):
		# 		if not (i == 0 and j == 0):
		# 			r = row + i
		# 			c = col + j
		# 			if r < 0: r += len(self.board)
		# 			elif r > len(self.board) - 1: r -= len(self.board)
		# 			if c < 0: c += len(self.board)
		# 			elif c > len(self.board) - 1: c -= len(self.board)
		# 			val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
		# 			if val == 1: num2 += 1
		# if num2 != num: print("MISTAKE")
		return num

	def next_gen(self):
		self.gen += 1
		visited = {}
		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				n  = self.get_live(row,col,visited)
				#print(n, end=" ")
				visited[(row, col)] = self.board[row][col]
				if self.board[row][col] == 1:
					if n < 2 or n > 3: self.board[row][col] = 0
				else: 
					if n == 3: self.board[row][col] = 1
# c = Game(800, .75)
# c.create_board()
# c.next_gen()
# cProfile.run('c.next_gen()')
