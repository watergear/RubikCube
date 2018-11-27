from ..base.transform import *
from ..base.symbol import *

from .solver import *

def edge_i(n, i):
	return [
		T("X+", i),
		T("Y+", n),
		T("Y+", n),
		T("X-", i),
		T("Y+", n),
		T("Y+", n),
		T("X+", -i),
		T("Y+", n),
		T("Y+", n),
		T("X+", i),
		T("Y+", n),
		T("Y+", n),
		T("X-", i),
		T("Y+", n),
		T("Y+", n),
		T("X-", -i),
		T("Y+", n),
		T("Y+", n),
	]

class EdgeSolver(Solver):
	def get_solutions_W(self, n, i):
		if 0 == i:
			return {}

		tEdge = edge_i(n, i)
		tEdgeInverse = inverse_transforms(tEdge)

		tEdge_ObliqueNX = smt_conjugate_transforms(SMT_ONX, tEdge)
		tEdgeInverse_ObliqueNX = smt_conjugate_transforms(SMT_ONX, tEdgeInverse)

		tEdge_MirrorZ = smt_conjugate_transforms(SMT_MZ, tEdge)

		return {
			# on UB edge
			( W(i,n,n),
				W(i,n,-n) ) :
			tEdge,

			( W(-i,n,n),
				W(i,n,-n) ) :
			tEdgeInverse,

			# on LB edge
			( W(-n,i,n),
				W(i,n,-n) ) :
			[T("Z+", n)] +
			tEdge +
			[T("Z-", n)],

			( W(-n,-i,n),
				W(i,n,-n) ) :
			[T("Z+", n)] +
			tEdgeInverse +
			[T("Z-", n)],
			
			# on RB edge
			( W(n,-i,n),
				W(i,n,-n) ) :
			[T("Z-", n)] +
			tEdge +
			[T("Z+", n)],

			( W(n,i,n),
				W(i,n,-n) ) :
			[T("Z-", n)] +
			tEdgeInverse +
			[T("Z+", n)],

			# on DB edge
			( W(-i,-n,n),
				W(i,n,-n) ) :
			[T("Z+", n),T("Z+", n)] +
			tEdge +
			[T("Z-", n),T("Z-", n)],

			( W(i,-n,n),
				W(i,n,-n) ) :
			[T("Z+", n),T("Z+", n)] +
			tEdgeInverse +
			[T("Z-", n),T("Z-", n)],

			# on LU edge
			( W(-n,n,-i),
				W(i,n,-n) ) :
			[T("X-", -n)] +
			[T("Z+", n)] +
			tEdge +
			[T("Z-", n)] +
			[T("X+", -n)],

			( W(-n,n,i),
				W(i,n,-n) ) :
			[T("X-", -n)] +
			[T("Z+", n)] +
			tEdgeInverse +
			[T("Z-", n)] +
			[T("X+", -n)],

			# on RU edge
			( W(n,n,i),
				W(i,n,-n) ) :
			[T("X-", n)] +
			[T("Z-", n)] +
			tEdge +
			[T("Z+", n)] +
			[T("X+", n)],

			( W(n,n,-i),
				W(i,n,-n) ) :
			[T("X-", n)] +
			[T("Z-", n)] +
			tEdgeInverse +
			[T("Z+", n)] +
			[T("X+", n)],

			# on LD edge
			( W(-n,-n,i),
				W(i,n,-n) ) :
			[T("X+", -n)] +
			[T("Z+", n)] +
			tEdge +
			[T("Z-", n)] +
			[T("X-", -n)],

			( W(-n,-n,-i),
				W(i,n,-n) ) :
			[T("X+", -n)] +
			[T("Z+", n)] +
			tEdgeInverse +
			[T("Z-", n)] +
			[T("X-", -n)],

			# on RD edge
			( W(n,-n,-i),
				W(i,n,-n) ) :
			[T("X+", n)] +
			[T("Z-", n)] +
			tEdge +
			[T("Z+", n)] +
			[T("X-", n)],

			( W(n,-n,i),
				W(i,n,-n) ) :
			[T("X+", n)] +
			[T("Z-", n)] +
			tEdgeInverse +
			[T("Z+", n)] +
			[T("X-", n)],

			# on LF edge
			( W(-n,-i,-n),
				W(i,n,-n) ) :
			[T("X+", -n),T("X+", -n)] +
			[T("Z+", n)] +
			tEdge +
			[T("Z-", n)] +
			[T("X-", -n),T("X-", -n)],

			( W(-n,i,-n),
				W(i,n,-n) ) :
			[T("X+", -n),T("X+", -n)] +
			[T("Z+", n)] +
			tEdgeInverse +
			[T("Z-", n)] +
			[T("X-", -n),T("X-", -n)],

			# on RF edge
			( W(n,i,-n),
				W(i,n,-n) ) :
			[T("X+", n),T("X+", n)] +
			[T("Z-", n)] +
			tEdge +
			[T("Z+", n)] +
			[T("X-", n),T("X-", n)],

			( W(n,-i,-n),
				W(i,n,-n) ) :
			[T("X+", n),T("X+", n)] +
			[T("Z-", n)] +
			tEdgeInverse +
			[T("Z+", n)] +
			[T("X-", n),T("X-", n)],

			# on DF edge
			( W(i,-n,-n),
				W(i,n,-n) ) :
			tEdge_ObliqueNX,

			( W(-i,-n,-n),
				W(i,n,-n) ) :
			tEdgeInverse_ObliqueNX,

			# on UF edge, shift RU edge
			( W(i,n,-n),
				W(i,n,-n) ) :
			[],

			( W(-i,n,-n),
				W(i,n,-n) ) :
			[T("X-", n)] +
			[T("Z-", n)] +
			tEdge_MirrorZ +
			[T("Z+", n)] +
			[T("X+", n)],
		}

	def solve(self, problem):
		n = problem.n
		solutions = []

		Ws_check = []
		solutionsWs_map = []
		lower = -n+1
		upper = n-1
		for i in range(lower, upper+1):
			Ws_check += [W(i,n,-n)]
			solutionsWs_map += [self.get_solutions_W(n, i)]

		smt_init_list = [
			SMT_RX,  # UF,RU -> DF,RF
		]
		Ws_check, solutionsWs_map = conjugate_check_solutions_W(Ws_check, solutionsWs_map, smt_init_list)

		smt_list = [
			SMT_RY,  # DF,RF -> RD,RB
			SMT_RY,  # RD,RB -> DB,LB
			SMT_RY,  # DB,LB -> LD,LF
			SMT_RNX, # LD,LF -> LF,LU
			SMT_RY,  # LF,LU -> RF,UF
			SMT_RY,  # RF,UF -> RB,RU
			SMT_RY,  # RB,RU -> LB,UB
			SMT_RX,  # LB,UB -> LU,UF
			SMT_RY,  # LU,UF -> UF,RU
			SMT_RY,  # UF,RU -> RU,UB
			SMT_RY,  # RU,UB -> UB,LU
		]
		solutions += self.solveWs_smt(problem, Ws_check, solutionsWs_map, smt_list)

		return solutions
