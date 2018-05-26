from .index import Index,NumericIndex
from .factor import Factor
from .transform import Transform,CW,CCW
from .symmetry import Symmetry,mapSymmetrySymbol

def I(indexName):
	if ( type(indexName) == int ):
		return NumericIndex(indexName)

	if '+' == indexName[0]:
		return Index(indexName[1:], 1)
	if '-' == indexName[0]:
		return Index(indexName[1:], -1)
	return Index(indexName, 1)

def F(factorName):
	sign = 1 if not '-' == factorName[0] else -1
	return Factor(factorName[-1], sign)

def T(factorName, indexName):
	factor = Factor(factorName[0], 1)
	clockwise = CW if not '-' == factorName[-1] else CCW
	index = I(indexName)
	return Transform(factor=factor, clockwise=clockwise, index=index)

def W(x, y, z):
	return (I(x), I(y), I(z))
def V(x, y, z):
	return (F(x), F(y), F(z))

def SMT(modeName, factorName):
	try:
		mode, ratio = mapSymmetrySymbol[modeName]
	except KeyError:
		pass
	factor = Factor(factorName, 1)
	return Symmetry(mode, factor, ratio)

