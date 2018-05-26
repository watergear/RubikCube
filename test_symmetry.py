from PyRubikCube.base.symbol import *

MirrorX			= SMT("||", 	"X")
MirrorY			= SMT("||", 	"Y")
MirrorZ			= SMT("||", 	"Z")

RotationX_2		= SMT("[]2",	"X")
RotationX_1		= SMT("[]",		"X")
RotationX_N1	= SMT("[]-",	"X")
RotationY_2		= SMT("[]2",	"Y")
RotationY_1		= SMT("[]",		"Y")
RotationY_N1	= SMT("[]-",	"Y")
RotationZ_2		= SMT("[]2",	"Z")
RotationZ_1		= SMT("[]",		"Z")
RotationZ_N1	= SMT("[]-",	"Z")

ObliqueX_1		= SMT(r"//", 	"X")
ObliqueX_N1		= SMT(r"\\", 	"X")
ObliqueY_1		= SMT(r"//", 	"Y")
ObliqueY_N1		= SMT(r"\\", 	"Y")
ObliqueZ_1		= SMT(r"//", 	"Z")
ObliqueZ_N1		= SMT(r"\\", 	"Z")


Transform_X_I	= T("X+", "i")
Transform_NX_I	= T("X-", "i")
Transform_Y_I	= T("Y+", "i")
Transform_NY_I	= T("Y-", "i")
Transform_Z_I	= T("Z+", "i")
Transform_NZ_I	= T("Z-", "i")
Transform_X_NI	= T("X+", "-i")
Transform_NX_NI	= T("X-", "-i")
Transform_Y_NI	= T("Y+", "-i")
Transform_NY_NI	= T("Y-", "-i")
Transform_Z_NI	= T("Z+", "-i")
Transform_NZ_NI	= T("Z-", "-i")


no_pass = 0;
def check_smt(smt, t, t_check):
	global no_pass
	cjg_t = smt.conjugate_transform(t)
	print("Symmetry: ", smt)
	print("Transform: ", t)
	print("Conjugated Transform: ", cjg_t)
	if ( cjg_t == t_check ):
		print("Pass!")
	else:
		print("No pass!")
		no_pass += 1
	print()

check_smt(MirrorX, Transform_X_I, Transform_X_NI)
check_smt(MirrorX, Transform_Y_I, Transform_NY_I)
check_smt(MirrorX, Transform_Z_I, Transform_NZ_I)

check_smt(MirrorY, Transform_X_I, Transform_NX_I)
check_smt(MirrorY, Transform_Y_I, Transform_Y_NI)
check_smt(MirrorY, Transform_Z_I, Transform_NZ_I)

check_smt(MirrorZ, Transform_X_I, Transform_NX_I)
check_smt(MirrorZ, Transform_Y_I, Transform_NY_I)
check_smt(MirrorZ, Transform_Z_I, Transform_Z_NI)

check_smt(RotationX_2, Transform_X_I, Transform_X_I)
check_smt(RotationX_2, Transform_Y_I, Transform_NY_NI)
check_smt(RotationX_2, Transform_Z_I, Transform_NZ_NI)

check_smt(RotationY_2, Transform_X_I, Transform_NX_NI)
check_smt(RotationY_2, Transform_Y_I, Transform_Y_I)
check_smt(RotationY_2, Transform_Z_I, Transform_NZ_NI)

check_smt(RotationZ_2, Transform_X_I, Transform_NX_NI)
check_smt(RotationZ_2, Transform_Y_I, Transform_NY_NI)
check_smt(RotationZ_2, Transform_Z_I, Transform_Z_I)

check_smt(RotationX_1, Transform_X_I, Transform_X_I)
check_smt(RotationX_1, Transform_Y_I, Transform_NZ_NI)
check_smt(RotationX_1, Transform_Z_I, Transform_Y_I)

check_smt(RotationX_N1, Transform_X_I, Transform_X_I)
check_smt(RotationX_N1, Transform_Y_I, Transform_Z_I)
check_smt(RotationX_N1, Transform_Z_I, Transform_NY_NI)

