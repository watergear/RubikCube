from PyRubikCube.base.symbol import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.firstlayer_edge_midpoint import *

N = 3
n = int(N/2)
odd = (1 == N % 2)

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
])

examiner = Examiner([], [], locked_areas, dump_message = False)

no_pass = 0;
def examine_solution(W_check, W_new, V_new):
	global no_pass
	global N, n, odd
	global examiner

	problem = Problem(N)
	problem.state.locations_map[W_check] = W_new
	problem.state.orientations_map[W_check] = V_new
	if not W_check == W_new:
		del problem.state.locations_map[W_new]
		del problem.state.orientations_map[W_new]

	s = FirstLayerEdgeMidpointSolution(problem)
	solutions_tlist = s.solve()
	print("solutions:")
	print(solutions_tlist)

	ok = examiner.test(problem.state)
	print("total same:", examiner.same_count)
	print("total shift:", examiner.shift_count)
	print("total error:", examiner.error_count)
	print("ok:", bool(ok))
	print()

	if not ok:
		no_pass += 1

examinations_list = [
	(
	W(-n,0,-n),	V('Y','-X','Z'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(-n,0,-n),	V('Z','X','Y'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(-n,0,n),	V('Y','X','-Z'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(-n,0,n),	V('Z','-X','-Y'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(n,0,-n),	V('-Y','X','Z'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(n,0,-n),	V('-Z','-X','Y'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(n,0,n),	V('-Y','-X','-Z'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(n,0,n),	V('-Z','X','-Y'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(n,n,0),	V('-Y','-Z','X'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(n,n,0),	V('-Z','-Y','-X'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(-n,n,0),	V('Y','-Z','-X'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(-n,n,0),	V('Z','-Y','X'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(0,n,n),	V('-X','-Z','-Y'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(0,n,n),	V('X','-Y','-Z'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(0,n,-n),	V('X','-Z','Y'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(0,n,-n),	V('-X','-Y','Z'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(n,-n,0),	V('-Y','Z','-X'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(n,-n,0),	V('-Z','Y','X'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(-n,-n,0),	V('Y','Z','X'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(-n,-n,0),	V('Z','Y','-X'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(0,-n,n),	V('X','Z','-Y'),
	W(0,-n,-n),	V_XYZ,
	),
	(
	W(0,-n,n),	V('-X','Y','-Z'),
	W(0,-n,-n),	V_XYZ,
	),

	(
	W(0,-n,-n),	V('-X','Z','Y'),
	W(0,-n,-n),	V_XYZ,
	),
]

for W_new, V_new, W_check, V_check in examinations_list:
	examine_solution(W_check, W_new, V_new)

smt_list = [
	SMT_RY,
	SMT_RY,
	SMT_RY,
]
for smt in smt_list:
	examinations_list = \
		[smt_conjugate_WV(smt, W_new, V_new, W_check, V_check, fixed_V_to = True) \
			for W_new, V_new, W_check, V_check in examinations_list]
	for W_new, V_new, W_check, V_check in examinations_list:
		examine_solution(W_check, W_new, V_new)

if ( no_pass > 0 ):
	print("No pass:", no_pass)
