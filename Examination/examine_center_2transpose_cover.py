if __name__ == "__main__":
	import init

from PyRubikCube.base.symbol import *
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import *
from PyRubikCube.examine.transform import *

center_i_j = [
	T("Y-", "n"),
	T("X-", "i"),
	T("X-", "j"),
	T("Y-", "n"),
	T("X+", "j"),
	T("Y+", "n"),
	T("X+", "i"),
	T("Y-", "n"),
	T("X-", "j"),
	T("Y+", "n"),
	T("X+", "j"),
]

src_vectors = [
	(W('i', 'n', 'j'),	V('X', 'Y', 'Z')),
	(W('i', 'j', '-n'),	V('X', 'Y', 'Z')),
]
dest_vectors = [
	(W('i', 'j', '-n'),	V('X', 'Z', '-Y')),
	(W('i', 'n', 'j'),	V('X', '-Z', 'Y')),
]

locked_areas = Areas([
	area_inner,
	area_center_F,
	area_center_B,
	area_center_L,
	area_center_R,
	area_center_D,
	area_center_U_around,
])

examiner = Examiner(src_vectors, dest_vectors, locked_areas, dump_message = True)
ok = examiner.test(gen_transform_state(center_i_j))
print("total same:", examiner.same_count)
print("total shift:", examiner.shift_count)
print("total error:", examiner.error_count)
print("ok:", bool(ok))
