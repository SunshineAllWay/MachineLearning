#Back-Propagation Neural Networks

import math
import random
import string
import sys
import os
from time import clock

random.seed(0)

#calculate a random number where: a<=rand<b
def rand(a, b):
	return (b-a)*random.random() + a


#make a matrix 
def makeMatrix(I, J, fill=0.0):
	m = []
	for i in range(I):
		m.append([fill] * J)
	return m


#our sigmoid function, tanh is a litte nicer than the standard 1/(1 + e^-x)
def sigmoid(x):
	return 1 / (math.exp(-x) + 1)


def dsigmoid(y):
	return (y - y * y)


class BPANN:
	def __init__(self, ni, nh, no):
		self.ni = ni + 1
		self.nh = nh
		self.no = no

		#activation for nodes
		self.ai = [1.0] * self.ni
		self.ah = [1.0] * self.nh
		self.ao = [1.0] * self.no

		#create weights
		#size self.ni * self.nh
		self.wi = makeMatrix(self.ni, self.nh)
		self.wo = makeMatrix(self.nh, self.no)

		for i in range(self.ni):
			for j in range(self.nh):
				self.wi[i][j] = rand(-1, 1)

		for i in range(self.nh):
			for k in range(self.no):
				self.wo[i][k] = rand(-1.0, 1.0)

		#last change in weights
		self.ci = makeMatrix(self.ni, self.nh)
		self.co = makeMatrix(self.nh, self.no)


	def update(self, inputs):
		if len(inputs) != self.ni - 1:
			raise ValueError('wrong number of inputs')

		#input activation
		for i in range(self.ni - 1):
			self.ai[i] = inputs[i]

		#hidden activation
		for j in range(self.nh):
			sum = 0.0
			for i in range(self.ni):
				sum = sum + self.ai[i] * self.wi[i][j]
			self.ah[j] = sigmoid(sum)

		#output activation
		for k in range(self.no):
			sum = 0.0
			for j in range(self.nh):
				sum =  sum + self.ah[j] * self.wo[j][k]
			self.ao[k] = sigmoid(sum)

		return self.ao[:]


	#Back-Propagation
	def backPropagate(self, targets, N, M):
		if len(targets) != self.no:
			raise ValueError('wrong number of target values')

		#calculate error terms for output
		output_deltas = [0.0] * self.no
		for k in range(self.no):
			error = targets[k] - self.ao[k]
			output_deltas[k] = dsigmoid(self.ao[k]) * error

		#calculate error terms for hidden
		hidden_deltas = [0.0] * self.nh
		for j in range(self.nh):
			error = 0.0
			for k in range(self.no):
				error += output_deltas[k] * self.wo[j][k]
			hidden_deltas[j] = dsigmoid(self.ah[j]) * error

		#update output weights
		#N: learning rate
		#M: monentum factor
		for j in range(self.nh):
			for k in range(self.no):
				change = output_deltas[k] * self.ah[j]
				self.wo[j][k] += N * change + M * self.co[j][k]
				self.co[j][k] = change

		#update input weights
		for i in range(self.ni):
			for j in range(self.nh):
				change = hidden_deltas[j] * self.ai[i]
				self.wi[i][j] += N * change + M * self.ci[i][j]
				self.ci[i][j] = change

		#calculate error
		error = 0.0
		for k in range(len(targets)):
			error += 0.5 * (targets[k] - self.ao[k])**2

		return error


	#test
	def test(self, patterns):
		for p in patterns:
			print (p[0], '->', p[1], '->', self.update(p[0]))


	def train(self, patterns, iterations = 1000, N = 0.5, M = 0.1):
		for i in range(iterations):
			error = 0.0
			for p in patterns:
				inputs = p[0]
				targets = p[1]
				self.update(inputs)
				error += self.backPropagate(targets, N, M)
			if i % 100 == 0:
				print('error %-.5f' %(error))

def demo():
	pat = []
	for i in range(10):
		l = [i]
		p = [math.sin(i), 1]
		pat.append([l, p])	
		n = BPANN(1, 5, 2)
	n.train(pat, 1000, 0.6, 0.1)
	n.test(pat)


if __name__ == '__main__':
	demo()