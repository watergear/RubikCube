from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import Examine
from PyRubikCube.base.state import gen_state

corner_transpose_I = [
	T("X+", "n"),
	T("Z-", "-n"),
	T("Y-", "n"),
	T("Z+", "-n"),
	T("Y+", "n"),
	T("Z-", "-n"),
	T("Y+", "n"),
	T("Z+", "-n"),
	T("Z+", "-n"),
	T("X-", "n"),
	T("Z-", "-n"),
	T("Y+", "n"),
	T("Z-", "-n"),
	T("Y-", "n"),
	T("Z+", "-n"),

	# edge 3 transpose reverse
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "I"),

	# edge 3 transpose mirror X
	T("X+", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "-I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X-", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
]

src_vectors = [
	((I('n'), I('n'), I('-n')),		(D('X'), D('Y'), D('Z'))),
	((I('-n'), I('n'), I('-n')),	(D('X'), D('Y'), D('Z'))),

	# c shall be empty set
	((I('c'), I('n'), I('n')),		(D('X'), D('Y'), D('Z'))),
	((I('c'), I('n'), I('-n')),		(D('X'), D('Y'), D('Z'))),
]
dest_vectors = [
	((I('-n'), I('n'), I('-n')),	(D('Z'), D('Y'), D('-X'))),
	((I('n'), I('n'), I('-n')),		(D('-Z'), D('Y'), D('X'))),

	# c shall be empty set
	((I('-c'), I('n'), I('-n')),	(D('-X'), D('Y'), D('-Z'))),
	((I('-c'), I('n'), I('n')),		(D('-X'), D('Y'), D('-Z'))),
]

locked_areas = VectorAreas([
	area_inner,
	area_center_F,
	area_center_B,
	area_center_L,
	area_center_R,
	area_center_D,
	area_center_U_around,
	area_edge_UB,
	area_edge_UF,
	area_edge_DB,
	area_edge_DF,
	area_edge_RB,
	area_edge_RF,
	area_edge_LB,
	area_edge_LF,
	area_edge_RU,
	area_edge_RD,
	area_edge_LU,
	area_edge_LD,
])

examine = Examine(src_vectors, dest_vectors, locked_areas, dump_message = True)
ok = examine.test(gen_state(corner_transpose_I, otherwise=True))
print("total same:", examine.same_count)
print("total shift:", examine.shift_count)
print("total error:", examine.error_count)
print("ok:", bool(ok))
