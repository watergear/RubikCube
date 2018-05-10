from ..base.index import *
from ..base.factor import *
from ..base.transform import *

class VectorAreas(list):
	def __init__(self, *args):
		list.__init__(self, *args)

	def is_contain(self, indexes, areafrom, areato, bound):
		in_area = True
		for i in range(len(indexes)):
			if '=' == bound[i]:
				if not indexes[i] == areafrom[i] and not areato[i] == indexes[i]:
					in_area = False
					break
			elif '()' == bound[i]:
				if indexes[i] <= areafrom[i] or areato[i] <= indexes[i]:
					in_area = False
					break
			elif '[]' == bound[i]:
				if indexes[i] < areafrom[i] or areato[i] < indexes[i]:
					in_area = False
					break
			else:
				in_area = False
				break
		return in_area

	def check(self, vfrom, vto):
		vfrom_indexes = vfrom[0]
		vto_indexes = vto[0]
		vfrom_directions = vfrom[1]
		vto_directions = vto[1]

		in_area = False
		pass_check = False

		for area in self:
			areafrom = area['from']
			areato = area['to']
			bound = area['bound']

			in_area = self.is_contain(vfrom_indexes, areafrom, areato, bound)

			if in_area:
				check_indexes_around = False
				if 'check_indexes' in area:
					check_indexes_around = 'around' == area['check_indexes']
				if check_indexes_around:
					pass_check = self.is_contain(vto_indexes, areafrom, areato, bound)
				else:
					pass_check = vfrom_indexes == vto_indexes

				check_directions = ''
				if 'check_directions' in area:
					check_directions = area['check_directions']
				if check_directions:
					if ( 'X' in check_directions ):
						pass_check = pass_check and vfrom_directions[0] == vto_directions[0]
					if ( 'Y' in check_directions ):
						pass_check = pass_check and vfrom_directions[1] == vto_directions[1]
					if ( 'Z' in check_directions ):
						pass_check = pass_check and vfrom_directions[2] == vto_directions[2]

				break

		return in_area, pass_check

def I(indexName):
	if '+' == indexName[0]:
		return Index(indexName[1:], 1)
	if '-' == indexName[0]:
		return Index(indexName[1:], -1)
	return Index(indexName, 1)

def T(factorName, indexName):
	factor = Factor(factorName[0], 1)
	clockwise = CW if not '-' == factorName[-1] else CCW
	index = I(indexName)
	return Transform(factor=factor, clockwise=clockwise, index=index)

def D(directName):
	factor = 1 if not '-' == directName[0] else -1
	return Factor(directName[-1], factor)

area_center_F = {
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('-n')),
		'bound'	:	(  '()' ,   '()' ,   '='  ),
	}

area_center_B =	{
		'from'	:	(I('-n'), I('-n'), I('+n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '()' ,   '()' ,   '='  ),
	}

area_center_L =	{
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('-n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '()' ,   '()' ),
	}

area_center_R =	{
		'from'	:	(I('+n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '()' ,   '()' ),
	}

area_center_U =	{
		'from'	:	(I('-n'), I('+n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '()' ,   '='  ,   '()' ),
	}

area_center_D =	{
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('-n'), I('+n')),
		'bound'	:	(  '()' ,   '='  ,   '()' ),
	}

area_edge_UB =	{
		'from'	:	(I('-n'), I('+n'), I('+n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '()' ,   '='  ,   '='  ),
	}

area_edge_UF =	{
		'from'	:	(I('-n'), I('+n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('-n')),
		'bound'	:	(  '()' ,   '='  ,   '='  ),
	}

area_edge_DB =	{
		'from'	:	(I('-n'), I('-n'), I('+n')),
		'to'	:	(I('+n'), I('-n'), I('+n')),
		'bound'	:	(  '()' ,   '='  ,   '='  ),
	}

area_edge_DF =	{
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('-n'), I('-n')),
		'bound'	:	(  '()' ,   '='  ,   '='  ),
	}

area_edge_RB =	{
		'from'	:	(I('+n'), I('-n'), I('+n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '()' ,   '='  ),
	}

area_edge_RF =	{
		'from'	:	(I('+n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('-n')),
		'bound'	:	(  '='  ,   '()' ,   '='  ),
	}

area_edge_LB =	{
		'from'	:	(I('-n'), I('-n'), I('+n')),
		'to'	:	(I('-n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '()' ,   '='  ),
	}

area_edge_LF =	{
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('-n'), I('+n'), I('-n')),
		'bound'	:	(  '='  ,   '()' ,   '='  ),
	}

area_edge_RU =	{
		'from'	:	(I('+n'), I('+n'), I('-n')),
		'to'	:	(I('+n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '='  ,   '()' ),
	}

area_edge_RD =	{
		'from'	:	(I('+n'), I('-n'), I('-n')),
		'to'	:	(I('+n'), I('-n'), I('+n')),
		'bound'	:	(  '='  ,   '='  ,   '()' ),
	}

area_edge_LU =	{
		'from'	:	(I('-n'), I('+n'), I('-n')),
		'to'	:	(I('-n'), I('+n'), I('+n')),
		'bound'	:	(  '='  ,   '='  ,   '()' ),
	}

area_edge_LD =	{
		'from'	:	(I('-n'), I('-n'), I('-n')),
		'to'	:	(I('-n'), I('-n'), I('+n')),
		'bound'	:	(  '='  ,   '='  ,   '()' ),
	}

area_center_U_around = area_center_U.copy()
area_center_U_around['check_indexes'] = 'around'
area_center_U_around['check_directions'] = 'Y'

area_center_F_around = area_center_F.copy()
area_center_F_around['check_indexes'] = 'around'
area_center_F_around['check_directions'] = 'Z'

area_center_B_around = area_center_B.copy()
area_center_B_around['check_indexes'] = 'around'
area_center_B_around['check_directions'] = 'Z'
