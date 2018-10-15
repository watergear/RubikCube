from PyRubikCube.base.symbol import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.lastlayer_edge_midpoint import *
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

solver = LastLayerEdgeMidpointSolver()

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


examinations_V_list = [
	examination_0000,
	examination_1010,
	examination_0101,
	examination_1001,
	examination_0011,
	examination_0110,
	examination_1100,
]

for e in examinations_V_list:
	solver_examiner.examine(N, e, solver, examiner)

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

examinations_W_list = []
for W_order in W_order_list:
	examination = {}
	for i in range(len(W_set)):
		W_new = W_set[W_order[i]]
		smt = W_SMT_list[(W_order[i] - i) % len(W_set)]
		V_new = smt.conjugate([V_XYZ])[0]
		examination[W_set[i]] = (W_new, V_new)
	examinations_W_list += [examination]

for e in examinations_W_list:
	solver_examiner.examine(N, e, solver, examiner)

solver_examiner.output_results()
