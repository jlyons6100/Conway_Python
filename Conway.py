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
				
	def get_live(self, row, col, visited):
		num = 0
		for (i, j) in ((-1,-1),(-1,0),(-1,1),(0,-1),(1,-1),(0,1),(1,0),(1,1)):
			r = row + i
			c = col + j
			if r < 0: r += len(self.board)
			elif r > len(self.board) - 1: r -= len(self.board)
			if c < 0: c += len(self.board)
			elif c > len(self.board) - 1: c -= len(self.board)
			val = self.board[r][c] if not (r,c) in visited else visited[(r,c)]
			if val == 1: num += 1
		return num

	def next_gen(self):
		self.gen += 1
		visited = {}
		for row in range(len(self.board)):
			for col in range(len(self.board[0])):
				n  = self.get_live(row,col,visited)
				visited[(row, col)] = self.board[row][col]
				if self.board[row][col] == 1:
					if n < 2 or n > 3: self.board[row][col] = 0
				else: 
					if n == 3: self.board[row][col] = 1
# c = Game(50, .75)
# c.create_board()
# for _ in range(50):
# 	c.next_gen()
# 	c.print_board()
# # c.next_gen()
# cProfile.run('c.next_gen()',sort=1)
