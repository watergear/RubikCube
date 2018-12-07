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
	numeric_area_center_U,
	numeric_area_center_F,
	numeric_area_center_B,
])

examiner = Examiner([], [], locked_areas, dump_message = False)

def gen_examinations(n, i, j):
	if 0 == i and 0 == j:
		return []
	
	I = NumericIndex(i)
	J = NumericIndex(j)
	N = NumericIndex(n)

	X = Factor('X', 1)
	Y = Factor('Y', 1)
	Z = Factor('Z', 1)

	return [
		# on U face
		{
		(I,N,J) :
			((I,N,J), V_XYZ),
		(-J,N,I) :
			((-J,N,I), V_XYZ),
		(-I,N,-J) :
			((-I,N,-J), V_XYZ),
		(J,N,-I) :
			((J,N,-I), V_XYZ),
		},

		{
		(I,N,J):
			((I,N,J), V_XYZ),
		(-J,N,I):
			((-I,N,-J), (-Z,Y,X)),
		(-I,N,-J):
			((J,N,-I), (-Z,Y,X)),
		(J,N,-I):
			((-J,N,I), (-X,Y,-Z)),
		},

		{
		(I,N,J):
			((I,N,J), V_XYZ),
		(-J,N,I):
			((J,N,-I), (-X,Y,-Z)),
		(-I,N,-J):
			((-J,N,I), (Z,Y,-X)),
		(J,N,-I):
			((-I,N,-J), (Z,Y,-X)),
		},

		{
		(I,N,J):
			((-J,N,I), (-Z,Y,X)),
		(-J,N,I):
			((I,N,J), (Z,Y,-X)),
		(-I,N,-J):
			((J,N,-I), (-Z,Y,X)),
		(J,N,-I):
			((-I,N,-J), (Z,Y,-X)),
		},

		{
		(I,N,J):
			((-J,N,I), (-Z,Y,X)),
		(-J,N,I):
			((-I,N,-J), (-Z,Y,X)),
		(-I,N,-J):
			((I,N,J), (-X,Y,-Z)),
		(J,N,-I):
			((J,N,-I), V_XYZ),
		},

		{
		(I,N,J):
			((-J,N,I), (-Z,Y,X)),
		(-J,N,I):
			((J,N,-I), (-X,Y,-Z)),
		(-I,N,-J):
			((-I,N,-J), V_XYZ),
		(J,N,-I):
			((I,N,J), (-Z,Y,X)),
		},

		{
		(I,N,J):
			((-I,N,-J), (-X,Y,-Z)),
		(-J,N,I):
			((I,N,J), (Z,Y,-X)),
		(-I,N,-J):
			((-J,N,I), (Z,Y,-X)),
		(J,N,-I):
			((J,N,-I), V_XYZ),
		},

		{
		(I,N,J):
			((-I,N,-J), (-X,Y,-Z)),
		(-J,N,I):
			((-J,N,I), V_XYZ),
		(-I,N,-J):
			((J,N,-I), (-Z,Y,X)),
		(J,N,-I):
			((I,N,J), (-Z,Y,X)),
		},

		{
		(I,N,J):
			((-I,N,-J), (-X,Y,-Z)),
		(-J,N,I):
			((J,N,-I), (-X,Y,-Z)),
		(-I,N,-J):
			((I,N,J), (-X,Y,-Z)),
		(J,N,-I):
			((-J,N,I), (-X,Y,-Z)),
		},

		{
		(I,N,J):
			((J,N,-I), (Z,Y,-X)),
		(-J,N,I):
			((I,N,J), (Z,Y,-X)),
		(-I,N,-J):
			((-I,N,-J), V_XYZ),
		(J,N,-I):
			((-J,N,I), (-X,Y,-Z)),
		},

		{
		(I,N,J):
			((J,N,-I), (Z,Y,-X)),
		(-J,N,I):
			((-J,N,I), V_XYZ),
		(-I,N,-J):
			((I,N,J), (-X,Y,-Z)),
		(J,N,-I):
			((-I,N,-J), (Z,Y,-X)),
		},

		{
		(I,N,J):
			((J,N,-I), (Z,Y,-X)),
		(-J,N,I):
			((-I,N,-J), (-Z,Y,X)),
		(-I,N,-J):
			((-J,N,I), (Z,Y,-X)),
		(J,N,-I):
			((I,N,J), (-Z,Y,X)),
		},
	]

examinations_list = []
for i in range(0, n):
	for j in range(1, n):
		examinations_list += gen_examinations(n, i, j)

solver = CenterShiftSolver()

check_examine_solver(N, examinations_list, solver, examiner, [])