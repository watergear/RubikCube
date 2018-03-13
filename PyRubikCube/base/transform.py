from .factor import Factor

factorX = Factor('X', 1)
factorY = Factor('Y', 1)
factorZ = Factor('Z', 1)

CW = 1
CCW = -1

TX 	=	(	(1, 0, 0),
			(0, 0, -1),
			(0, 1, 0)
		)

TX_	=	(	(1, 0, 0),
			(0, 0, 1),
			(0, -1, 0)
		)

TY 	=	(	(0, 0, 1),
			(0, 1, 0),
			(-1, 0, 0)
		)

TY_	=	(	(0, 0, -1),
			(0, 1, 0),
			(1, 0, 0)
		)

TZ 	=	(	(0, -1, 0),
			(1, 0, 0),
			(0, 0, 1)
		)

TZ_	=	(	(0, 1, 0),
			(-1, 0, 0),
			(0, 0, 1)
		)

transform_mat_map = {
	(factorX, CW):	TX,
	(factorX, CCW):	TX_,
	(factorY, CW):	TY,
	(factorY, CCW):	TY_,
	(factorZ, CW):	TZ,
	(factorZ, CCW):	TZ_,
}

class Transform:
	def __init__(self, factor, clockwise, index):
		self.factor = factor
		self.clockwise = clockwise
		try:
			self.matrix = transform_mat_map[(factor, clockwise)]
		except KeyError:
			pass
		self.index = index

	def __eq__(self, other):
		return \
			self.factor == other.factor \
			and self.clockwise == other.clockwise \
			and self.index == other.index

	def __repr__(self):
		return "%s|%s" % (repr(self.factor)+('+' if 1 == self.clockwise else '-'), repr(self.index))

	def transform(self, v):
		matrix = self.matrix

		v_new = type(v)()

		i_n = len(v)
		j_n = len(matrix[0])
		k_n = len(v[0])
		for i in range(i_n):
			v_new_i = type(v[i])()
			for j in range(j_n):
				c = type(v[i][0])()
				for k in range(k_n):
					c+= v[i][k]*matrix[k][j]
				v_new_i += (c,)
			v_new += (v_new_i,)

		return v_new

	def dotmul(self, indexes):
		factor = self.factor
		c = type(indexes[0])()
		for i in range(len(indexes)):
			c += indexes[i]*factor[i]
		return c

	def is_active(self, indexes):
		index = self.dotmul(indexes)
		return self.index == index

def get_inverse_transform(t):
	return Transform(factor = t.factor, clockwise = t.clockwise*-1, index = t.index)