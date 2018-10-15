from .center_midpoint import *
from .firstlayer_edge_midpoint import *

class RubikSolver:
	def __init__(self):
		pass

	def solve(self, problem):
		solutions = []

		if problem.odd:
			print("====CenterMidpointSolver====")
			solutions += CenterMidpointSolver().solve(problem)
		
		print("====FirstLayerEdgeMidpointSolver====")
		solutions += FirstLayerEdgeMidpointSolver().solve(problem)

		return solutions
