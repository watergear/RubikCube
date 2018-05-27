from ..base.transform import *

# v1 * mm = v2
# return mm
def get_transform_mat_by_vv(v1, v2):
	# vv * mat(vv) = E
	# vv = E * mat_inverse(vv)

	# v1 = E * mat_inverse(v1)
	# v2 = E * mat_inverse(v2)

	# v1 * mm = v2
	# E * mat_inverse(v1) * mm = E * mat_inverse(v2)
	# mat_inverse(v1) * mm = mat_inverse(v2)
	# mm = mat(v1) * mat_inverse(v2)

	mm = mat_mul(v1, mat_inverse(v2))
	return mm

def conjugate_solutions_W(solutions_map, smt):
	solutions_smt_map = {}

	for key in solutions_map.keys():
		(W_now, W_check) = key
		transforms = solutions_map[key]

		W_now_smt = smt.conjugate([W_now])[0]
		W_check_smt = smt.conjugate([W_check])[0]

		transforms_smt = [smt.conjugate_transform(t) for t in transforms]

		key_smt = (W_now_smt, W_check_smt)
		solutions_smt_map[key_smt] = transforms_smt

	return solutions_smt_map

def conjugate_solutions_WV(solutions_map, smt):
	solutions_smt_map = {}

	for key in solutions_map.keys():
		(W_now, V_now) = key[0]
		(W_check, V_check) = key[1]
		transforms = solutions_map[key]

		W_now_smt = smt.conjugate([W_now])[0]
		W_check_smt = smt.conjugate([W_check])[0]

		mat = get_transform_mat_by_vv(V_check, V_now)
		mat_smt = smt.conjugate_matrix(mat)
		V_now_smt = mat_mul([V_check], mat_smt)[0]
		V_check_smt = V_check

		transforms_smt = [smt.conjugate_transform(t) for t in transforms]

		key_smt = ((W_now_smt, V_now_smt), (W_check_smt, V_check_smt))
		solutions_smt_map[key_smt] = transforms_smt

	return solutions_smt_map

class Solution:
	def __init__(self, problem):
		self.problem = problem
		self.solutions_list = []

	def solveW(self, W_check, solutionsW_map):
		check_pass = False
		while not check_pass:
			W_now = self.problem.state.positions_map[W_check]
			if ( W_check == W_now ):
				check_pass = True
			else:
				solutions = solutionsW_map[(W_now, W_check)]
				for t in solutions:
					self.problem.state.transform(t)
				self.solutions_list += solutions

	def solveWV(self, W_check, V_check, solutionsWV_map):
		check_pass = False
		while not check_pass:
			W_now = self.problem.state.positions_map[W_check]
			V_now = self.problem.state.orientations_map[W_check]
			if ( W_check == W_now and V_check == V_now ):
				check_pass = True
			else:
				solutions = solutionsWV_map[((W_now,V_now),(W_check,V_check))]
				for t in solutions:
					self.problem.state.transform(t)
				self.solutions_list += solutions

	def solveW_smt(self, W_check, solutionsW_map, smt_list):
		self.solveW(W_check, solutionsW_map)
		for smt in smt_list:
			solutionsW_map = conjugate_solutions_W(solutionsW_map, smt)
			W_check = smt.conjugate([W_check])[0]
			self.solveW(W_check, solutionsW_map)

	def solveWV_smt(self, W_check, V_check, solutionsWV_map, smt_list):
		self.solveWV(W_check, V_check, solutionsWV_map)
		for smt in smt_list:
			solutionsWV_map = conjugate_solutions_WV(solutionsWV_map, smt)
			W_check = smt.conjugate([W_check])[0]
			self.solveWV(W_check, V_check, solutionsWV_map)
