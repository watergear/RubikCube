if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.solve.center import *
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
	# numeric_area_center_U,
	numeric_area_center_U_around,
	numeric_area_center_F,
	numeric_area_center_B,
])

examiner = Examiner([], [], locked_areas, dump_message = False)

def gen_examinations(n, i, j):
	if 0 == i and 0 == j:
		return []
	
	sign = 1 if i == j else -1
	
	I = NumericIndex(i)
	J = NumericIndex(j)
	N = NumericIndex(n)
	SI = I * sign
	SJ = J * sign
	
	X = Factor('X', 1)
	Y = Factor('Y', 1)
	Z = Factor('Z', 1)
	SX = X * sign
	SY = Y * sign
	SZ = Z * sign
	
	return [
		# on U face
		{
		(I,J,-N) :
			((I,N,J), (X,-Z,Y)),
		(I,N,J) :
			((SJ,N,-SI), (SZ,Y,-SX)),
		(SJ,N,-SI) :
			((I,J,-N), (-SZ,SX,-Y)),
		},
		{
		(I,J,-N) :
			((J,N,-I), (Y,-Z,-X)),
		(J,N,-I) :
			((-SI,N,-SJ), (SZ,Y,-SX)),
		(-SI,N,-SJ):
			((I,J,-N), (-SX,-SZ,-Y)),
		},
		{
		(I,J,-N) :
			((-I,N,-J), (-X,-Z,-Y)),
		(-I,N,-J) :
			((-SJ,N,SI), (SZ,Y,-SX)),
		(-SJ,N,SI) :
			((I,J,-N), (SZ,-SX,-Y)),
		},
		{
		(I,J,-N) :
			((-J,N,I), (-Y,-Z,X)),
		(-J,N,I) :
			((SI,N,SJ), (SZ,Y,-SX)),
		(SI,N,SJ) :
			((I,J,-N), (SX,SZ,-Y)),
		},

		# on R face
		{
		(I,J,-N) :
			((N,-I,J), (-Z,-X,Y)),
		(N,-I,J) :
			((N,-SJ,-SI), (X,-SZ,SY)),
		(N,-SJ,-SI) :
			((I,J,-N), (-SZ,-SY,-X)),
		},
		{
		(I,J,-N) :
			((N,-J,-I), (-Z,-Y,-X)),
		(N,-J,-I) :
			((N,SI,-SJ), (X,-SZ,SY)),
		(N,SI,-SJ) :
			((I,J,-N), (SY,-SZ,-X)),
		},
		{
		(I,J,-N) :
			((N,I,-J), (-Z,X,-Y)),
		(N,I,-J) :
			((N,SJ,SI), (X,-SZ,SY)),
		(N,SJ,SI) :
			((I,J,-N), (SZ,SY,-X)),
		},
		{
		(I,J,-N) :
			((N,J,I), (-Z,Y,X)),
		(N,J,I) :
			((N,-SI,SJ), (X,-SZ,SY)),
		(N,-SI,SJ):
			((I,J,-N), (-SY,SZ,-X)),
		},

		# on L face
		{
		(I,J,-N) :
			((-N,I,J), (Z,X,Y)),
		(-N,I,J) :
			((-N,SJ,-SI), (X,SZ,-SY)),
		(-N,SJ,-SI) :
			((I,J,-N), (-SZ,SY,X)),
		},
		{
		(I,J,-N) :
			((-N,-J,I), (Z,-Y,X)),
		(-N,-J,I) :
			((-N,SI,SJ), (X,SZ,-SY)),
		(-N,SI,SJ) :
			((I,J,-N), (SY,SZ,X)),
		},
		{
		(I,J,-N) :
			((-N,-I,-J), (Z,-X,-Y)),
		(-N,-I,-J) :
			((-N,-SJ,SI), (X,SZ,-SY)),
		(-N,-SJ,SI) :
			((I,J,-N), (SZ,-SY,X)),
		},
		{
		(I,J,-N) :
			((-N,J,-I), (Z,Y,-X)),
		(-N,J,-I) :
			((-N,-SI,-SJ), (X,SZ,-SY)),
		(-N,-SI,-SJ) :
			((I,J,-N), (-SY,-SZ,X)),
		},

		# on D face
		{
		(I,J,-N) :
			((-I,-N,J), (-X,Z,Y)),
		(-I,-N,J) :
			((-SJ,-N,-SI), (-SZ,Y,SX)),
		(-SJ,-N,-SI):
			((I,J,-N), (-SZ,-SX,Y)),
		},
		{
		(I,J,-N) :
			((J,-N,I), (Y,Z,X)),
		(J,-N,I) :
			((-SI,-N,SJ), (-SZ,Y,SX)),
		(-SI,-N,SJ):
			((I,J,-N), (-SX,SZ,Y)),
		},
		{
		(I,J,-N) :
			((I,-N,-J), (X,Z,-Y)),
		(I,-N,-J) :
			((SJ,-N,SI), (-SZ,Y,SX)),
		(SJ,-N,SI):
			((I,J,-N), (SZ,SX,Y)),
		},
		{
		(I,J,-N) :
			((-J,-N,-I), (-Y,Z,-X)),
		(-J,-N,-I) :
			((SI,-N,-SJ), (-SZ,Y,SX)),
		(SI,-N,-SJ):
			((I,J,-N), (SX,-SZ,Y)),
		},

		# on B face
		{
		(I,J,-N) :
			((I,-J,N), (X,-Y,-Z)),
		(I,-J,N) :
			((SJ,SI,N), (-SY,SX,Z)),
		(SJ,SI,N) :
			((I,J,-N), (SY,SX,-Z)),
		},
		{
		(I,J,-N) :
			((J,I,N), (Y,X,-Z)),
		(J,I,N) :
			((-SI,SJ,N), (-SY,SX,Z)),
		(-SI,SJ,N):
			((I,J,-N), (-SX,SY,-Z)),
		},
		{
		(I,J,-N) :
			((-I,J,N), (-X,Y,-Z)),
		(-I,J,N) :
			((-SJ,-SI,N), (-SY,SX,Z)),
		(-SJ,-SI,N):
			((I,J,-N), (-SY,-SX,-Z)),
		},
		{
		(I,J,-N) :
			((-J,-I,N), (-Y,-X,-Z)),
		(-J,-I,N) :
			((SI,-SJ,N), (-SY,SX,Z)),
		(SI,-SJ,N):
			((I,J,-N), (SX,-SY,-Z)),
		},

		# on F face
		{
		(I,J,-N) :
			((I,J,-N), (X,Y,Z)),
		},
		{
		(I,J,-N) :
			((-J,I,-N), (-Y,X,Z)),
		(-J,I,-N) :
			((-I,-J,-N), (-Y,X,Z)),
		(-I,-J,-N) :
			((I,J,-N), (-X,-Y,Z)),
		},
		{
		(I,J,-N) :
			((-I,-J,-N), (-X,-Y,Z)),
		(-I,-J,-N) :
			((-J,I,-N), (Y,-X,Z)),
		(-J,I,-N) :
			((I,J,-N), (Y,-X,Z)),
		},
		{
		(I,J,-N) :
			((J,-I,-N), (Y,-X,Z)),
		(J,-I,-N) :
			((-I,-J,-N), (Y,-X,Z)),
		(-I,-J,-N):
			((I,J,-N), (-X,-Y,Z)),
		},
	]

examinations_list = []
lower = -n+1
upper = n-1
for i in range(lower, upper+1):
	for j in range(lower, upper+1):
		examinations_list += gen_examinations(n, i, j)

smt_init_orders = [
	SMT_RX, # F,U -> D,F
	SMT_RY, # D,F -> D,R
]
for smt in smt_init_orders:
	examinations_list = [smt_examination(smt, e) for e in examinations_list]

smt_orders = [
	SMT_RNZ, # D,R -> R,U
	SMT_RY, # R,U -> B,U
	SMT_RY, # B,U -> L,U
	SMT_RY, # L,U -> F,U
	SMT_RNX, # F,U -> U,B
]

solver = CenterSolver()

check_examine_solver(N, examinations_list, solver, examiner, smt_orders)