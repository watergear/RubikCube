from PyRubikCube.base.symbol import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.firstlayer_edge_midpoint import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.examine.solve import *

N = 3
n = int(N/2)

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

examinations_list = [
	{
	W(0,-n,-n) :
		(W(-n,0,-n),	V('Y','-X','Z')),
	},
	{
	W(0,-n,-n) :
		(W(-n,0,-n),	V('Z','X','Y')),
	},

	{
	W(0,-n,-n) :
		(W(-n,0,n),	V('Y','X','-Z')),
	},
	{
	W(0,-n,-n) :
		(W(-n,0,n),	V('Z','-X','-Y')),
	},

	{
	W(0,-n,-n) :
		(W(n,0,-n),	V('-Y','X','Z')),
	},
	{
	W(0,-n,-n) :
		(W(n,0,-n),	V('-Z','-X','Y')),
	},

	{
	W(0,-n,-n) :
		(W(n,0,n),	V('-Y','-X','-Z')),
	},
	{
	W(0,-n,-n) :
		(W(n,0,n),	V('-Z','X','-Y')),
	},

	{
	W(0,-n,-n) :
		(W(n,n,0),	V('-Y','-Z','X')),
	},
	{
	W(0,-n,-n) :
		(W(n,n,0),	V('-Z','-Y','-X')),
	},

	{
	W(0,-n,-n) :
		(W(-n,n,0),	V('Y','-Z','-X')),
	},
	{
	W(0,-n,-n) :
		(W(-n,n,0),	V('Z','-Y','X')),
	},

	{
	W(0,-n,-n) :
		(W(0,n,n),	V('-X','-Z','-Y')),
	},
	{
	W(0,-n,-n) :
		(W(0,n,n),	V('X','-Y','-Z')),
	},

	{
	W(0,-n,-n) :
		(W(0,n,-n),	V('X','-Z','Y')),
	},
	{
	W(0,-n,-n) :
		(W(0,n,-n),	V('-X','-Y','Z')),
	},

	{
	W(0,-n,-n) :
		(W(n,-n,0),	V('-Y','Z','-X')),
	W(n,-n,0) :
		None,
	},
	{
	W(0,-n,-n) :
		(W(n,-n,0),	V('-Z','Y','X')),
	W(n,-n,0) :
		None,
	},

	{
	W(0,-n,-n) :
		(W(-n,-n,0),	V('Y','Z','X')),
	W(-n,-n,0) :
		None,
	},
	{
	W(0,-n,-n) :
		(W(-n,-n,0),	V('Z','Y','-X')),
	W(-n,-n,0) :
		None,
	},

	{
	W(0,-n,-n) :
		(W(0,-n,n),	V('X','Z','-Y')),
	W(0,-n,n) :
		None,
	},
	{
	W(0,-n,-n) :
		(W(0,-n,n),	V('-X','Y','-Z')),
	W(0,-n,n) :
		None,
	},

	{
	W(0,-n,-n) :
		(W(0,-n,-n),	V('-X','Z','Y')),
	},
]

smt_orders = [
	SMT_RY,
	SMT_RY,
	SMT_RY,
]

solver = FirstLayerEdgeMidpointSolver()

check_examine_solver(N, examinations_list, solver, examiner, smt_orders)