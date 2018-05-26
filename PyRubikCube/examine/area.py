from ..base.symbol import *

class Areas(list):
	def __init__(self, *args):
		list.__init__(self, *args)

	def is_contain(self, indexes, areafrom, areato, bound):
		in_area = True
		for i in range(len(indexes)):
			if '==' == bound[i]:
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
		vfrom_position = vfrom[0]
		vto_position = vto[0]
		vfrom_orientation = vfrom[1]
		vto_orientation = vto[1]

		in_area = False
		pass_check = False

		for area in self:
			areafrom = area['from']
			areato = area['to']
			bound = area['bound']

			in_area = self.is_contain(vfrom_position, areafrom, areato, bound)

			if in_area:
				check_position_around = False
				if 'check_position' in area:
					check_position_around = 'around' == area['check_position']
				if check_position_around:
					pass_check = self.is_contain(vto_position, areafrom, areato, bound)
				else:
					pass_check = vfrom_position == vto_position

				check_orientation = ''
				if 'check_orientation' in area:
					check_orientation = area['check_orientation']
				if check_orientation:
					if ( 'X' in check_orientation ):
						pass_check = pass_check and vfrom_orientation[0] == vto_orientation[0]
					if ( 'Y' in check_orientation ):
						pass_check = pass_check and vfrom_orientation[1] == vto_orientation[1]
					if ( 'Z' in check_orientation ):
						pass_check = pass_check and vfrom_orientation[2] == vto_orientation[2]
				else:
					pass_check = pass_check and vfrom_orientation == vto_orientation

				break

		return in_area, pass_check

