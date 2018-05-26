class Factor(tuple):
	def __new__(cls, name = '', ratio = 0):
		vector = []
		vector.append(ratio if 'X' == name else 0)
		vector.append(ratio if 'Y' == name else 0)
		vector.append(ratio if 'Z' == name else 0)
		return super(Factor, cls).__new__(cls, tuple(vector))

	def __init__(self, name = '', ratio = 0):
		self.name = name;
		self.ratio = ratio;

	def __hash__(self):
		return hash(tuple(self))

	def __mul__(self, ratio):
		return Factor(self.name, self.ratio*ratio)

	def __neg__(self):
		return self.__mul__(-1)

	def __eq__(self, other):
		return self.name == other.name and self.ratio == other.ratio

	def __iadd__(self, other):
		if 0 == self.ratio:
			self = other
		elif 0 == other.ratio:
			pass
		else:
			print(self.name, other.name)
			raise ValueError

		return self

	def __add__(self, other):
		return self.__iadd__(other)

	def __repr__(self):
		if 0 == self.ratio:
			return "O"
		elif 1 == self.ratio:
			sign = ""
		elif -1 == self.ratio:
			sign = "-"
		else:
			sign = "%d" % self.ratio

		return "{sign}{factor}".format(factor = self.name, sign = sign)

def reFactor(tuple_factor):
	if ( not 0 == tuple_factor[0] ):
		return Factor("X", tuple_factor[0])
	if ( not 0 == tuple_factor[1] ):
		return Factor("Y", tuple_factor[1])
	if ( not 0 == tuple_factor[2] ):
		return Factor("Z", tuple_factor[2])
