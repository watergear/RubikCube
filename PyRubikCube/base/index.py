class Index:
	def __init__(self, name = '', sign = 0):
		self.name = name if not 0 == sign else None;
		self.sign = sign;

	def __hash__(self):
		return hash(self.name)*self.sign

	def __mul__(self, factor):
		return Index(self.name, self.sign*factor)

	def __neg__(self):
		return self.__mul__(-1)

	def __iadd__(self, other):
		if 0 == self.sign:
			self = other
		elif not 0 == other.sign:
			raise ValueError
		return self

	def __add__(self, other):
		return self.__iadd__(other)

	def __eq__(self, other):
		if 0 == self.sign and 0 == other.sign:
			return True
		return self.sign == other.sign and self.name == other.name
	def __lt__(self, other):
		if self.sign < other.sign:
			return True
		elif self.sign > other.sign:
			return False
		elif 0 == self.sign:
			return False
		elif self.sign < 0:
			return self.name > other.name
		else:
			return self.name < other.name
	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)

	def __repr__(self):
		if ( 0 == self.sign ):
			return "None";
		if ( self.sign < 0 ):
			return "-" + self.name
		return self.name
