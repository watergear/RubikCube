from .center_midpoint import *
from .firstlayer_edge_midpoint import *

class Solver:
	def __init__(self):
		pass

	def solve(self, problem):
		solutions = []

		if problem.odd:
			print("====CenterMidpointSolution====")
			solutions += CenterMidpointSolution().solve(problem)
		
		print("====FirstLayerEdgeMidpointSolution====")
		solutions += FirstLayerEdgeMidpointSolution().solve(problem)

		return solutions
