from .factor import Factor

factorX = Factor('X', 1)
factorY = Factor('Y', 1)
factorZ = Factor('Z', 1)

CW = 1
CCW = -1

RotationX 	= \
		(	(1, 0, 0),
			(0, 0, -1),
			(0, 1, 0)
		)

RotationX_	= \
		(	(1, 0, 0),
			(0, 0, 1),
			(0, -1, 0)
		)

RotationY 	= \
		(	(0, 0, 1),
			(0, 1, 0),
			(-1, 0, 0)
		)

RotationY_	= \
		(	(0, 0, -1),
			(0, 1, 0),
			(1, 0, 0)
		)

RotationZ 	= \
		(	(0, -1, 0),
			(1, 0, 0),
			(0, 0, 1)
		)

RotationZ_	= \
		(	(0, 1, 0),
			(-1, 0, 0),
			(0, 0, 1)
		)

mapTransformMat = {
	(factorX, CW):	RotationX,
	(factorX, CCW):	RotationX_,
	(factorY, CW):	RotationY,
	(factorY, CCW):	RotationY_,
	(factorZ, CW):	RotationZ,
	(factorZ, CCW):	RotationZ_,
}

def mat_inverse(mm):
	mm_i = type(mm)()
	for i in range(len(mm[0])):
		vv = type(mm[0])()
		for j in range(len(mm)):
			vv += (mm[j][i],)
		mm_i += (vv,)
	return mm_i

def mat_mul(m1, m2):
	mm = type(m1)()

	i_n = len(m1)
	j_n = len(m2[0])
	k_n = len(m1[0])
	for i in range(i_n):
		vv = type(m1[i])()
		for j in range(j_n):
			c = type(m1[i][0])()
			for k in range(k_n):
				c += m1[i][k]*m2[k][j]
			vv += (c,)
		mm += (vv,)

	return mm

def mat_div(m1, m2):
	return mat_mul(mat_inverse(m2), m1)

def vec_mul(v1, v2):
	c = type(v1[0])()
	for i in range(len(v1)):
		c += v1[i]*v2[i]
	return c

class Transform:
	def __init__(self, factor, clockwise, index):
		self.factor = factor
		self.clockwise = clockwise
		try:
			self.matrix = mapTransformMat[(factor, clockwise)]
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
		return mat_mul(v, self.matrix)

	def is_active(self, indexes):
		index = vec_mul(indexes, self.factor)
		return self.index == index

def inverse_transform(t):
	return Transform(factor = t.factor, clockwise = t.clockwise*-1, index = t.index)

def inverse_transforms(tlist):
	return [inverse_transform(t) for t in tlist[::-1]]
