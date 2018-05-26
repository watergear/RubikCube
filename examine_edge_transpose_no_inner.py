﻿from PyRubikCube.base.symbol import *
from PyRubikCube.base.state import gen_transform_state
from PyRubikCube.examine.area import *
from PyRubikCube.examine.examine import Examiner

edge_transpose_I = [
	T("Y+", "I"),
	T("Y+", "I"),
	T("Y+", "-I'"),
	T("Y+", "-I'"),
	T("X+", "I"),
	T("X+", "I"),
	T("Y+", "-I'"),
	T("Y+", "-I'"),
	T("Y+", "I"),
	T("Y+", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "I"),
	T("X+", "I"),
	T("Y+", "n"),
	T("Y+", "n"),
	T("X+", "I"),
	T("X+", "I"),
]

src_vectors = [
	(W('I', 'n', 'n'),		V('X', 'Y', 'Z')),
	(W('-I', 'n', 'n'),		V('X', 'Y', 'Z')),
	(W('I', 'n', '-n'),		V('X', 'Y', 'Z')),
	(W('-I', 'n', '-n'),	V('X', 'Y', 'Z')),

	# c shall be empty set
	(W('I', 'c', 'n'),		V('X', 'Y', 'Z')),
	(W('I', 'c', '-n'),		V('X', 'Y', 'Z')),
]
dest_vectors = [
	(W('-I', 'n', '-n'),	V('-X', 'Y', '-Z')),
	(W('I', 'n', '-n'),		V('-X', 'Y', '-Z')),
	(W('-I', 'n', 'n'),		V('-X', 'Y', '-Z')),
	(W('I', 'n', 'n'),		V('-X', 'Y', '-Z')),

	# c shall be empty set
	(W('I', '-c', '-n'),	V('X', '-Y', '-Z')),
	(W('I', '-c', 'n'),		V('X', '-Y', '-Z')),
]

locked_areas = Areas([
	# area_inner, # no match
	area_center_F_around,
	area_center_B_around,
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

examiner = Examiner(src_vectors, dest_vectors, locked_areas, dump_message = True)
ok = examiner.test(gen_transform_state(edge_transpose_I, otherwise=True))
print("total same:", examiner.same_count)
print("total shift:", examiner.shift_count)
print("total error:", examiner.error_count)
print("ok:", bool(ok))
