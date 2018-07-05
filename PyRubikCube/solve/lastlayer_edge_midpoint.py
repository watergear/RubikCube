from ..base.symbol import *

from .solution import *

def lastlayer_edge_midpoint_coverA(n):
	return [
		T("Z+", -n),
		T("X-", n),
		T("Y-", n),
		T("X+", n),
		T("Y+", n),
		T("Z-", -n),
	]

def lastlayer_edge_midpoint_coverB(n):
	return [
		T("Z+", -n),
		T("Y-", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
		T("Z-", -n),
	]

def lastlayer_edge_midpoint_shiftA(n):
	return [
		T("X-", n),
		T("Y+", n),
		T("Y+", n),
		T("X+", n),
		T("Y+", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
	]

def lastlayer_edge_midpoint_shiftB(n):
	return [
		T("X-", n),
		T("Y-", n),
		T("X+", n),
		T("Y-", n),
		T("X-", n),
		T("Y-", n),
		T("Y-", n),
		T("X+", n),
	]

def lastlayer_edge_midpoint_switch(n):
	return [
		T("X+", n),
		T("Z-", -n),
		T("Y-", n),
		T("Z+", -n),
		T("Y+", n),
		T("Z-", -n),
		T("Y+", n),
		T("Z+", -n),
		T("Z+", -n),
		T("X-", n),
		T("Z-", -n),
		T("Y+", n),
		T("Z-", -n),
		T("Y-", n),
		T("Z+", -n),
	]

class LastLayerEdgeMidpointSolution(Solution):
	def get_solutions_V(self, n):
		coverA = lastlayer_edge_midpoint_coverA(n)
		coverB = lastlayer_edge_midpoint_coverB(n)

		coverA_ObliqueNY = smt_conjugate_transforms(SMT_ONY, coverA)

		coverB_RotationY = smt_conjugate_transforms(SMT_RY, coverB)
		coverB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverB)
		coverB_RotationNY = smt_conjugate_transforms(SMT_RNY, coverB)

		return {
			(
			(W(0,n,-n),	False),
			(W(-n,n,0),	True),
			(W(0,n,n),	False),
			(W(n,n,0),	True),
			) :
			coverA,

			(
			(W(0,n,-n),	True),
			(W(-n,n,0),	False),
			(W(0,n,n),	True),
			(W(n,n,0),	False),
			) :
			coverA_ObliqueNY,

			(
			(W(0,n,-n),	False),
			(W(-n,n,0),	True),
			(W(0,n,n),	True),
			(W(n,n,0),	False),
			) :
			coverB,

			(
			(W(0,n,-n),	False),
			(W(-n,n,0),	False),
			(W(0,n,n),	True),
			(W(n,n,0),	True),
			) :
			coverB_RotationNY,

			(
			(W(0,n,-n),	True),
			(W(-n,n,0),	False),
			(W(0,n,n),	False),
			(W(n,n,0),	True),
			) :
			coverB_Rotation2Y,

			(
			(W(0,n,-n),	True),
			(W(-n,n,0),	True),
			(W(0,n,n),	False),
			(W(n,n,0),	False),
			) :
			coverB_RotationY,

			(
			(W(0,n,-n),	False),
			(W(-n,n,0),	False),
			(W(0,n,n),	False),
			(W(n,n,0),	False),
			) :
			coverA,
		}

	def get_solutions_W(self, n):
		shiftA = lastlayer_edge_midpoint_shiftA(n)
		shiftB = lastlayer_edge_midpoint_shiftB(n)

		switch = lastlayer_edge_midpoint_switch(n)

		shiftA_RotationY = smt_conjugate_transforms(SMT_RY, shiftA)
		shiftA_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, shiftA)
		shiftA_RotationNY = smt_conjugate_transforms(SMT_RNY, shiftA)
		shiftB_RotationY = smt_conjugate_transforms(SMT_RY, shiftB)
		shiftB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, shiftB)
		shiftB_RotationNY = smt_conjugate_transforms(SMT_RNY, shiftB)

		switch_ObliqueNY = smt_conjugate_transforms(SMT_ONY, switch)

		return {
			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(n,n,0)),
			) :
			[],

			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(0,n,n)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(n,n,0)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			shiftB,

			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(0,n,n)),
			) :
			shiftA,

			(
			(W(0,n,-n),	W(0,n,-n)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			switch_ObliqueNY,

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(n,n,0)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(0,n,n)),
			) :
			shiftB_RotationY,

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(n,n,0)),
			) :
			shiftB_RotationY,

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(0,n,n)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(-n,n,0)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			shiftB_Rotation2Y,

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(n,n,0)),
			) :
			shiftA_RotationY,

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(n,n,0)),
			) :
			switch,

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(n,n,0)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			shiftB_RotationNY,

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			shiftA_RotationY,

			(
			(W(0,n,-n),	W(0,n,n)),
			(W(-n,n,0),	W(n,n,0)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(0,n,n)),
			) :
			[T("Y-", n)],

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(0,n,-n)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			shiftA_Rotation2Y,

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(0,n,n)),
			) :
			shiftA_RotationNY,

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(-n,n,0)),
			(W(0,n,n),	W(0,n,n)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(0,n,-n)),
			(W(n,n,0),	W(-n,n,0)),
			) :
			[T("Y+", n)],

			(
			(W(0,n,-n),	W(n,n,0)),
			(W(-n,n,0),	W(0,n,n)),
			(W(0,n,n),	W(-n,n,0)),
			(W(n,n,0),	W(0,n,-n)),
			) :
			shiftA_RotationNY,
		}

	def checkV(self):
		n = self.problem.n

		tableVs = {}

		W_check_UF = W(0,n,-n)
		W_now_UF = self.problem.state.locations_map[W_check_UF]
		V_now_UF = self.problem.state.orientations_map[W_check_UF]
		tableVs[W_now_UF] = (factorY == V_now_UF[1])

		W_check_UL = W(-n,n,0)
		W_now_UL = self.problem.state.locations_map[W_check_UL]
		V_now_UL = self.problem.state.orientations_map[W_check_UL]
		tableVs[W_now_UL] = (factorY == V_now_UL[1])

		W_check_UB = W(0,n,n)
		W_now_UB = self.problem.state.locations_map[W_check_UB]
		V_now_UB = self.problem.state.orientations_map[W_check_UB]
		tableVs[W_now_UB] = (factorY == V_now_UB[1])

		W_check_UR = W(n,n,0)
		W_now_UR = self.problem.state.locations_map[W_check_UR]
		V_now_UR = self.problem.state.orientations_map[W_check_UR]
		tableVs[W_now_UR] = (factorY == V_now_UR[1])

		self.currentVs = tuple()
		self.currentVs += ((W_check_UF, tableVs[W_check_UF]),)
		self.currentVs += ((W_check_UL, tableVs[W_check_UL]),)
		self.currentVs += ((W_check_UB, tableVs[W_check_UB]),)
		self.currentVs += ((W_check_UR, tableVs[W_check_UR]),)

		check_pass = True
		for k in tableVs:
			check_pass = check_pass and tableVs[k]
		return check_pass

	def checkW(self):
		n = self.problem.n

		W_check_UF = W(0,n,-n)
		W_now_UF = self.problem.state.locations_map[W_check_UF]

		W_check_UL = W(-n,n,0)
		W_now_UL = self.problem.state.locations_map[W_check_UL]

		W_check_UB = W(0,n,n)
		W_now_UB = self.problem.state.locations_map[W_check_UB]

		W_check_UR = W(n,n,0)
		W_now_UR = self.problem.state.locations_map[W_check_UR]

		self.currentWs = tuple()
		self.currentWs += ((W_check_UF, W_now_UF),)
		self.currentWs += ((W_check_UL, W_now_UL),)
		self.currentWs += ((W_check_UB, W_now_UB),)
		self.currentWs += ((W_check_UR, W_now_UR),)

		check_pass = True
		for w in self.currentWs:
			check_pass = check_pass and (w[0]==w[1])
		return check_pass

	def solveV(self):
		n = self.problem.n
		solutionsV_map = self.get_solutions_V(n)
		while not self.checkV():
			if not self.currentVs in solutionsV_map:
				break
			solutions = solutionsV_map[self.currentVs]
			print("V keys:", self.currentVs)
			print("V solutions:", solutions)
			for t in solutions:
				self.problem.state.transform(t)
			self.solutions_list += solutions

	def solveW(self):
		n = self.problem.n
		solutionsW_map = self.get_solutions_W(n)
		while not self.checkW():
			if not self.currentWs in solutionsW_map:
				break
			solutions = solutionsW_map[self.currentWs]
			print("W keys:", self.currentWs)
			print("W solutions:", solutions)
			for t in solutions:
				self.problem.state.transform(t)
			self.solutions_list += solutions

	def solve(self):
		self.solveV()
		self.solveW()

		return self.solutions_list
