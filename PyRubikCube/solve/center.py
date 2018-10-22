from ..base.symbol import *

from .solver import *

def center_i_i(n, i):
	return [
		T("Y+", n),
		T("X-", i),
		T("X-", -i),
		T("Y+", n),
		T("X+", -i),
		T("Y-", n),
		T("X+", i),
		T("Y+", n),
		T("X-", -i),
		T("Y-", n),
		T("X+", -i),
		T("Y-", n),
	]

def center_i_j(n, i, j):
	return [
		T("Y-", n),
		T("X-", i),
		T("X-", j),
		T("Y-", n),
		T("X+", j),
		T("Y+", n),
		T("X+", i),
		T("Y-", n),
		T("X-", j),
		T("Y+", n),
		T("X+", j),
		T("Y+", n),
	]

class CenterSolver(Solver):
	def get_solutions_W(self, n, i, j):
		if 0 == i and 0 == j:
			return {}

		if i == j:
			tCenter = center_i_i(n, i)
		else:
			tCenter = center_i_j(n, i, j)

		tCenter_RotationZ = smt_conjugate_transforms(SMT_RZ, tCenter)
		tCenter_RotationNZ = smt_conjugate_transforms(SMT_RNZ, tCenter)
		tCenter_Rotation2Z = smt_conjugate_transforms(SMT_R2Z, tCenter)

		tCenter_RotationNX = smt_conjugate_transforms(SMT_RNX, tCenter)

		return {
			# on U face
			( W(i,n,j),
				W(i,j,-n) ) :
			tCenter,

			( W(j,n,-i),
				W(i,j,-n) ) :
			[T("Y+", n)] +
			tCenter +
			[T("Y-", n)],

			( W(-i,n,-j),
				W(i,j,-n) ) :
			[T("Y+", n),T("Y+", n)] +
			tCenter +
			[T("Y-", n),T("Y-", n)],

			( W(-j,n,i),
				W(i,j,-n) ) :
			[T("Y-", n)] +
			tCenter +
			[T("Y+", n)],

			# on R face
			( W(n,-i,j),
				W(i,j,-n) ) :
			[T("Z+", -n)] +
			tCenter_RotationZ +
			[T("Z-", -n)],

			( W(n,-j,-i),
				W(i,j,-n) ) :
			[T("Z+", -n)] +
			[T("X+", n)] +
			tCenter_RotationZ +
			[T("X-", n)] +
			[T("Z-", -n)],

			( W(n,i,-j),
				W(i,j,-n) ) :
			[T("Z+", -n)] +
			[T("X+", n),T("X+", n)] +
			tCenter_RotationZ +
			[T("X-", n),T("X-", n)] +
			[T("Z-", -n)],

			( W(n,j,i),
				W(i,j,-n) ) :
			[T("Z+", -n)] +
			[T("X-", n)] +
			tCenter_RotationZ +
			[T("X+", n)] +
			[T("Z-", -n)],

			# on L face
			( W(-n,i,j),
				W(i,j,-n) ) :
			[T("Z-", -n)] +
			tCenter_RotationNZ +
			[T("Z+", -n)],

			( W(-n,-j,i),
				W(i,j,-n) ) :
			[T("Z-", -n)] +
			[T("X+", -n)] +
			tCenter_RotationNZ +
			[T("X-", -n)] +
			[T("Z+", -n)],

			( W(-n,-i,-j),
				W(i,j,-n) ) :
			[T("Z-", -n)] +
			[T("X+", -n),T("X+", -n)] +
			tCenter_RotationNZ +
			[T("X-", -n),T("X-", -n)] +
			[T("Z+", -n)],

			( W(-n,j,-i),
				W(i,j,-n) ) :
			[T("Z-", -n)] +
			[T("X-", -n)] +
			tCenter_RotationNZ +
			[T("X+", -n)] +
			[T("Z+", -n)],

			# on D face
			( W(-i,-n,j),
				W(i,j,-n) ) :
			[T("Z+", -n),T("Z+", -n)] +
			tCenter_Rotation2Z +
			[T("Z-", -n),T("Z-", -n)],
			
			( W(j,-n,i),
				W(i,j,-n) ) :
			[T("Z+", -n),T("Z+", -n)] +
			[T("Y+", -n)] +
			tCenter_Rotation2Z +
			[T("Y-", -n)] +
			[T("Z-", -n),T("Z-", -n)],

			( W(i,-n,-j),
				W(i,j,-n) ) :
			[T("Z+", -n),T("Z+", -n)] +
			[T("Y+", -n),T("Y+", -n)] +
			tCenter_Rotation2Z +
			[T("Y-", -n),T("Y-", -n)] +
			[T("Z-", -n),T("Z-", -n)],

			( W(-j,-n,-i),
				W(i,j,-n) ) :
			[T("Z+", -n),T("Z+", -n)] +
			[T("Y-", -n)] +
			tCenter_Rotation2Z +
			[T("Y+", -n)] +
			[T("Z-", -n),T("Z-", -n)],

			# on B face
			( W(i,-j,n),
				W(i,j,-n) ) :
			tCenter_RotationNX,

			( W(j,i,n),
				W(i,j,-n) ) :
			[T("Z+", n)] +
			tCenter_RotationNX +
			[T("Z-", n)],

			( W(-i,j,n),
				W(i,j,-n) ) :
			[T("Z+", n),T("Z+", n)] +
			tCenter_RotationNX +
			[T("Z-", n),T("Z-", n)],

			( W(-j,-i,n),
				W(i,j,-n) ) :
			[T("Z-", n)] +
			tCenter_RotationNX +
			[T("Z+", n)],

			# on F face
			( W(i,j,-n),
				W(i,j,-n) ) :
			[],

			( W(-j,i,-n),
				W(i,j,-n) ) :
			[T("Z+", -n)] +
			tCenter +
			[T("Z-", -n)],

			( W(-i,-j,-n),
				W(i,j,-n) ) :
			[T("Z+", -n),T("Z+", -n)] +
			tCenter +
			[T("Z-", -n),T("Z-", -n)],

			( W(j,-i,-n),
				W(i,j,-n) ) :
			[T("Z-", -n)] +
			tCenter +
			[T("Z+", -n)],
		}

	def conjugate_check_solutions_W(self, Ws_check, solutionsWs_map, smt_list):
		for smt in smt_list:
			Ws_check = [smt.conjugate([W_check])[0] for W_check in Ws_check]
			solutionsWs_map = [conjugate_solutions_W(solutionsW_map, smt) for solutionsW_map in solutionsWs_map]
		return Ws_check, solutionsWs_map

	def solveWs_smt(self, problem, Ws_check, solutionsWs_map, smt_list):
		solutions_list = []
		for W_check, solutionsW_map in zip(Ws_check, solutionsWs_map):
			solutions_list += self.solveW(problem, W_check, solutionsW_map)
		for smt in smt_list:
			Ws_check, solutionsWs_map = self.conjugate_check_solutions_W(Ws_check, solutionsWs_map, [smt])
			for W_check, solutionsW_map in zip(Ws_check, solutionsWs_map):
				solutions_list += self.solveW(problem, W_check, solutionsW_map)
		return solutions_list

	def solve(self, problem):
		n = problem.n
		solutions = []

		Ws_check = []
		solutionsWs_map = []
		lower = -n+1
		upper = n-1
		for i in range(lower, upper+1):
			for j in range(lower, upper+1):
				Ws_check += [W(i,j,-n)]
				solutionsWs_map += [self.get_solutions_W(n, i, j)]

		smt_init_list = [
			SMT_RX, # F,U -> D,F
			SMT_RY, # D,F -> D,R
		]
		Ws_check, solutionsWs_map = self.conjugate_check_solutions_W(Ws_check, solutionsWs_map, smt_init_list)

		smt_list = [
			SMT_RNZ, # D,R -> R,U
			SMT_RY, # R,U -> B,U
			SMT_RY, # B,U -> L,U
			SMT_RY, # L,U -> F,U
		]
		solutions += self.solveWs_smt(problem, Ws_check, solutionsWs_map, smt_list)

		return solutions
