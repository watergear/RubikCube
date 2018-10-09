from ..base.symbol import *

from .solution import *

def firstlayer_edge_midpoint_FU_W(n):
	return [
		T("X-", n),
		T("Y+", n),
		T("X+", n),
		T("Y-", n),
	]

def firstlayer_edge_midpoint_RF_WV(n):
	return [
		T("X+", n),
		T("Z-", -n),
		T("X-", n),
		T("Z+", -n),
	]

class FirstLayerEdgeMidpointSolution(Solution):
	def get_solutions_W(self, n):
		tFU = firstlayer_edge_midpoint_FU_W(n)
		tFU_RotationY = smt_conjugate_transforms(SMT_RY, tFU)
		tFU_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, tFU)
		tFU_RotationNY = smt_conjugate_transforms(SMT_RNY, tFU)

		return {
			( W(n,n,0),
				W(0,-n,-n) ) :
			tFU_RotationY,

			( W(-n,n,0),
				W(0,-n,-n) ) :
			tFU_RotationNY,

			( W(0,n,n),
				W(0,-n,-n) ) :
			tFU_Rotation2Y,

			( W(0,n,-n),
				W(0,-n,-n) ) :
			tFU,

			( W(n,-n,0),
				W(0,-n,-n) ) :
			[
			T("Z+", -n),
			T("Y-", -n),
			T("Z-", -n),
			T("Y+", -n),
			],

			( W(-n,-n,0),
				W(0,-n,-n) ) :
			[
			T("Z+", -n),
			T("Y+", -n),
			T("Z-", -n),
			T("Y-", -n),
			],

			( W(0,-n,n),
				W(0,-n,-n) ) :
			[
			T("Z+", n),
			T("Z+", n),
			T("X-", n),
			T("Y-", n),
			T("X+", n),
			T("Y+", n),
			T("Z-", n),
			T("Z-", n),
			],
		}

	def get_solutions_WV(self, n):
		t = firstlayer_edge_midpoint_RF_WV(n)
		t_ObliqueNY = smt_conjugate_transforms(SMT(r"\\","Y"), t)

		t_MirrorX = smt_conjugate_transforms(SMT("||","X"), t)
		t_ObliqueNY_MirrorX = smt_conjugate_transforms(SMT("||","X"), t_ObliqueNY)

		t_MirrorZ = smt_conjugate_transforms(SMT("||","Z"), t)
		t_ObliqueNY_MirrorZ = smt_conjugate_transforms(SMT("||","Z"), t_ObliqueNY)

		t_Rotation2Y = smt_conjugate_transforms(SMT("[]2","Y"), t)
		t_ObliqueNY_Rotation2Y = smt_conjugate_transforms(SMT("[]2","Y"), t_ObliqueNY)

		return {
			( (W(n,0,-n), V('-Y','X','Z')),
				(W(0,-n,-n), V_XYZ) ) :
			t,
			
			( (W(-n,0,-n), V('Y','-X','Z')),
				(W(0,-n,-n), V_XYZ) ) :
			t_MirrorX,
			
			( (W(n,0,n), V('-Y','-X','-Z')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y+", -n),T("Y+", -n)] +
			t_MirrorZ +
			[T("Y+", -n),T("Y+", -n)],
			
			( (W(-n,0,n), V('Y','X','-Z')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y+", -n),T("Y+", -n)] +
			t_Rotation2Y +
			[T("Y+", -n),T("Y+", -n)],
			
			( (W(n,0,-n), V('-Z','-X','Y')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y+", -n)] +
			t_ObliqueNY +
			[T("Y-", -n)],

			( (W(-n,0,-n), V('Z','X','Y')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y-", -n)] +
			t_ObliqueNY_MirrorX +
			[T("Y+", -n)],

			( (W(n,0,n), V('-Z','X','-Y')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y+", -n)] +
			t_ObliqueNY_MirrorZ +
			[T("Y-", -n)],

			( (W(-n,0,n), V('Z','-X','-Y')),
				(W(0,-n,-n), V_XYZ) ) :
			[T("Y-", -n)] +
			t_ObliqueNY_Rotation2Y +
			[T("Y+", -n)],

			( (W(0,-n,-n), V('-X','Z','Y')),
				(W(0,-n,-n), V_XYZ) ) :
			[
			T("Z-", -n),
			T("Z-", -n),
			T("Y-", n),
			T("Z+", -n),
			T("X-", n),
			T("Y+", n),
			T("Y+", n),
			T("X+", n),
			T("Z+", -n),
			T("Y-", n),
			],
		}

	def solve(self, problem):
		n = problem.n
		solutions = []

		solutionsW_map = self.get_solutions_W(n)
		solutionsWV_map = self.get_solutions_WV(n)
		smt_list = [
			SMT_RY,
			SMT_RY,
			SMT_RY,
		]
		W_check = W(0,-n,-n)
		V_check = V_XYZ
		solutions += self.solve_smt(problem, W_check, V_check, solutionsW_map, solutionsWV_map, smt_list)

		return solutions
