from PyRubikCube.base.symbol import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.rubik_solver import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *

# problemn
N = 3
n = int(N/2)
odd = (1 == N % 2)

scrambles = [
	T("X+", 0),
	T("Z+", 0),
	T("Y-", 0),
	T("X+", n),
	T("Y-", -n),
	T("Z+", -n),
]

problem = Problem(N)
problem.scramble(scrambles)

# solve
solver = RubikSolver()
solutions = solver.solve(problem)
print("solutions:")
print(solutions)

# examine
state = gen_original_state(n, odd)
for t in scrambles: state.transform(t)
for t in solutions: state.transform(t)

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
	#area_all_n
	numeric_area_core_midpoint,

	numeric_area_center_midpoint_L,
	numeric_area_center_midpoint_R,
	numeric_area_center_midpoint_D,
	numeric_area_center_midpoint_U,
	numeric_area_center_midpoint_F,
	numeric_area_center_midpoint_B,

	numeric_area_edge_midpoint_DF,
	numeric_area_edge_midpoint_RD,
	numeric_area_edge_midpoint_DB,
	numeric_area_edge_midpoint_LD,

	# numeric_area_edge_midpoint_UB,
	# numeric_area_edge_midpoint_UF,
	# numeric_area_edge_midpoint_RB,
	# numeric_area_edge_midpoint_RF,
	# numeric_area_edge_midpoint_LB,
	# numeric_area_edge_midpoint_LF,
	# numeric_area_edge_midpoint_RU,
	# numeric_area_edge_midpoint_LU,
])

# examiner = Examiner([], [], locked_areas, dump_message = True)
examiner = Examiner([], [], locked_areas, dump_message = False)
ok = examiner.test(state)
print("total same:", examiner.same_count)
print("total shift:", examiner.shift_count)
print("total error:", examiner.error_count)
print("ok:", bool(ok))
