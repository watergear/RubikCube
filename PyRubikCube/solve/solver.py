from .center_midpoint import *

class Solver:
	def __init__(self, problem):
		self.problem = problem

	def solve(self):
		solutions = []

		if self.problem.odd:
			solutions += CenterMidpointSolution(self.problem).solve()
		
		return solutions
