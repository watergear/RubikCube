from ..base.symbol import *

from .solution import *

def lastlayer_corner_coverA(n):
	return [
		T("X-", n),
		T("X-", -n),
		T("Y-", n),
		T("X+", n),
		T("Y+", n),
		T("X+", -n),
		T("Y-", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
	]

def lastlayer_corner_coverB(n):
	return [
		T("X-", n),
		T("X-", -n),
		T("Y-", n),
		T("X+", n),
		T("Y+", n),
		T("Y+", n),
		T("X+", -n),
		T("Y+", n),
		T("Y+", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
		T("Y+", n),
		T("Y+", n),
		T("X-", -n),
		T("Y+", n),
		T("Y+", n),
		T("X+", -n),
	]

def lastlayer_corner_shift(n):
	return [
		T("X-", -n),
		T("X+", n),
		T("Y+", n),
		T("Y+", n),
		T("X+", n),
		T("Y-", -n),
		T("X-", n),
		T("Y+", n),
		T("Y+", n),
		T("X+", n),
		T("Y+", -n),
		T("X-", n),
		T("X-", n),
		T("X+", -n),
	]

# corner_edge_transpose
def lastlayer_corner_switch(n):
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

class LastLayerCornerSolution(Solution):
	def get_solutions_step1_WV(self, n):
		coverA = lastlayer_corner_coverA(n)
		coverB = lastlayer_corner_coverB(n)
		shift = lastlayer_corner_shift(n)

		coverA_ObliqueNY = smt_conjugate_transforms(SMT_ONY, coverA)

		coverA_MirrorX = smt_conjugate_transforms(SMT_MX, coverA)
		coverB_MirrorX = smt_conjugate_transforms(SMT_MX, coverB)

		coverA_RotationY = smt_conjugate_transforms(SMT_RY, coverA)
		coverA_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverA)
		coverA_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA)
		coverB_RotationY = smt_conjugate_transforms(SMT_RY, coverB)
		coverB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverB)
		coverB_RotationNY = smt_conjugate_transforms(SMT_RNY, coverB)

		shift_RotationY = smt_conjugate_transforms(SMT_RY, shift)
		shift_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, shift)
		shift_RotationNY = smt_conjugate_transforms(SMT_RNY, shift)

		coverA_ObliqueNY_RotationY = smt_conjugate_transforms(SMT_RY, coverA_ObliqueNY)
		coverA_MirrorX_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA_MirrorX)

		return {
			( (W(n,n,n), V('-Z','Y','X')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_RotationNY,
			
			( (W(n,n,n), V('Y','X','-Z')),
				(W(n,n,-n), V_XYZ) ) :
			coverB_MirrorX,

			( (W(n,n,n), V('X','-Z','Y')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_Rotation2Y,

			( (W(-n,n,n), V('-X','Y','-Z')),
				(W(n,n,-n), V_XYZ) ) :
			shift_RotationNY,

			( (W(-n,n,n), V('Z','X','Y')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_RotationY,
			
			( (W(-n,n,n), V('-Y','-Z','X')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_MirrorX,
			
			( (W(-n,n,-n), V('Z','Y','-X')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_ObliqueNY_RotationY,

			( (W(-n,n,-n), V('-Y','X','Z')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_MirrorX_RotationNY,

			( (W(-n,n,-n), V('-X','-Z','-Y')),
				(W(n,n,-n), V_XYZ) ) :
			coverB_RotationY,

			( (W(n,n,-n), V('-Z','X','-Y')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_MirrorX,

			( (W(n,n,-n), V('Y','-Z','-X')),
				(W(n,n,-n), V_XYZ) ) :
			coverA_RotationY,
		}
	
	def solve_step1(self, problem):
		n = problem.n

		solutionsWV_map = self.get_solutions_step1_WV(n)
		W_check = W(n,n,-n)
		V_check = V_XYZ
		solutions = self.solveWV(problem, W_check, V_check, solutionsWV_map)
		return solutions

	def get_solutions_step2_WV(self, n):
		coverA = lastlayer_corner_coverA(n)
		coverB = lastlayer_corner_coverB(n)
		shift = lastlayer_corner_shift(n)

		coverA_ObliqueNY = smt_conjugate_transforms(SMT_ONY, coverA)
		shift_ObliqueY = smt_conjugate_transforms(SMT_OY, shift)

		# coverA_MirrorX = smt_conjugate_transforms(SMT_MX, coverA)
		# coverB_MirrorX = smt_conjugate_transforms(SMT_MX, coverB)
		coverB_MirrorZ = smt_conjugate_transforms(SMT_MZ, coverB)

		# coverA_RotationY = smt_conjugate_transforms(SMT_RY, coverA)
		# coverA_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverA)
		# coverA_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA)
		# coverB_RotationY = smt_conjugate_transforms(SMT_RY, coverB)
		# coverB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverB)
		coverB_RotationNY = smt_conjugate_transforms(SMT_RNY, coverB)

		# shift_RotationY = smt_conjugate_transforms(SMT_RY, shift)
		shift_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, shift)
		# shift_RotationNY = smt_conjugate_transforms(SMT_RNY, shift)

		# coverA_ObliqueNY_RotationY = smt_conjugate_transforms(SMT_RY, coverA_ObliqueNY)
		# coverA_MirrorX_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA_MirrorX)

		return {
			( (W(n,n,n), V('X','Y','Z')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			shift_ObliqueY,
			
			( (W(n,n,n), V('Y','Z','X')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverA_ObliqueNY,

			( (W(n,n,n), V('Z','X','Y')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverB_RotationNY,

			( (W(-n,n,n), V('-Z','Y','X')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			[],

			( (W(-n,n,n), V('-X','Z','Y')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverA,
			
			( (W(-n,n,n), V('-Y','X','Z')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverA,
			
			( (W(-n,n,-n), V('-X','Y','-Z')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			shift_Rotation2Y,

			( (W(-n,n,-n), V('-Y','Z','-X')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverB_MirrorZ,

			( (W(-n,n,-n), V('-Z','X','-Y')),
				(W(-n,n,n), V('-Z','Y','X')) ) :
			coverA,
		}

	def solve_step2(self, problem):
		n = problem.n

		solutionsWV_map = self.get_solutions_step2_WV(n)
		W_check = W(n,n,n)
		W_goal = W(-n,n,n)
		V_goal = V('-Z','Y','X')
		solutions = self.solveWWV(problem, W_check, W_goal, V_goal, solutionsWV_map)
		return solutions

	def get_solutions_step3_WV(self, n):
		coverA = lastlayer_corner_coverA(n)
		coverB = lastlayer_corner_coverB(n)
		shift = lastlayer_corner_shift(n)

		coverA_ObliqueNY = smt_conjugate_transforms(SMT_ONY, coverA)
		# shift_ObliqueY = smt_conjugate_transforms(SMT_OY, shift)

		# coverA_MirrorX = smt_conjugate_transforms(SMT_MX, coverA)
		# coverB_MirrorX = smt_conjugate_transforms(SMT_MX, coverB)
		# coverB_MirrorZ = smt_conjugate_transforms(SMT_MZ, coverB)

		# coverA_RotationY = smt_conjugate_transforms(SMT_RY, coverA)
		# coverA_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverA)
		# coverA_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA)
		# coverB_RotationY = smt_conjugate_transforms(SMT_RY, coverB)
		# coverB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, coverB)
		coverB_RotationNY = smt_conjugate_transforms(SMT_RNY, coverB)

		# shift_RotationY = smt_conjugate_transforms(SMT_RY, shift)
		shift_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, shift)
		# shift_RotationNY = smt_conjugate_transforms(SMT_RNY, shift)

		# coverA_ObliqueNY_RotationY = smt_conjugate_transforms(SMT_RY, coverA_ObliqueNY)
		# coverA_MirrorX_RotationNY = smt_conjugate_transforms(SMT_RNY, coverA_MirrorX)

		return {
			( (W(n,n,n), V('-X','Y','-Z')),
				(W(-n,n,-n), V_XYZ) ) :
			shift_Rotation2Y,
			
			( (W(n,n,n), V('Y','-Z','-X')),
				(W(-n,n,-n), V_XYZ) ) :
			coverA,

			( (W(n,n,n), V('-Z','-X','Y')),
				(W(-n,n,-n), V_XYZ) ) :
			coverA_ObliqueNY + coverB_RotationNY,

			# for even-n
			( (W(-n,n,-n), V('X','Y','Z')),
				(W(-n,n,-n), V_XYZ) ) :
			[],

			# for even-n
			( (W(-n,n,-n), V('Z','-X','-Y')),
				(W(-n,n,-n), V_XYZ) ) :
			# coverA + shift_ObliqueY,
			coverA_ObliqueNY + shift_Rotation2Y,

			# for even-n
			( (W(-n,n,-n), V('-Y','-Z','X')),
				(W(-n,n,-n), V_XYZ) ) :
			coverB_RotationNY + coverA,
		}

	def solve_step3(self, problem):
		n = problem.n

		solutionsWV_map = self.get_solutions_step3_WV(n)
		W_check = W(-n,n,-n)
		V_check = V_XYZ
		solutions = self.solveWV(problem, W_check, V_check, solutionsWV_map)
		return solutions

	def get_solutions_step4_WV(self, n):
		switch = lastlayer_corner_switch(n)

		switch_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, switch)

		return {
			( (W(-n,n,n), V('-Z','Y','X')),
				(W(n,n,n), V_XYZ) ) :
			switch_Rotation2Y,
		}

	def solve_step4(self, problem):
		n = problem.n

		solutionsWV_map = self.get_solutions_step4_WV(n)
		W_check = W(n,n,n)
		V_check = V_XYZ
		solutions = self.solveWV(problem, W_check, V_check, solutionsWV_map)
		return solutions

	def solve(self, problem):
		solutions = []

		solutions += self.solve_step1(problem)
		solutions += self.solve_step2(problem)
		solutions += self.solve_step3(problem)
		solutions += self.solve_step4(problem) # for n = 1, even

		return solutions
