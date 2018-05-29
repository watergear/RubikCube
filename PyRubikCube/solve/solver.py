from .center_midpoint import *
from .firstlayer_edge_midpoint import *

class Solver:
	def __init__(self, problem):
		self.problem = problem

	def solve(self):
		solutions = []

		if self.problem.odd:
			print("====CenterMidpointSolution====")
			solutions += CenterMidpointSolution(self.problem).solve()
		
		print("====FirstLayerEdgeMidpointSolution====")
		solutions += FirstLayerEdgeMidpointSolution(self.problem).solve()

		return solutions
