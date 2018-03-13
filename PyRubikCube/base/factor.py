class Factor(tuple):
	def __new__(cls, name = '', factor = 0):
		vector = []
		vector.append(factor if 'X' == name else 0)
		vector.append(factor if 'Y' == name else 0)
		vector.append(factor if 'Z' == name else 0)
		return super(Factor, cls).__new__(cls, tuple(vector))

	def __init__(self, name = '', factor = 0):
		self.name = name;
		self.factor = factor;

	def __hash__(self):
		return hash(tuple(self))

	def __mul__(self, factor):
		return Factor(self.name, self.factor*factor)

	def __neg__(self):
		return self.__mul__(-1)

	def __eq__(self, other):
		return self.name == other.name and self.factor == other.factor

	def __iadd__(self, other):
		if 0 == self.factor:
			self = other
		elif 0 == other.factor:
			pass
		else:
			print(self.name, other.name)
			raise ValueError

		return self

	def __add__(self, other):
		return self.__iadd__(other)

	def __repr__(self):
		if 0 == self.factor:
			return "O"
		elif 1 == self.factor:
			sign = ""
		elif -1 == self.factor:
			sign = "-"
		else:
			sign = "%d" % self.factor

		return "{sign}{direct}".format(direct = self.name, sign = sign)
