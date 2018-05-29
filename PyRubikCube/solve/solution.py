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

def smt_conjugate_transforms(smt, transforms):
	return [smt.conjugate_transform(t) for t in transforms]

def smts_conjugate_transforms(smts, transforms):
	for smt in smt_list:
		transforms = smt_conjugate_transforms(smt, transforms)
	return transforms

def smt_conjugate_W(smt, W_from, W_to):
	W_from_smt = smt.conjugate([W_from])[0]
	W_to_smt = smt.conjugate([W_to])[0]
	return (W_from_smt, W_to_smt)

def smt_conjugate_WV(smt, W_from, V_from, W_to, V_to, fixed_V_to):
	W_from_smt,	W_to_smt = smt_conjugate_W(smt, W_from, W_to)
	if not fixed_V_to:
		V_from_smt = smt.conjugate([V_from])[0]
		V_to_smt = smt.conjugate([V_to])[0]
	else:
		mat = get_transform_mat_by_vv(V_to, V_from)
		mat_smt = smt.conjugate_matrix(mat)
		V_from_smt = mat_mul([V_to], mat_smt)[0]
		V_to_smt = V_to

	return W_from_smt, V_from_smt, W_to_smt, V_to_smt

def conjugate_solutions_W(solutions_map, smt):
	solutions_smt_map = {}

	for key in solutions_map.keys():
		(W_from, W_to) = key
		transforms = solutions_map[key]

		W_from_smt, W_to_smt = smt_conjugate_W(smt, W_from, W_to)

		transforms_smt = smt_conjugate_transforms(smt, transforms)

		key_smt = (W_from_smt, W_to_smt)
		solutions_smt_map[key_smt] = transforms_smt

	return solutions_smt_map

def conjugate_solutions_WV(solutions_map, smt):
	solutions_smt_map = {}

	for key in solutions_map.keys():
		(W_from, V_from) = key[0]
		(W_to, V_to) = key[1]
		transforms = solutions_map[key]

		W_from_smt, V_from_smt, W_to_smt, V_to_smt = \
			smt_conjugate_WV(smt, W_from, V_from, W_to, V_to,
				fixed_V_to = True
			 )

		transforms_smt = smt_conjugate_transforms(smt, transforms)

		key_smt = ((W_from_smt, V_from_smt), (W_to_smt, V_to_smt))
		solutions_smt_map[key_smt] = transforms_smt

	return solutions_smt_map

class Solution:
	def __init__(self, problem):
		self.problem = problem
		self.solutions_list = []

	def solveW(self, W_check, solutionsW_map):
		if not W_check in self.problem.state.locations_map:
			return
		check_pass = False
		while not check_pass:
			W_now = self.problem.state.locations_map[W_check]
			if ( W_check == W_now ):
				check_pass = True
			else:
				if not (W_now, W_check) in solutionsW_map:
					break
				solutions = solutionsW_map[(W_now, W_check)]
				print("W key:", (W_now, W_check))
				print("W solutions:", solutions)
				for t in solutions:
					self.problem.state.transform(t)
				self.solutions_list += solutions

	def solveWV(self, W_check, V_check, solutionsWV_map):
		if not W_check in self.problem.state.locations_map:
			return
		check_pass = False
		while not check_pass:
			W_now = self.problem.state.locations_map[W_check]
			V_now = self.problem.state.orientations_map[W_check]
			if ( W_check == W_now and V_check == V_now ):
				check_pass = True
			else:
				if not ((W_now,V_now),(W_check,V_check)) in solutionsWV_map:
					break
				solutions = solutionsWV_map[((W_now,V_now),(W_check,V_check))]
				print("WV key:", ((W_now,V_now),(W_check,V_check)))
				print("WV solutions:", solutions)
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

	def solve_smt(self, W_check, V_check, solutionsW_map, solutionsWV_map, smt_list):
		self.solveW(W_check, solutionsW_map)
		self.solveWV(W_check, V_check, solutionsWV_map)
		for smt in smt_list:
			solutionsW_map = conjugate_solutions_W(solutionsW_map, smt)
			solutionsWV_map = conjugate_solutions_WV(solutionsWV_map, smt)
			W_check = smt.conjugate([W_check])[0]
			self.solveW(W_check, solutionsW_map)
			self.solveWV(W_check, V_check, solutionsWV_map)
