from ..base.symbol import *
from ..base.state import *
from ..solve.problem import *
from ..solve.solver import *
from .examine import *

def gen_problem(N, WV_toChange, WV_toRemove = None):
	problem = Problem(N)

	for w in WV_toChange:
		if WV_toChange[w]:
			problem.state.locations_map[w] = WV_toChange[w][0]
			problem.state.orientations_map[w] = WV_toChange[w][1]
		else:
			del problem.state.locations_map[w]
			del problem.state.orientations_map[w]

	if WV_toRemove:
		for w in WV_toRemove:
			del problem.state.locations_map[w]
			del problem.state.orientations_map[w]

	return problem

def examine_solver(problem, solver, examiner):
	solutions = solver.solve(problem)
	print("solutions:")
	print(solutions)

	ok = examiner.test(problem.state)
	print("total same:", examiner.same_count)
	print("total shift:", examiner.shift_count)
	print("total error:", examiner.error_count)
	print("ok:", bool(ok))
	print()

	return ok

def smt_examination(smt, WV_toChange):
	WV_smt_toChange = {}
	for W_check in WV_toChange:
		if WV_toChange[W_check]:
			V_check = V_XYZ
			W_toChange = WV_toChange[W_check][0]
			V_toChange = WV_toChange[W_check][1]
			W_smt_toChange, V_smt_toChange, W_smt_check, V_smt_check = \
				smt_conjugate_WV(smt, W_toChange, V_toChange, W_check, V_check, fixed_V_to = True)
			WV_smt_toChange[W_smt_check] = (W_smt_toChange, V_smt_toChange)
		else:
			W_smt_check = smt.conjugate([W_check])[0]
			WV_smt_toChange[W_smt_check] = None
	return WV_smt_toChange

class SolverExaminer:
	def __init__(self):
		self.passed = 0
		self.no_passed = 0

	def examine(self, N, examination, solver, examiner, smt_orders = []):
		print(examination)
		ok = examine_solver(gen_problem(N, examination), solver, examiner)
		if ok:
			self.passed += 1
		else:
			self.no_passed += 1

		for smt in smt_orders:
			examination = smt_examination(smt, examination)
			print(examination)
			ok = examine_solver(gen_problem(N, examination), solver, examiner)
			if ok:
				self.passed += 1
			else:
				self.no_passed += 1

	def output_results(self):
		print("examination passed:", self.passed)
		print("examination not passed:", self.no_passed)

def check_examine_solver(N, examinations, solver, examiner, smt_orders = []):
	solver_examiner = SolverExaminer()
	for e in examinations:
		solver_examiner.examine(N, e, solver, examiner, smt_orders)
	solver_examiner.output_results()
