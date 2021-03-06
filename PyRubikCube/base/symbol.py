from .index import Index,NoneIndex,NumericIndex
from .factor import Factor
from .transform import Transform,CW,CCW
from .symmetry import Symmetry,mapSymmetrySymbol

def I(indexName = None):
	if indexName is None:
		return NoneIndex()

	if type(indexName) == int:
		return NumericIndex(indexName)

	if '+' == indexName[0]:
		return Index(indexName[1:], 1)
	if '-' == indexName[0]:
		return Index(indexName[1:], -1)
	return Index(indexName, 1)

def F(factorName):
	sign = 1 if not '-' == factorName[0] else -1
	return Factor(factorName[-1], sign)

def T(factorName, indexName = None):
	factor = Factor(factorName[0], 1)
	clockwise = CW if not '-' == factorName[-1] else CCW
	index = I(indexName)
	return Transform(factor=factor, clockwise=clockwise, index=index)

def W(x, y, z):
	return (I(x), I(y), I(z))
def V(x, y, z):
	return (F(x), F(y), F(z))

V_XYZ = V('X','Y','Z')

def SMT(modeName, factorName):
	try:
		mode, ratio = mapSymmetrySymbol[modeName]
	except KeyError:
		pass
	factor = Factor(factorName, 1)
	return Symmetry(mode, factor, ratio)

SMT_E	= SMT("==","")

SMT_MX	= SMT("||",  "X")
SMT_MY	= SMT("||",  "Y")
SMT_MZ	= SMT("||",  "Z")

SMT_RX	= SMT("[]",  "X")
SMT_RNX	= SMT("[]-", "X")
SMT_R2X	= SMT("[]2", "X")
SMT_RY	= SMT("[]",  "Y")
SMT_RNY	= SMT("[]-", "Y")
SMT_R2Y	= SMT("[]2", "Y")
SMT_RZ	= SMT("[]",  "Z")
SMT_RNZ	= SMT("[]-", "Z")
SMT_R2Z	= SMT("[]2", "Z")

SMT_OX	= SMT(r"//", "X")
SMT_ONX	= SMT(r"\\", "X")
SMT_OY	= SMT(r"//", "Y")
SMT_ONY	= SMT(r"\\", "Y")
SMT_OZ	= SMT(r"//", "Z")
SMT_ONZ	= SMT(r"\\", "Z")
