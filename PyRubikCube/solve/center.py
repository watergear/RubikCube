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
		Ws_check, solutionsWs_map = conjugate_check_solutions_W(Ws_check, solutionsWs_map, smt_init_list)

		smt_list = [
			SMT_RNZ, # D,R -> R,U
			SMT_RY, # R,U -> B,U
			SMT_RY, # B,U -> L,U
			SMT_RY, # L,U -> F,U
		]
		solutions += self.solveWs_smt(problem, Ws_check, solutionsWs_map, smt_list)

		return solutions

# (i,n,i) -> (-i,n,i) -> (i,n,-i) -> (i,n,i)
def center_shift_i_i(n, i):
	return [
		T("Y-", n),

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

		T("Y+", n),

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

# (i,n,j) -> (j,n,-i) -> (-j,n,i) -> (i,n,j)
def center_shift_i_j(n, i, j):
	return [
		T("Y+", n),

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

		T("Y-", n),

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

class CenterShiftSolver(Solver):
	def get_solutions_W(self, n, i, j):
		if 0 == i and 0 == j:
			return {}

		if i == j:
			tCenterShiftB = center_shift_i_i(n, i)
			tCenterShiftA = inverse_transforms(tCenterShiftB)
		else:
			tCenterShiftA = center_shift_i_j(n, i, j)
			tCenterShiftB = inverse_transforms(tCenterShiftA)

		tCenterShiftA_RotationY = smt_conjugate_transforms(SMT_RY, tCenterShiftA)
		tCenterShiftA_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, tCenterShiftA)
		tCenterShiftA_RotationNY = smt_conjugate_transforms(SMT_RNY, tCenterShiftA)
		tCenterShiftB_RotationY = smt_conjugate_transforms(SMT_RY, tCenterShiftB)
		tCenterShiftB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, tCenterShiftB)
		tCenterShiftB_RotationNY = smt_conjugate_transforms(SMT_RNY, tCenterShiftB)

		return {
			# on U face
			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			[],

			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			tCenterShiftA_Rotation2Y,

			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			tCenterShiftB_Rotation2Y,

			(
			(W(i,n,j),		W(i,n,j)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			tCenterShiftA,

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			tCenterShiftA_RotationY,

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			[T("Y-", n)],

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(-j,n,i)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			tCenterShiftA,

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			tCenterShiftB_RotationY,

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(j,n,-i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(j,n,-i)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			tCenterShiftA_RotationNY,

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			# tCenterShiftB_RotationY,
			tCenterShiftA_RotationNY,			

			(
			(W(i,n,j),		W(-i,n,-j)),
			(W(-j,n,i),		W(j,n,-i)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(i,n,j)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			tCenterShiftB,

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(-i,n,-j)),
			) :
			tCenterShiftB_RotationNY,

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(-j,n,i)),
			(W(-i,n,-j),	W(-i,n,-j)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(i,n,j)),
			(W(j,n,-i),		W(-j,n,i)),
			) :
			[T("Y+", n)],

			(
			(W(i,n,j),		W(j,n,-i)),
			(W(-j,n,i),		W(-i,n,-j)),
			(W(-i,n,-j),	W(-j,n,i)),
			(W(j,n,-i),		W(i,n,j)),
			) :
			tCenterShiftB,
		}

	def checkW(self, problem, i, j):
		n = problem.n

		W_check_1 = W(i,n,j)
		W_now_1 = problem.state.locations_map[W_check_1]

		W_check_2 = W(-j,n,i)
		W_now_2 = problem.state.locations_map[W_check_2]

		W_check_3 = W(-i,n,-j)
		W_now_3 = problem.state.locations_map[W_check_3]

		W_check_4 = W(j,n,-i)
		W_now_4 = problem.state.locations_map[W_check_4]

		self.currentWs = tuple()
		self.currentWs += ((W_check_1, W_now_1),)
		self.currentWs += ((W_check_2, W_now_2),)
		self.currentWs += ((W_check_3, W_now_3),)
		self.currentWs += ((W_check_4, W_now_4),)

		check_pass = True
		for w in self.currentWs:
			check_pass = check_pass and (w[0]==w[1])
		return check_pass

	def solveW(self, problem, i, j):
		n = problem.n
		solutions_list = []
		solutionsW_map = self.get_solutions_W(n, i, j)
		while not self.checkW(problem, i, j):
			if not self.currentWs in solutionsW_map:
				break
			solutions = solutionsW_map[self.currentWs]
			print("W keys:", self.currentWs)
			print("W solutions:", solutions)
			for t in solutions:
				problem.state.transform(t)
			solutions_list += solutions
		return solutions_list

	def solve(self, problem):
		n = problem.n
		solutions = []

		for i in range(0, n):
			for j in range(1, n):
				solutions += self.solveW(problem, i, j)

		return solutions
