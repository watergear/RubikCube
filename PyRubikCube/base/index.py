class Index(object):
	def __init__(self, name = '', ratio = 0):
		self.name = name if not 0 == ratio else None;
		self.ratio = ratio;

	def __hash__(self):
		return hash(self.name)*self.ratio

	def __mul__(self, ratio):
		return Index(self.name, self.ratio*ratio)

	def __neg__(self):
		return self.__mul__(-1)

	def __iadd__(self, other):
		if 0 == self.ratio:
			self = other
		elif not 0 == other.ratio:
			raise ValueError
		return self

	def __add__(self, other):
		return self.__iadd__(other)

	def __eq__(self, other):
		if 0 == self.ratio and 0 == other.ratio:
			return True
		return self.ratio == other.ratio and self.name == other.name
	def __lt__(self, other):
		if self.ratio < other.ratio:
			return True
		elif self.ratio > other.ratio:
			return False
		elif 0 == self.ratio:
			return False
		elif self.ratio < 0:
			return self.name > other.name
		else:
			return self.name < other.name
	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)

	def __repr__(self):
		if ( 0 == self.ratio ):
			return "None";
		if ( self.ratio < 0 ):
			return "-" + self.name
		return self.name

class NoneIndex(Index):
	pass

class NumericIndex(int):
	pass
