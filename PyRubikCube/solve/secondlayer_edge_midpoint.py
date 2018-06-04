from ..base.symbol import *

from .solution import *

def secondlayer_edge_midpoint_push(n):
	return [
		T("Y-", n),
		T("X-", n),
		T("Y+", n),
		T("X+", n),
		T("Y+", n),
		T("Z-", -n),
		T("Y-", n),
		T("Z+", -n),
	]

# secondlayer_edge_midpoint_W, reverse
def secondlayer_edge_midpoint_pop(n):
	return inverse_transforms(secondlayer_edge_midpoint_push(n))

class SecondLayerEdgeMidpointSolution(Solution):
	def get_solutions_W(self, n):
		t_pop = secondlayer_edge_midpoint_pop(n)
		t_pop_RotationY = smt_conjugate_transforms(SMT_RY, t_pop)
		t_pop_RotationNY = smt_conjugate_transforms(SMT_RNY, t_pop)
		t_pop_Rotation2Y = smt_conjugate_transforms(SMT_R2Y, t_pop)

		return {
			( W(n,0,n),
				W(n,0,-n) ) :
			t_pop_RotationY,

			( W(-n,0,-n),
				W(n,0,-n) ) :
			t_pop_RotationNY,

			( W(-n,0,n),
				W(n,0,-n) ) :
			t_pop_Rotation2Y,
		}

	def get_solutions_WV(self, n):
		t_push = secondlayer_edge_midpoint_push(n)
		t_push_ObliqueNY = smt_conjugate_transforms(SMT_ONY, t_push)
		
		return {
			( (W(0,n,-n), V('-Y','X','Z')),
				(W(n,0,-n), V_XYZ) ) :
			t_push,
			
			( (W(-n,n,0), V('Z','X','Y')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y+", n)] +
			t_push +
			[T("Y-", n)],

			( (W(n,n,0), V('-Z','X','-Y')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y-", n)] +
			t_push +
			[T("Y+", n)],

			( (W(0,n,n), V('Y','X','-Z')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y+", n),T("Y+", n)] +
			t_push +
			[T("Y-", n),T("Y-", n)],

			( (W(n,n,0), V('X','-Z','Y')),
				(W(n,0,-n), V_XYZ) ) :
			t_push_ObliqueNY,

			( (W(0,n,-n), V('Y','-Z','-X')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y+", n)] +
			t_push_ObliqueNY +
			[T("Y-", n)],

			( (W(0,n,n), V('-Y','-Z','X')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y-", n)] +
			t_push_ObliqueNY +
			[T("Y+", n)],

			( (W(-n,n,0), V('-X','-Z','-Y')),
				(W(n,0,-n), V_XYZ) ) :
			[T("Y+", n),T("Y+", n)] +
			t_push_ObliqueNY +
			[T("Y-", n),T("Y-", n)],

			( (W(n,0,-n), V('-Z','-Y','-X')),
				(W(n,0,-n), V_XYZ) ) :
			t_push,
		}

	def solve(self):
		n = self.problem.n

		solutionsW_map = self.get_solutions_W(n)
		solutionsWV_map = self.get_solutions_WV(n)
		smt_list = [
			SMT_RY,
			SMT_RY,
			SMT_RY,
		]
		W_check = W(n,0,-n)
		V_check = V_XYZ
		self.solve_smt(W_check, V_check, solutionsW_map, solutionsWV_map, smt_list)

		return self.solutions_list
