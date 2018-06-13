from PyRubikCube.base.symbol import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.lastlayer_edge_midpoint import *

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
	numeric_area_edge_midpoint_UF,
	numeric_area_edge_midpoint_UB,
])

examiner = Examiner([], [], locked_areas, dump_message = False)

no_pass = 0;
def examine_solution(WV_map):
	global no_pass
	global N, n, odd
	global examiner

	problem = Problem(N)
	# problem.state.locations_map[W_check] = W_new
	# problem.state.orientations_map[W_check] = V_new
	# if not W_check == W_new:
	# 	del problem.state.locations_map[W_new]
	# 	del problem.state.orientations_map[W_new]
	for w in WV_map:
		problem.state.locations_map[w] = WV_map[w][0]
		problem.state.orientations_map[w] = WV_map[w][1]

	s = LastLayerEdgeMidpointSolution(problem)
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

examination_0000 = {
	W(0,n,-n) :
		(W(0,n,-n),	V('-X','-Z','-Y')),

	W(-n,n,0) :
		(W(-n,n,0),	V('-Y','-X','-Z')),

	W(0,n,n) :
		(W(0,n,n),	V('-X','Z','Y')),

	W(n,n,0) :
		(W(n,n,0),	V('Y','X','-Z')),
}

examination_1010 = {
	W(0,n,-n) :
		(W(0,n,-n),	V_XYZ),

	W(-n,n,0) :
		(W(-n,n,0),	V('-Y','-X','-Z')),

	W(0,n,n) :
		(W(0,n,n),	V_XYZ),

	W(n,n,0) :
		(W(n,n,0),	V('Y','X','-Z')),
}

examination_0101 = {
	W(0,n,-n) :
		(W(0,n,-n),	V('-X','-Z','-Y')),

	W(-n,n,0) :
		(W(-n,n,0),	V_XYZ),

	W(0,n,n) :
		(W(0,n,n),	V('-X','Z','Y')),

	W(n,n,0) :
		(W(n,n,0),	V_XYZ),
}

examination_1001 = {
	W(0,n,-n) :
		(W(0,n,-n),	V_XYZ),

	W(-n,n,0) :
		(W(-n,n,0),	V('-Y','-X','-Z')),

	W(0,n,n) :
		(W(0,n,n),	V('-X','Z','Y')),

	W(n,n,0) :
		(W(n,n,0),	V_XYZ),
}

examination_0011 = {
	W(0,n,-n) :
		(W(0,n,-n),	V('-X','-Z','-Y')),

	W(-n,n,0) :
		(W(-n,n,0),	V('-Y','-X','-Z')),

	W(0,n,n) :
		(W(0,n,n),	V_XYZ),

	W(n,n,0) :
		(W(n,n,0),	V_XYZ),
}

examination_0110 = {
	W(0,n,-n) :
		(W(0,n,-n),	V('-X','-Z','-Y')),

	W(-n,n,0) :
		(W(-n,n,0),	V_XYZ),

	W(0,n,n) :
		(W(0,n,n),	V_XYZ),

	W(n,n,0) :
		(W(n,n,0),	V('Y','X','-Z')),
}

examination_1100 = {
	W(0,n,-n) :
		(W(0,n,-n),	V_XYZ),

	W(-n,n,0) :
		(W(-n,n,0),	V_XYZ),

	W(0,n,n) :
		(W(0,n,n),	V('-X','Z','Y')),

	W(n,n,0) :
		(W(n,n,0),	V('Y','X','-Z')),
}


examinations_list = [
	examination_0000,
	examination_1010,
	examination_0101,
	examination_1001,
	examination_0011,
	examination_0110,
	examination_1100,
]

for e in examinations_list:
	print(e)
	examine_solution(e)

W_set = [
	W(0,n,-n),
	W(-n,n,0),
	W(0,n,n),
	W(n,n,0),
]
W_SMT_list = [
	SMT_E,
	SMT_RNY,
	SMT_R2Y,
	SMT_RY,
]

W_order_list = []

def gen_W_order_list(W_order):
	global W_set, W_order_list

	if len(W_order) == len(W_set):
		W_order_list += [W_order]
		return

	for i in range(len(W_set)):
		if not i in W_order:
			gen_W_order_list(W_order+[i])

gen_W_order_list([])

examinations_order_list = []
for W_order in W_order_list:
	examination = {}
	for i in range(len(W_set)):
		W_new = W_set[W_order[i]]
		smt = W_SMT_list[(W_order[i] - i) % len(W_set)]
		V_new = smt.conjugate([V_XYZ])[0]
		examination[W_set[i]] = (W_new, V_new)
	examinations_order_list += [examination]

for e in examinations_order_list:
	print(e)
	examine_solution(e)

if ( no_pass > 0 ):
	print("No pass:", no_pass)
