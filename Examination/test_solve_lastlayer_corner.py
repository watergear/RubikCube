if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.lastlayer_corner import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.examine.solve import *

N = 3
n = int(N/2)

solver_examiner = SolverExaminer()

numeric_area_factory = NumericAreaFactory(n)
numeric_area_all 		= 	numeric_area_factory.all()
numeric_area_inner 		= 	numeric_area_factory.inner()
numeric_area_center_L 	= 	numeric_area_factory.center_L()
numeric_area_center_R 	= 	numeric_area_factory.center_R()
numeric_area_center_D 	= 	numeric_area_factory.center_D()
numeric_area_center_U 	= 	numeric_area_factory.center_U()
numeric_area_center_F 	= 	numeric_area_factory.center_F()
numeric_area_center_B 	= 	numeric_area_factory.center_B()
numeric_area_edge_UB 	= 	numeric_area_factory.edge_UB()
numeric_area_edge_UF 	= 	numeric_area_factory.edge_UF()
numeric_area_edge_DB 	= 	numeric_area_factory.edge_DB()
numeric_area_edge_DF 	= 	numeric_area_factory.edge_DF()
numeric_area_edge_RB 	= 	numeric_area_factory.edge_RB()
numeric_area_edge_RF 	= 	numeric_area_factory.edge_RF()
numeric_area_edge_LB 	= 	numeric_area_factory.edge_LB()
numeric_area_edge_LF 	= 	numeric_area_factory.edge_LF()
numeric_area_edge_RU 	= 	numeric_area_factory.edge_RU()
numeric_area_edge_RD 	= 	numeric_area_factory.edge_RD()
numeric_area_edge_LU 	= 	numeric_area_factory.edge_LU()
numeric_area_edge_LD 	= 	numeric_area_factory.edge_LD()
numeric_area_corner_LDF	=	numeric_area_factory.corner_LDF()
numeric_area_corner_LDB	=	numeric_area_factory.corner_LDB()
numeric_area_corner_LUF	=	numeric_area_factory.corner_LUF()
numeric_area_corner_LUB	=	numeric_area_factory.corner_LUB()
numeric_area_corner_RDF	=	numeric_area_factory.corner_RDF()
numeric_area_corner_RDB	=	numeric_area_factory.corner_RDB()
numeric_area_corner_RUF	=	numeric_area_factory.corner_RUF()
numeric_area_corner_RUB	=	numeric_area_factory.corner_RUB()
numeric_area_center_L_around	=	numeric_area_factory.center_L_around()
numeric_area_center_R_around	=	numeric_area_factory.center_R_around()
numeric_area_center_D_around	=	numeric_area_factory.center_D_around()
numeric_area_center_U_around	=	numeric_area_factory.center_U_around()
numeric_area_center_F_around	=	numeric_area_factory.center_F_around()
numeric_area_center_B_around	=	numeric_area_factory.center_B_around()
numeric_area_core_midpoint		=	numeric_area_factory.core_midpoint()
numeric_area_center_midpoint_L	=	numeric_area_factory.center_midpoint_L()
numeric_area_center_midpoint_R	=	numeric_area_factory.center_midpoint_R()
numeric_area_center_midpoint_D	=	numeric_area_factory.center_midpoint_D()
numeric_area_center_midpoint_U	=	numeric_area_factory.center_midpoint_U()
numeric_area_center_midpoint_F	=	numeric_area_factory.center_midpoint_F()
numeric_area_center_midpoint_B	=	numeric_area_factory.center_midpoint_B()
numeric_area_edge_midpoint_UB	=	numeric_area_factory.edge_midpoint_UB()
numeric_area_edge_midpoint_UF	=	numeric_area_factory.edge_midpoint_UF()
numeric_area_edge_midpoint_DB	=	numeric_area_factory.edge_midpoint_DB()
numeric_area_edge_midpoint_DF	=	numeric_area_factory.edge_midpoint_DF()
numeric_area_edge_midpoint_RB	=	numeric_area_factory.edge_midpoint_RB()
numeric_area_edge_midpoint_RF	=	numeric_area_factory.edge_midpoint_RF()
numeric_area_edge_midpoint_LB	=	numeric_area_factory.edge_midpoint_LB()
numeric_area_edge_midpoint_LF	=	numeric_area_factory.edge_midpoint_LF()
numeric_area_edge_midpoint_RU	=	numeric_area_factory.edge_midpoint_RU()
numeric_area_edge_midpoint_RD	=	numeric_area_factory.edge_midpoint_RD()
numeric_area_edge_midpoint_LU	=	numeric_area_factory.edge_midpoint_LU()
numeric_area_edge_midpoint_LD	=	numeric_area_factory.edge_midpoint_LD()