check_smt(RotationY_1, Transform_X_I, Transform_Z_I)
check_smt(RotationY_1, Transform_Y_I, Transform_Y_I)
check_smt(RotationY_1, Transform_Z_I, Transform_NX_NI)

check_smt(RotationY_N1, Transform_X_I, Transform_NZ_NI)
check_smt(RotationY_N1, Transform_Y_I, Transform_Y_I)
check_smt(RotationY_N1, Transform_Z_I, Transform_X_I)

check_smt(RotationZ_1, Transform_X_I, Transform_NY_NI)
check_smt(RotationZ_1, Transform_Y_I, Transform_X_I)
check_smt(RotationZ_1, Transform_Z_I, Transform_Z_I)

check_smt(RotationZ_N1, Transform_X_I, Transform_Y_I)
check_smt(RotationZ_N1, Transform_Y_I, Transform_NX_NI)
check_smt(RotationZ_N1, Transform_Z_I, Transform_Z_I)

check_smt(ObliqueX_1, Transform_X_I, Transform_NX_I)
check_smt(ObliqueX_1, Transform_Y_I, Transform_NZ_I)
check_smt(ObliqueX_1, Transform_Z_I, Transform_NY_I)

check_smt(ObliqueX_N1, Transform_X_I, Transform_NX_I)
check_smt(ObliqueX_N1, Transform_Y_I, Transform_Z_NI)
check_smt(ObliqueX_N1, Transform_Z_I, Transform_Y_NI)

check_smt(ObliqueY_1, Transform_X_I, Transform_NZ_I)
check_smt(ObliqueY_1, Transform_Y_I, Transform_NY_I)
check_smt(ObliqueY_1, Transform_Z_I, Transform_NX_I)

check_smt(ObliqueY_N1, Transform_X_I, Transform_Z_NI)
check_smt(ObliqueY_N1, Transform_Y_I, Transform_NY_I)
check_smt(ObliqueY_N1, Transform_Z_I, Transform_X_NI)

check_smt(ObliqueZ_1, Transform_X_I, Transform_NY_I)
check_smt(ObliqueZ_1, Transform_Y_I, Transform_NX_I)
check_smt(ObliqueZ_1, Transform_Z_I, Transform_NZ_I)

check_smt(ObliqueZ_N1, Transform_X_I, Transform_Y_NI)
check_smt(ObliqueZ_N1, Transform_Y_I, Transform_X_NI)
check_smt(ObliqueZ_N1, Transform_Z_I, Transform_NZ_I)

if ( no_pass > 0 ):
	print("No pass: ", no_pass)

# symmetry_list = [
# 	MirrorX,
# 	MirrorY,
# 	MirrorZ,
# 	RotationX_2,
# 	RotationX_1,
# 	RotationX_N1,
# 	RotationY_2,
# 	RotationY_1,
# 	RotationY_N1,
# 	RotationZ_2,
# 	RotationZ_1,
# 	RotationZ_N1,
# 	ObliqueX_1,
# 	ObliqueX_N1,
# 	ObliqueY_1,
# 	ObliqueY_N1,
# 	ObliqueZ_1,
# 	ObliqueZ_N1,
# ]
# transform_list = [
# 	Transform_X_I,
# 	Transform_NX_I,
# 	Transform_Y_I,
# 	Transform_NY_I,
# 	Transform_Z_I,
# 	Transform_NZ_I,
# 	Transform_X_NI,
# 	Transform_NX_NI,
# 	Transform_Y_NI,
# 	Transform_NY_NI,
# 	Transform_Z_NI,
# 	Transform_NZ_NI,
# ]
# for smt in symmetry_list:
# 	for t in transform_list:
# 		print("Symmetry: ", smt)
# 		print("Transform: ", t)
# 		print("Conjugated Transform: ", smt.conjugate_transform(t))
# 		print()
