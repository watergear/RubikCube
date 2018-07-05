from PyRubikCube.base.symbol import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.solve.problem import *
from PyRubikCube.solve.lastlayer_corner import *

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

no_pass = 0;
def examine_solution(examiner, WV_map):
	global no_pass
	global N, n, odd
	#global examiner

	problem = Problem(N)
	for w in WV_map:
		problem.state.locations_map[w] = WV_map[w][0]
		problem.state.orientations_map[w] = WV_map[w][1]

	s = LastLayerCornerSolution(problem)
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

# need to turn off step4
for e in examinations_list_step1:
	print(e)
	examine_solution(examiner1, e)

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

# need to turn off step3, step4
for e in examinations_list_step2:
	print(e)
	examine_solution(examiner2, e)

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

for e in examinations_list_step3:
	print(e)
	examine_solution(examiner3, e)

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

# need to turn off step4
for e in examinations_list_step3_even:
	print(e)
	examine_solution(examiner3_even, e)

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

# test step4 only
for e in examinations_list_step4:
	print(e)
	examine_solution(examiner4, e)

if ( no_pass > 0 ):
	print("No pass:", no_pass)