locked_areas = Areas([
	numeric_area_inner,

	numeric_area_center_L,
	numeric_area_center_R,
	numeric_area_center_D,
	numeric_area_center_U,
	numeric_area_center_F,
	numeric_area_center_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	numeric_area_corner_LDF,
	numeric_area_corner_LDB,
	numeric_area_corner_RDF,
	numeric_area_corner_RDB,

	numeric_area_edge_midpoint_RB,
	numeric_area_edge_midpoint_RF,
	numeric_area_edge_midpoint_LB,
	numeric_area_edge_midpoint_LF,

	numeric_area_edge_midpoint_LU,
	numeric_area_edge_midpoint_RU,
	numeric_area_edge_midpoint_UF,
	numeric_area_edge_midpoint_UB,

	numeric_area_corner_LUF,
	numeric_area_corner_LUB,
	numeric_area_corner_RUF,
	numeric_area_corner_RUB,
])

examiner = Examiner([], [], locked_areas, dump_message = False)

locked_areas1 = Areas([
	numeric_area_inner,

	numeric_area_center_L,
	numeric_area_center_R,
	numeric_area_center_D,
	numeric_area_center_U,
	numeric_area_center_F,
	numeric_area_center_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	numeric_area_corner_LDF,
	numeric_area_corner_LDB,
	numeric_area_corner_RDF,
	numeric_area_corner_RDB,

	numeric_area_edge_midpoint_RB,
	numeric_area_edge_midpoint_RF,
	numeric_area_edge_midpoint_LB,
	numeric_area_edge_midpoint_LF,

	numeric_area_edge_midpoint_LU,
	numeric_area_edge_midpoint_RU,
	numeric_area_edge_midpoint_UF,
	numeric_area_edge_midpoint_UB,

	numeric_area_corner_RUF,
])

examiner1 = Examiner([], [], locked_areas1, dump_message = False)

examinations_list_step1 = [
	{
	W(n,n,-n) :
		(W(n,n,n), V('-Z','Y','X')),
	},

	{
	W(n,n,-n) :
		(W(n,n,n), V('Y','X','-Z')),
	},

	{
	W(n,n,-n) :
		(W(n,n,n), V('X','-Z','Y')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,n), V('-X','Y','-Z')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,n), V('Z','X','Y')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,n), V('-Y','-Z','X')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,-n), V('Z','Y','-X')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,-n), V('-Y','X','Z')),
	},

	{
	W(n,n,-n) :
		(W(-n,n,-n), V('-X','-Z','-Y')),
	},

	{
	W(n,n,-n) :
		(W(n,n,-n), V_XYZ),
	},

	{
	W(n,n,-n) :
		(W(n,n,-n), V('-Z','X','-Y')),
	},

	{
	W(n,n,-n) :
		(W(n,n,-n), V('Y','-Z','-X')),
	},
]

class LastLayerCornerSolver1(LastLayerCornerSolver):
	# need to turn off step4
	def solve(self, problem):
		return self.solve_step1(problem)
solver1 = LastLayerCornerSolver1()

for e in examinations_list_step1:
	solver_examiner.examine(N, e, solver1, examiner1)

locked_areas2 = Areas([
	numeric_area_inner,

	numeric_area_center_L,
	numeric_area_center_R,
	numeric_area_center_D,
	numeric_area_center_U,
	numeric_area_center_F,
	numeric_area_center_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	numeric_area_corner_LDF,
	numeric_area_corner_LDB,
	numeric_area_corner_RDF,
	numeric_area_corner_RDB,

	numeric_area_edge_midpoint_RB,
	numeric_area_edge_midpoint_RF,
	numeric_area_edge_midpoint_LB,
	numeric_area_edge_midpoint_LF,

	numeric_area_edge_midpoint_LU,
	numeric_area_edge_midpoint_RU,
	numeric_area_edge_midpoint_UF,
	numeric_area_edge_midpoint_UB,

	numeric_area_corner_RUF,
])

src_vectors_2 = [
	(W(n, n, n),		V('X', 'Y', 'Z')),
]
dest_vectors_2 = [
	(W(-n, n, n),		V('-Z', 'Y', 'X')),
]

examiner2 = Examiner(src_vectors_2, dest_vectors_2, locked_areas2, dump_message = False)

examinations_list_step2 = [
	{
	W(n,n,n) :
		(W(n,n,n), V('X','Y','Z')),
	},
	
	{
	W(n,n,n) :
		(W(n,n,n), V('Y','Z','X')),
	},
	
	{
	W(n,n,n) :
		(W(n,n,n), V('Z','X','Y')),
	},
	
	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-X','Z','Y')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-Y','X','Z')),
	},

	{
	W(n,n,n) :
		(W(-n,n,-n), V('-X','Y','-Z')),
	},

	{
	W(n,n,n) :
		(W(-n,n,-n), V('-Y','Z','-X')),
	},

	{
	W(n,n,n) :
		(W(-n,n,-n), V('-Z','X','-Y')),
	},
]

