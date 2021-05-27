#! usr/bin/python

import sys

class Heap(object):

	def __init__(self):
		self.lower = []
		self.upper = []

	def find_parent(self, index):
		if index == 0:
			return -1

		if index % 2 == 0:
			return (index-2)//2

		return (index-1)//2

	def max_up(self, c, t):
		self.lower[c], self.lower[t] = self.lower[t], self.lower[c]
		c = t

		while True:
			parent_index = self.find_parent(c)

			if parent_index == -1:
				break

			if self.lower[parent_index] > self.lower[c]:
				break

			t = parent_index

			self.lower[c], self.lower[t] = self.lower[t], self.lower[c]
			c = t

	def max_insert(self, value):
		self.lower.append(value)
		parent_index = self.find_parent(len(self.lower) - 1)
        
		if parent_index != -1:
			if self.lower[parent_index] < value:
				self.max_up(len(self.lower)-1, parent_index)

	def min_up(self, c, t):
		self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
		c = t

		while True:
			parent_index = self.find_parent(c)

			if parent_index == -1:
				break

			if self.upper[parent_index] < self.upper[c]:
				break

			t = parent_index

			self.upper[c], self.upper[t] = self.upper[t], self.upper[c]
			c = t

	def find_min_child(self, index):
		l = (index*2) + 1
		r = (index*2) + 2
		if l >= len(self.upper) and r >= len(self.upper):
			return -1
		if l >= len(self.upper):
			return r

		if r >= len(self.upper):
			return l

		return l if self.upper[l] < self.upper[r] else r

	def find_max_child(self, index):
		l = (index*2) + 1
		r = (index*2) + 2
		if l >= len(self.lower) and r >= len(self.lower):
			return -1
		if l >= len(self.lower):
			return r

		if r >= len(self.lower):
			return l

		return l if self.lower[l] > self.lower[r] else r

	def max_pop(self):
		pop_value = self.lower[0]

		self.lower[0] = self.lower.pop()

		n_i = 0
		while True:
			r_i = self.find_max_child(n_i)
			if r_i == -1:
				break
			if self.lower[n_i] < self.lower[r_i]:
				self.lower[n_i], self.lower[r_i] = self.lower[r_i], self.lower[n_i]
				n_i = r_i
			else:
				break

		return pop_value

	def min_pop(self):
		pop_value = self.upper[0]
		self.upper[0] = self.upper.pop()

		n_i = 0
		while True:
			r_i = self.find_min_child(n_i)
			if r_i == -1:
				break
			if self.upper[n_i] > self.upper[r_i]:
				self.upper[n_i], self.upper[r_i] = self.upper[r_i], self.upper[n_i]
				n_i = r_i
			else:
				break

		return pop_value

	def balance(self):
		if abs(len(self.lower) - len(self.upper)) >= 2:
			if len(self.upper) < len(self.lower):
				self.min_insert(self.max_pop())
			else:
				self.max_insert(self.min_pop())


	def min_insert(self, value):
		self.upper.append(value)
		parent_index = self.find_parent(len(self.upper) - 1)

		if parent_index != -1:
			if self.upper[parent_index] > value:
				self.min_up(len(self.upper)-1, parent_index)

	def median(self):
		if len(self.lower) == len(self.upper):
			return (float(self.lower[0]) + float(self.upper[0]))/2.0
		elif len(self.lower) > len(self.upper):
			return float(self.lower[0])
		else:
			return float(self.upper[0])

	def insert(self, value):
		if len(self.lower) == 0 or value < self.lower[0]:
			self.max_insert(value)
		else:
			self.min_insert(value)

		self.balance()

		return self.median()

	def minmax(self):
		print (self.lower)
		print (self.upper)

input_file = open("STDIN", "r")

#Counting Number of lines in input file
ln = 0
for i in input_file.read().split("\n"):
    if i:
        ln += 1

#Moving cursor to top of the file
input_file.seek(0,0)

a = []
a_i = 0
for a_i in range(ln):
	a_t = int(input_file.readline().strip())
	a.append(a_t)

heap = Heap()

for number in a:
	mean = heap.insert(number)
	print ("%.1f" % mean)

input_file.close();