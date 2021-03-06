from ..base.symbol import *

from .solver import *

TX0		= T("X+", 0)
TX0_	= T("X-", 0)
TY0		= T("Y+", 0)
TY0_	= T("Y-", 0)
TZ0		= T("Z+", 0)
TZ0_	= T("Z-", 0)

class CenterMidpointSolver(Solver):
	def get_solutions_W(self, n):
		return {
			( W(0,0,n),
				W(0,n,0) ) :
			[TX0],

			( W(0,0,-n),
				W(0,n,0) ) :
			[TX0_],
			
			( W(n,0,0),
				W(0,n,0) ) :
			[TZ0_],

			( W(-n,0,0),
				W(0,n,0) ) :
			[TZ0],

			( W(0,-n,0),
				W(0,n,0) ) :
			[TX0, TX0],
		}

	def get_solutions_WV(self, n):
		TYn		= T("Y+", n)
		TYn_	= T("Y-", n)

		return {
			( (W(0,n,0), V('Z','Y','-X')),
				(W(0,n,0), V_XYZ) ) :
			[TYn],
			
			( (W(0,n,0), V('-Z','Y','X')),
				(W(0,n,0), V_XYZ) ) :
			[TYn_],
			
			( (W(0,n,0), V('-X','Y','-Z')),
				(W(0,n,0), V_XYZ) ) :
			[TYn, TYn],
		}

	def solve(self, problem):
		n = problem.n
		solutions = []

		solutionsW_map = self.get_solutions_W(n)
		smt_list = [
			SMT_RZ
		]
		W_check = W(0,n,0)
		solutions += self.solveW_smt(problem, W_check, solutionsW_map, smt_list)

		solutionsWV_map = self.get_solutions_WV(n)
		smt_list = [
			SMT_MY,
			SMT_RX,
			SMT_RY,
			SMT_RY,
			SMT_RY,
		]
		W_check = W(0,n,0)
		V_check = V_XYZ
		solutions += self.solveWV_smt(problem, W_check, V_check, solutionsWV_map, smt_list)

		return solutions