class LastLayerCornerSolver2(LastLayerCornerSolver):
	# need to turn off step3, step4
	def solve(self, problem):
		return self.solve_step2(problem)
solver2 = LastLayerCornerSolver2()

for e in examinations_list_step2:
	solver_examiner.examine(N, e, solver2, examiner2)

examiner3 = examiner

examinations_list_step3 = [
	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(-n,n,-n), V('-Z','Y','X')),
	W(-n,n,-n) :
		(W(n,n,n), V('-X','Y','-Z')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(-n,n,-n), V('X','Z','-Y')),
	W(-n,n,-n) :
		(W(n,n,n), V('Y','-Z','-X')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(-n,n,-n), V('-Y','-X','-Z')),
	W(-n,n,-n) :
		(W(n,n,n), V('-Z','-X','Y')),
	},
]

class LastLayerCornerSolver3(LastLayerCornerSolver):
	def solve(self, problem):
		return self.solve_step3(problem)
solver3 = LastLayerCornerSolver3()

for e in examinations_list_step3:
	solver_examiner.examine(N, e, solver3, examiner3)

locked_areas3_even = Areas([
	numeric_area_inner,

	numeric_area_center_L,
	numeric_area_center_R,
	numeric_area_center_D,
	numeric_area_center_U,
	numeric_area_center_F,
	numeric_area_center_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	numeric_area_corner_LDF,
	numeric_area_corner_LDB,
	numeric_area_corner_RDF,
	numeric_area_corner_RDB,

	numeric_area_edge_midpoint_RB,
	numeric_area_edge_midpoint_RF,
	numeric_area_edge_midpoint_LB,
	numeric_area_edge_midpoint_LF,

	numeric_area_edge_midpoint_LU,
	numeric_area_edge_midpoint_RU,
	numeric_area_edge_midpoint_UF,
	numeric_area_edge_midpoint_UB,

	numeric_area_corner_LUF,
	numeric_area_corner_RUF,
])

src_vectors_3_even = [
	(W(n, n, n),		V('X', 'Y', 'Z')),
	(W(-n, n, n),		V('X', 'Y', 'Z')),
]
dest_vectors_3_even = [
	(W(-n, n, n),		V('-Z', 'Y', 'X')),
	(W(n, n, n),		V('Z', 'Y', '-X')),
]

examiner3_even = Examiner(src_vectors_3_even, dest_vectors_3_even, locked_areas3_even, dump_message = False)

examinations_list_step3_even = [
	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(n,n,n), V('Z','Y','-X')),
	W(-n,n,-n) :
		(W(-n,n,-n), V('X','Y','Z')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(n,n,n), V('Y','-X','Z')),
	W(-n,n,-n) :
		(W(-n,n,-n), V('Z','-X','-Y')),
	},

	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(n,n,n), V('-X','Z','Y')),
	W(-n,n,-n) :
		(W(-n,n,-n), V('-Y','-Z','X')),
	},
]

class LastLayerCornerSolver3_even(LastLayerCornerSolver):
	# need to turn off step4
	def solve(self, problem):
		return self.solve_step3(problem)
solver3_even = LastLayerCornerSolver3_even()

for e in examinations_list_step3_even:
	solver_examiner.examine(N, e, solver3_even, examiner3_even)

locked_areas4 = Areas([
	numeric_area_inner,

	numeric_area_center_L,
	numeric_area_center_R,
	numeric_area_center_D,
	# numeric_area_center_U,
	numeric_area_center_U_around,
	numeric_area_center_F,
	numeric_area_center_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	numeric_area_corner_LDF,
	numeric_area_corner_LDB,
	numeric_area_corner_RDF,
	numeric_area_corner_RDB,

	numeric_area_edge_midpoint_RB,
	numeric_area_edge_midpoint_RF,
	numeric_area_edge_midpoint_LB,
	numeric_area_edge_midpoint_LF,

	numeric_area_edge_midpoint_LU,
	numeric_area_edge_midpoint_RU,
	# numeric_area_edge_midpoint_UF,
	# numeric_area_edge_midpoint_UB,

	numeric_area_corner_LUF,
	numeric_area_corner_LUB,
	numeric_area_corner_RUF,
	numeric_area_corner_RUB,
])

examiner4 = Examiner([], [], locked_areas4, dump_message = False)

examinations_list_step4 = [
	{
	W(n,n,n) :
		(W(-n,n,n), V('-Z','Y','X')),
	W(-n,n,n) :
		(W(n,n,n), V('Z','Y','-X')),
	},
]

class LastLayerCornerSolver4(LastLayerCornerSolver):
	# test step4 only
	def solve(self, problem):
		return self.solve_step4(problem)
solver4 = LastLayerCornerSolver4()

for e in examinations_list_step4:
	solver_examiner.examine(N, e, solver4, examiner4)

solver_examiner.output_results()
