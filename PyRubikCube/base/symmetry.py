from .factor import reFactor
from .transform import *

Mirror = "Mirror"
Rotation = "Rotation"
Oblique = "Oblique"

Ratio_1 = 1
Ratio_2 = 2
Ratio_N1 = -1

RefX 	= \
	(	(-1, 0, 0),
		(0, 1, 0),
		(0, 0, 1)
	)
RefX_ = RefX

RefY 	= \
	(	(1, 0, 0),
		(0, -1, 0),
		(0, 0, 1)
	)
RefY_ = RefY

RefZ 	= \
	(	(1, 0, 0),
		(0, 1, 0),
		(0, 0, -1)
	)
RefZ_ = RefZ

Rotation2X 	= \
	(	(1, 0, 0),
		(0, -1, 0),
		(0, 0, -1)
	)
Rotation2X_ = Rotation2X

Rotation2Y 	= \
	(	(-1, 0, 0),
		(0, 1, 0),
		(0, 0, -1)
	)
Rotation2Y_ = Rotation2Y

Rotation2Z 	= \
	(	(-1, 0, 0),
		(0, -1, 0),
		(0, 0, 1)
	)
Rotation2Z_ = Rotation2Z

ObliqueRefX 	= \
	(	(1, 0, 0),
		(0, 0, 1),
		(0, 1, 0)
	)
ObliqueRefX_ = ObliqueRefX

NegObliqueRefX 	= \
	(	(1, 0, 0),
		(0, 0, -1),
		(0, -1, 0)
	)
NegObliqueRefX_ = NegObliqueRefX

ObliqueRefY 	= \
	(	(0, 0, 1),
		(0, 1, 0),
		(1, 0, 0)
	)
ObliqueRefY_ = ObliqueRefY

NegObliqueRefY 	= \
	(	(0, 0, -1),
		(0, 1, 0),
		(-1, 0, 0)
	)
NegObliqueRefY_ = NegObliqueRefY

ObliqueRefZ 	= \
	(	(0, 1, 0),
		(1, 0, 0),
		(0, 0, 1)
	)
ObliqueRefZ_ = ObliqueRefZ

NegObliqueRefZ 	= \
	(	(0, -1, 0),
		(-1, 0, 0),
		(0, 0, 1)
	)
NegObliqueRefZ_ = NegObliqueRefZ

mapSymmetryMat = {
	(Mirror, factorX, Ratio_1):		RefX,
	(Mirror, factorY, Ratio_1):		RefY,
	(Mirror, factorZ, Ratio_1):		RefZ,

	(Rotation, factorX, Ratio_1):	RotationX,
	(Rotation, factorX, Ratio_N1):	RotationX_,
	(Rotation, factorX, Ratio_2):	Rotation2X,
	(Rotation, factorY, Ratio_1):	RotationY,
	(Rotation, factorY, Ratio_N1):	RotationY_,
	(Rotation, factorY, Ratio_2):	Rotation2Y,
	(Rotation, factorZ, Ratio_1):	RotationZ,
	(Rotation, factorZ, Ratio_N1):	RotationZ_,
	(Rotation, factorZ, Ratio_2):	Rotation2Z,

	(Oblique, factorX, Ratio_1):	ObliqueRefX,
	(Oblique, factorX, Ratio_N1):	NegObliqueRefX,
	(Oblique, factorY, Ratio_1):	ObliqueRefY,
	(Oblique, factorY, Ratio_N1):	NegObliqueRefY,
	(Oblique, factorZ, Ratio_1):	ObliqueRefZ,
	(Oblique, factorZ, Ratio_N1):	NegObliqueRefZ,
}

mapInverseMat = {
	RefX		:		RefX,
	RefY		:		RefY,
	RefZ		:		RefZ,
	RotationX	:		RotationX_,
	RotationX_	:		RotationX,
	Rotation2X	:		Rotation2X,
	RotationY	:		RotationY_,
	RotationY_	:		RotationY,
	Rotation2Y	:		Rotation2Y,
	RotationZ	:		RotationZ_,
	RotationZ_	:		RotationZ,
	Rotation2Z	:		Rotation2Z,
	ObliqueRefX	:		ObliqueRefX,
	NegObliqueRefX	:	NegObliqueRefX,
	ObliqueRefY	:		ObliqueRefY,
	NegObliqueRefY	:	NegObliqueRefY,
	ObliqueRefZ	:		ObliqueRefZ,
	NegObliqueRefZ	:	NegObliqueRefZ,
}

SMT_XYZ 	= \
	(	(1, 0, 0),
		(0, 1, 0),
		(0, 0, 1)
	)

SMT_XZY 	= \
	(	(1, 0, 0),
		(0, 0, 1),
		(0, 1, 0)
	)

SMT_ZYX 	= \
	(	(0, 0, 1),
		(0, 1, 0),
		(1, 0, 0)
	)

SMT_YXZ 	= \
	(	(0, 1, 0),
		(1, 0, 0),
		(0, 0, 1)
	)

SMT_V_1_1_1 	= \
	(1,1,1)

SMT_V_1_1_N1 	= \
	(1,1,-1)

