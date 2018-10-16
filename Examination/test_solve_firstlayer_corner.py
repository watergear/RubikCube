if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.firstlayer_corner import *
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
])

examiner = Examiner([], [], locked_areas, dump_message = False)

examinations_list = [
	{
	W(n,-n,-n) :
		(W(n,n,-n), V('X','-Z','Y')),
	},
	{
	W(n,-n,-n) :
		(W(n,n,-n), V('-Y','X','Z')),
	},
	{
	W(n,-n,-n) :
		(W(n,n,-n), V('-Z','-Y','-X')),
	},

	{
	W(n,-n,-n) :
		(W(-n,n,-n), V('Y','-Z','-X')),
	},
	{
	W(n,-n,-n) :
		(W(-n,n,-n), V('Z','X','Y')),
	},
	{
	W(n,-n,-n) :
		(W(-n,n,-n), V('-X','-Y','Z')),
	},

	{
	W(n,-n,-n) :
		(W(-n,n,n), V('-X','-Z','-Y')),
	},
	{
	W(n,-n,-n) :
		(W(-n,n,n), V('Y','X','-Z')),
	},
	{
	W(n,-n,-n) :
		(W(-n,n,n), V('Z','-Y','X')),
	},

	{
	W(n,-n,-n) :
		(W(n,n,n), V('-Y','-Z','X')),
	},
	{
	W(n,-n,-n) :
		(W(n,n,n), V('-Z','X','-Y')),
	},
	{
	W(n,-n,-n) :
		(W(n,n,n), V('X','-Y','-Z')),
	},


	{
	W(n,-n,-n) :
		(W(n,-n,-n), V('-Z','-X','Y')),
	},
	{
	W(n,-n,-n) :
		(W(n,-n,-n), V('-Y','Z','-X')),
	},
	{
	W(n,-n,-n) :
		(W(n,-n,-n), V('X','Y','Z')),
	},

	{
	W(n,-n,-n) :
		(W(-n,-n,-n), V('Y','-X','Z')),
	W(-n,-n,-n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(-n,-n,-n), V('-X','Z','Y')),
	W(-n,-n,-n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(-n,-n,-n), V('Z','Y','-X')),
	W(-n,-n,-n) :
		None,
	},

	{
	W(n,-n,-n) :
		(W(-n,-n,n), V('Z','-X','-Y')),
	W(-n,-n,n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(-n,-n,n), V('Y','Z','X')),
	W(-n,-n,n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(-n,-n,n), V('-X','Y','-Z')),
	W(-n,-n,n) :
		None,
	},

	{
	W(n,-n,-n) :
		(W(n,-n,n), V('-Y','-X','-Z')),
	W(n,-n,n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(n,-n,n), V('X','Z','-Y')),
	W(n,-n,n) :
		None,
	},
	{
	W(n,-n,-n) :
		(W(n,-n,n), V('-Z','Y','X')),
	W(n,-n,n) :
		None,
	},
]

smt_orders = [
	SMT_RY,
	SMT_RY,
	SMT_RY,
]

solver = FirstLayerCornerSolver()

check_examine_solver(N, examinations_list, solver, examiner, smt_orders)