class AreaFactory():
	def __init__(self, n):
		self.indexN = I(n)
		self.indexN_ = -(self.indexN)


	def all(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '[]', '[]', '[]' ),
		}

	def inner(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '()', '()', '()' ),
		}

	def center_L(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n_ ,  n  ,  n   ),
			'bound'	:	( '==', '()', '()' ),
		}

	def center_R(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '==', '()', '()' ),
		}

	def center_D(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n_ ,  n   ),
			'bound'	:	( '()', '==', '()' ),
		}

	def center_U(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n_  ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '()', '==', '()' ),
		}

	def center_F(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n  ,  n_  ),
			'bound'	:	( '()', '()', '==' ),
		}

	def center_B(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n   ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '()', '()', '==' ),
		}

	def edge_UB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n   ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '()', '==', '==' ),
		}

	def edge_UF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n_  ),
			'to'	:	(  n  ,  n  ,  n_  ),
			'bound'	:	( '()', '==', '==' ),
		}

	def edge_DB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n   ),
			'to'	:	(  n  ,  n_ ,  n   ),
			'bound'	:	( '()', '==', '==' ),
		}

	def edge_DF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n_ ,  n_  ),
			'bound'	:	( '()', '==', '==' ),
		}

	def edge_RB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n   ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '==', '()', '==' ),
		}

	def edge_RF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n  ,  n_  ),
			'bound'	:	( '==', '()', '==' ),
		}

	def edge_LB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n   ),
			'to'	:	(  n_ ,  n  ,  n   ),
			'bound'	:	( '==', '()', '==' ),
		}

	def edge_LF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n_ ,  n  ,  n_  ),
			'bound'	:	( '==', '()', '==' ),
		}

	def edge_RU(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n  ,  n_  ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '==', '==', '()' ),
		}

	def edge_RD(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n_ ,  n   ),
			'bound'	:	( '==', '==', '()' ),
		}

	def edge_LU(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n_  ),
			'to'	:	(  n_ ,  n  ,  n   ),
			'bound'	:	( '==', '==', '()' ),
		}

	def edge_LD(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n_ ,  n_ ,  n   ),
			'bound'	:	( '==', '==', '()' ),
		}

	def corner_LDF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n_  ),
			'to'	:	(  n_ ,  n_ ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_LDB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n_ ,  n   ),
			'to'	:	(  n_ ,  n_ ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_LUF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n_  ),
			'to'	:	(  n_ ,  n  ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_LUB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n_ ,  n  ,  n   ),
			'to'	:	(  n_ ,  n  ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_RDF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n_  ),
			'to'	:	(  n  ,  n_ ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_RDB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n_ ,  n   ),
			'to'	:	(  n  ,  n_ ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_RUF(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n  ,  n_  ),
			'to'	:	(  n  ,  n  ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def corner_RUB(self):
		n = self.indexN
		n_ = self.indexN_
		return {
			'from'	:	(  n  ,  n  ,  n   ),
			'to'	:	(  n  ,  n  ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_L_around(self):
		center_L_around = self.center_L()
		center_L_around['check_position'] = 'around'
		center_L_around['check_orientation'] = 'X'
		return center_L_around
	
	def center_R_around(self):
		center_R_around = self.center_R()
		center_R_around['check_position'] = 'around'
		center_R_around['check_orientation'] = 'X'
		return center_R_around

	def center_D_around(self):
		center_D_around = self.center_D()
		center_D_around['check_position'] = 'around'
		center_D_around['check_orientation'] = 'Y'
		return center_D_around

	def center_U_around(self):
		center_U_around = self.center_U()
		center_U_around['check_position'] = 'around'
		center_U_around['check_orientation'] = 'Y'
		return center_U_around
	
	def center_F_around(self):
		center_F_around = self.center_F()
		center_F_around['check_position'] = 'around'
		center_F_around['check_orientation'] = 'Z'
		return center_F_around

	def center_B_around(self):
		center_B_around = self.center_B()
		center_B_around['check_position'] = 'around'
		center_B_around['check_orientation'] = 'Z'
		return center_B_around


area_factory = AreaFactory('n')
area_all 		= 	area_factory.all()
area_inner 		= 	area_factory.inner()
area_center_L 	= 	area_factory.center_L()
area_center_R 	= 	area_factory.center_R()
area_center_D 	= 	area_factory.center_D()
area_center_U 	= 	area_factory.center_U()
area_center_F 	= 	area_factory.center_F()
area_center_B 	= 	area_factory.center_B()
area_edge_UB 	= 	area_factory.edge_UB()
area_edge_UF 	= 	area_factory.edge_UF()
area_edge_DB 	= 	area_factory.edge_DB()
area_edge_DF 	= 	area_factory.edge_DF()
area_edge_RB 	= 	area_factory.edge_RB()
area_edge_RF 	= 	area_factory.edge_RF()
area_edge_LB 	= 	area_factory.edge_LB()
area_edge_LF 	= 	area_factory.edge_LF()
area_edge_RU 	= 	area_factory.edge_RU()
area_edge_RD 	= 	area_factory.edge_RD()
area_edge_LU 	= 	area_factory.edge_LU()
area_edge_LD 	= 	area_factory.edge_LD()
area_center_L_around	=	area_factory.center_L_around()
area_center_R_around	=	area_factory.center_R_around()
area_center_D_around	=	area_factory.center_D_around()
area_center_U_around	=	area_factory.center_U_around()
area_center_F_around	=	area_factory.center_F_around()
area_center_B_around	=	area_factory.center_B_around()
area_corner_LDF	=	area_factory.corner_LDF()
area_corner_LDB	=	area_factory.corner_LDB()
area_corner_LUF	=	area_factory.corner_LUF()
area_corner_LUB	=	area_factory.corner_LUB()
area_corner_RDF	=	area_factory.corner_RDF()
area_corner_RDB	=	area_factory.corner_RDB()
area_corner_RUF	=	area_factory.corner_RUF()
area_corner_RUB	=	area_factory.corner_RUB()


class NumericAreaFactory(AreaFactory):
	def __init__(self, n, odd=True):
		AreaFactory.__init__(self, n)
		self.index0 = I(0)
		self.odd = odd

	def core_midpoint(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  i0 ,  i0  ),
			'to'	:	(  i0 ,  i0 ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_L(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n_ ,  i0 ,  i0  ),
			'to'	:	(  n_ ,  i0 ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_R(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n ,  i0 ,  i0  ),
			'to'	:	(  n ,  i0 ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_D(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n_ ,  i0  ),
			'to'	:	(  i0 ,  n_ ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_U(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n ,  i0  ),
			'to'	:	(  i0 ,  n ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_F(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  i0 ,  n_  ),
			'to'	:	(  i0 ,  i0 ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def center_midpoint_B(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  i0 ,  n  ),
			'to'	:	(  i0 ,  i0 ,  n  ),
			'bound'	:	( '==', '==', '==' ),
		}

	def edge_midpoint_UB(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n  ,  n   ),
			'to'	:	(  i0 ,  n  ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_UF(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n  ,  n_  ),
			'to'	:	(  i0 ,  n  ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_DB(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n_ ,  n   ),
			'to'	:	(  i0 ,  n_ ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_DF(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  i0 ,  n_ ,  n_  ),
			'to'	:	(  i0 ,  n_ ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_RB(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n  ,  i0 ,  n   ),
			'to'	:	(  n  ,  i0 ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_RF(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n  ,  i0 ,  n_  ),
			'to'	:	(  n  ,  i0 ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_LB(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n_ ,  i0 ,  n   ),
			'to'	:	(  n_ ,  i0 ,  n   ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_LF(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n_ ,  i0 ,  n_  ),
			'to'	:	(  n_ ,  i0 ,  n_  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_RU(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n  ,  n  ,  i0  ),
			'to'	:	(  n  ,  n  ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_RD(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n  ,  n_ ,  i0  ),
			'to'	:	(  n  ,  n_ ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_LU(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n_ ,  n  ,  i0  ),
			'to'	:	(  n_ ,  n  ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}


	def edge_midpoint_LD(self):
		n = self.indexN
		n_ = self.indexN_
		i0 = self.index0
		return {
			'from'	:	(  n_ ,  n_ ,  i0  ),
			'to'	:	(  n_ ,  n_ ,  i0  ),
			'bound'	:	( '==', '==', '==' ),
		}

