if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.solve.edge import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.examine.solve import *

N = 9
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

	numeric_area_edge_DF,
	numeric_area_edge_RD,
	numeric_area_edge_DB,
	numeric_area_edge_LD,
	numeric_area_edge_RB,
	numeric_area_edge_RF,
	numeric_area_edge_LB,
	numeric_area_edge_LF,
	numeric_area_edge_LU,
	numeric_area_edge_RU,
	numeric_area_edge_UF,
	numeric_area_edge_UB,
])

examiner = Examiner([], [], locked_areas, dump_message = False)

def gen_examinations(n, i):
	if 0 == i:
		return []

	I = NumericIndex(i)
	N = NumericIndex(n)
	X = Factor('X', 1)
	Y = Factor('Y', 1)
	Z = Factor('Z', 1)
	
	wA1 = (I,N,-N)
	tA1 = [T('X-')]
	tB1 = [T('X+'),T('Y+'),T('Y+')]

	wA2 = (I,N,-N)
	tA2 = [T('Y+'),T('Y+')]
	tB2 = [T('Y+'),T('Y+'),T('X-')]

	return [
		# on UB edge
		conjugate_examination(wA1, tA1, tB1, []),
		conjugate_examination(wA2, tA2, tB2, []),

		# on LB edge
		conjugate_examination(wA1, tA1, tB1, [T('Z-')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z-')]),

		# on RB edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+')]),

		# on DB edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+'),T('Z+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+'),T('Z+')]),

		# on LU edge
		conjugate_examination(wA1, tA1, tB1, [T('Z-'),T('X+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z-'),T('X+')]),

		# on RU edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+'),T('X+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+'),T('X+')]),

		# on LD edge
		conjugate_examination(wA1, tA1, tB1, [T('Z-'),T('X-')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z-'),T('X-')]),

		# on RD edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+'),T('X-')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+'),T('X-')]),

		# on LF edge
		conjugate_examination(wA1, tA1, tB1, [T('Z-'),T('X+'),T('X+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z-'),T('X+'),T('X+')]),

		# on RF edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+'),T('X+'),T('X+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+'),T('X+'),T('X+')]),

		# on DF edge
		conjugate_examination(wA1, tA1, tB1, [T('Z+'),T('Z+'),T('Y+'),T('Y+')]),
		conjugate_examination(wA2, tA2, tB2, [T('Z+'),T('Z+'),T('Y+'),T('Y+')]),

		# on UF edge
		# {
		# (I,N,-N) :
		# 	((I,N,-N), V_XYZ),
		# },
		{
		(I,N,-N) :
			((-I,N,-N), (-X,-Z,-Y)),
		(-I,N,-N) :
			((N,N,I), (Y,-Z,-X)),
		(N,N,I) :
			((I,N,-N), (Z,Y,-X)),
		}
	]

examinations_list = []
lower = -n+1
upper = n-1
for i in range(lower, upper+1):
	examinations_list += gen_examinations(n, i)

smt_init_orders = [
	SMT_RX,  # UF,RU -> DF,RF
]
for smt in smt_init_orders:
	examinations_list = [smt_examination(smt, e) for e in examinations_list]

smt_orders = [
	SMT_RY,  # DF,RF -> RD,RB
	SMT_RY,  # RD,RB -> DB,LB
	SMT_RY,  # DB,LB -> LD,LF
	SMT_RNX, # LD,LF -> LF,LU
	SMT_RY,  # LF,LU -> RF,UF
	SMT_RY,  # RF,UF -> RB,RU
	SMT_RY,  # RB,RU -> LB,UB
	SMT_RX,  # LB,UB -> LU,UF
	SMT_RY,  # LU,UF -> UF,RU
	SMT_RY,  # UF,RU -> RU,UB
	SMT_RY,  # RU,UB -> UB,LU
]

solver = EdgeSolver()

check_examine_solver(N, examinations_list, solver, examiner, smt_orders)