SMT_V_1_N1_1 	= \
	(1,-1,1)

SMT_V_1_N1_N1 	= \
	(1,-1,-1)

SMT_V_N1_1_1 	= \
	(-1,1,1)

SMT_V_N1_1_N1 	= \
	(-1,1,-1)

SMT_V_N1_N1_1 	= \
	(-1,-1,1)

SMT_V_N1_N1_N1	= \
	(-1,-1,-1)

# map { (mode, factor, ratio): (factor, clockwise, index) }
mapSymmetryTransformMats = {
	(Mirror, factorX, Ratio_1):
		(SMT_XYZ,	SMT_V_1_N1_N1,	SMT_V_N1_1_1),
	(Mirror, factorY, Ratio_1):
		(SMT_XYZ,	SMT_V_N1_1_N1,	SMT_V_1_N1_1),
	(Mirror, factorZ, Ratio_1):
		(SMT_XYZ,	SMT_V_N1_N1_1,	SMT_V_1_1_N1),

	(Rotation, factorX, Ratio_1):
		(SMT_XZY,	SMT_V_1_N1_1,	SMT_V_1_N1_1),
	(Rotation, factorX, Ratio_N1):
		(SMT_XZY,	SMT_V_1_1_N1,	SMT_V_1_1_N1),
	(Rotation, factorX, Ratio_2):
		(SMT_XYZ,	SMT_V_1_N1_N1,	SMT_V_1_N1_N1),
	(Rotation, factorY, Ratio_1):
		(SMT_ZYX,	SMT_V_1_1_N1,	SMT_V_1_1_N1),
	(Rotation, factorY, Ratio_N1):
		(SMT_ZYX,	SMT_V_N1_1_1,	SMT_V_N1_1_1),
	(Rotation, factorY, Ratio_2):
		(SMT_XYZ,	SMT_V_N1_1_N1,	SMT_V_N1_1_N1),
	(Rotation, factorZ, Ratio_1):
		(SMT_YXZ,	SMT_V_N1_1_1,	SMT_V_N1_1_1),
	(Rotation, factorZ, Ratio_N1):
		(SMT_YXZ,	SMT_V_1_N1_1,	SMT_V_1_N1_1),
	(Rotation, factorZ, Ratio_2):
		(SMT_XYZ,	SMT_V_N1_N1_1,	SMT_V_N1_N1_1),

	(Oblique, factorX, Ratio_1):
		(SMT_XZY,	SMT_V_N1_N1_N1,	SMT_V_1_1_1),
	(Oblique, factorX, Ratio_N1):
		(SMT_XZY,	SMT_V_N1_1_1,	SMT_V_1_N1_N1),
	(Oblique, factorY, Ratio_1):
		(SMT_ZYX,	SMT_V_N1_N1_N1,	SMT_V_1_1_1),
	(Oblique, factorY, Ratio_N1):
		(SMT_ZYX,	SMT_V_1_N1_1,	SMT_V_N1_1_N1),
	(Oblique, factorZ, Ratio_1):
		(SMT_YXZ,	SMT_V_N1_N1_N1,	SMT_V_1_1_1),
	(Oblique, factorZ, Ratio_N1):
		(SMT_YXZ,	SMT_V_1_1_N1,	SMT_V_N1_N1_1),
}

mapSymmetrySymbol = {
	"||" 		: (Mirror, Ratio_1),
	r"//" 		: (Oblique, Ratio_1),
	r"\\" 		: (Oblique, Ratio_N1),
	"[]" 		: (Rotation, Ratio_1),
	"[]-" 		: (Rotation, Ratio_N1),
	"[]2" 		: (Rotation, Ratio_2),
}

class Symmetry:
	def __init__(self, mode, factor, ratio = 1):
		self.mode = mode
		self.factor = factor
		self.ratio = ratio
		try:
			key = (mode, factor, ratio)
			self.matrix = mapSymmetryMat[key]
			self.matT_factor, self.vecT_clockwise, self.vecT_index = \
				mapSymmetryTransformMats[key]
		except KeyError:
			pass

	def __repr__(self):
		for symbol in mapSymmetrySymbol:
			if ( mapSymmetrySymbol[symbol] == (self.mode, self.ratio) ):
				return symbol + repr(self.factor)
		raise ValueError
		return "Invalid Symmetry!"

	def conjugate_transform(self, t):
		tuple_factor = mat_mul([t.factor], self.matT_factor)[0]
		factor = reFactor(tuple_factor)

		v_clockwise = [t.clockwise*f for f in t.factor]
		clockwise = vec_mul(v_clockwise, self.vecT_clockwise)

		v_index = [t.index*f for f in t.factor]
		index = vec_mul(v_index, self.vecT_index)

		return Transform(factor, clockwise, index)

	def conjugate(self, v):
		return mat_mul(v, self.matrix)

	def inverse_conjugate(self, v):
		return mat_mul(v, mapInverseMat[self.matrix])

	def conjugate_matrix(self, mm):
		mm2 = mapInverseMat[self.matrix]
		mm2 = mat_mul(mm2, mm)
		mm2 = mat_mul(mm2, self.matrix)
		return mm2