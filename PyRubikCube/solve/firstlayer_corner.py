from ..base.symbol import *

from .solution import *

def firstlayer_corner_DRB_W(n):
	return [
		T("X+", n),
		T("Y+", n),
		T("X-", n),
		T("Y-", n),
	]

# firstlayer_corner_DRB_W, Mirror Z, Reverse
def firstlayer_corner_FUR_WV(n):
	return [
		T("Y-", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
	]

def firstlayer_corner_URF_shift(n):
	return [
		T("X-", n),
		T("Y+", n),
		T("X+", n),
		T("Y-", n),
	]

# firstlayer_corner_DRB_W, Mirror Z
def firstlayer_corner_RDF_shift(n):
	return [
		T("X-", n),
		T("Y-", n),
		T("X+", n),
		T("Y+", n),
	]

class FirstLayerCornerSolution(Solution):
	def get_solutions_W(self, n):
		tDRB = firstlayer_corner_DRB_W(n)
		tDRB_RotationY = smt_conjugate_transforms(SMT_RY, tDRB)
		tDRB_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, tDRB)

		return {
			( W(n,-n,n),
				W(n,-n,-n) ) :
			tDRB,

			( W(-n,-n,n),
				W(n,-n,-n) ) :
			tDRB_RotationY,

			( W(-n,-n,-n),
				W(n,-n,-n) ) :
			tDRB_Rotation2Y,
		}

	def get_solutions_WV(self, n):
		tFUR = firstlayer_corner_FUR_WV(n)
		tFUR_ObliqueNY = smt_conjugate_transforms(SMT_ONY, tFUR)
		
		tURF_shift = firstlayer_corner_URF_shift(n)

		tRDF_shift = firstlayer_corner_RDF_shift(n)
		tRDF_shift_ObliqueNY = smt_conjugate_transforms(SMT_ONY, tRDF_shift)

		return {
			( (W(n,n,-n), V('X','-Z','Y')),
				(W(n,-n,-n), V_XYZ) ) :
			tFUR,
			
			( (W(n,n,-n), V('-Y','X','Z')),
				(W(n,-n,-n), V_XYZ) ) :
			tFUR_ObliqueNY,

			( (W(n,n,-n), V('-Z','-Y','-X')),
				(W(n,-n,-n), V_XYZ) ) :
			tURF_shift,

			( (W(-n,n,-n), V('Y','-Z','-X')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n)] +
			tFUR +
			[T("Y-", n)],
			
			( (W(-n,n,-n), V('Z','X','Y')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n)] +
			tFUR_ObliqueNY +
			[T("Y-", n)],

			( (W(-n,n,-n), V('-X','-Y','Z')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n)] +
			tURF_shift +
			[T("Y-", n)],

			( (W(-n,n,n), V('-X','-Z','-Y')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n), T("Y+", n)] +
			tFUR +
			[T("Y-", n), T("Y-", n)],
			
			( (W(-n,n,n), V('Y','X','-Z')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n), T("Y+", n)] +
			tFUR_ObliqueNY +
			[T("Y-", n), T("Y-", n)],

			( (W(-n,n,n), V('Z','-Y','X')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y+", n), T("Y+", n)] +
			tURF_shift +
			[T("Y-", n), T("Y-", n)],

			( (W(n,n,n), V('-Y','-Z','X')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y-", n)] +
			tFUR +
			[T("Y+", n)],
			
			( (W(n,n,n), V('-Z','X','-Y')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y-", n)] +
			tFUR_ObliqueNY +
			[T("Y+", n)],

			( (W(n,n,n), V('X','-Y','-Z')),
				(W(n,-n,-n), V_XYZ) ) :
			[T("Y-", n)] +
			tURF_shift +
			[T("Y+", n)],


			( (W(n,-n,-n), V('-Z','-X','Y')),
				(W(n,-n,-n), V_XYZ) ) :
			tRDF_shift_ObliqueNY,

			( (W(n,-n,-n), V('-Y','Z','-X')),
				(W(n,-n,-n), V_XYZ) ) :
			tRDF_shift,
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
		W_check = W(n,-n,-n)
		V_check = V_XYZ
		solutions += self.solve_smt(problem, W_check, V_check, solutionsW_map, solutionsWV_map, smt_list)

		return solutions
