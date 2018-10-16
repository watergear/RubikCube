if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.examine.transform import *

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
	(W('n', 'n', '-n'),		V('X', 'Y', 'Z')),
	(W('-n', 'n', '-n'),	V('X', 'Y', 'Z')),

	# c shall be empty set
	(W('c', 'n', 'n'),		V('X', 'Y', 'Z')),
	(W('c', 'n', '-n'),		V('X', 'Y', 'Z')),
]
dest_vectors = [
	(W('-n', 'n', '-n'),	V('Z', 'Y', '-X')),
	(W('n', 'n', '-n'),		V('-Z', 'Y', 'X')),

	# c shall be empty set
	(W('-c', 'n', '-n'),	V('-X', 'Y', '-Z')),
	(W('-c', 'n', 'n'),		V('-X', 'Y', '-Z')),
]

locked_areas = Areas([
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
	area_corner_LDF,
	area_corner_LDB,
	area_corner_LUF,
	area_corner_LUB,
	area_corner_RDF,
	area_corner_RDB,
	area_corner_RUF,
	area_corner_RUB,
])

examiner = Examiner(src_vectors, dest_vectors, locked_areas, dump_message = True)
ok = examiner.test(gen_transform_state(corner_transpose_I, otherwise=True))
print("total same:", examiner.same_count)
print("total shift:", examiner.shift_count)
print("total error:", examiner.error_count)
print("ok:", bool(ok))
