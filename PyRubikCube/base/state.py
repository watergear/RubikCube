from .factor import *
from .transform import *
from .group import *

class State:
	def __init__(self, indexes_list):
		self.indexes_map = {}
		self.directions_map = {}
		self.actives_map = {}

		for indexes in indexes_list:
			self.indexes_map[indexes] = indexes
			self.directions_map[indexes] = (factorX, factorY, factorZ)
			self.actives_map[indexes] = []

		self.transforms = []

	def transform(self, t):
		for key in self.indexes_map.keys():
			if t.is_active(self.indexes_map[key]):
				self.indexes_map[key], self.directions_map[key] = \
					t.transform((self.indexes_map[key], self.directions_map[key]))
				self.actives_map[key].append(1)
			else:
				self.actives_map[key].append(0)
		self.transforms.append(t)

	def __repr__(self):
		str = ""
		str += "--------------------------------------------"
		str += "\n"
		str += "indexes_map: " + repr(self.indexes_map)
		str += "\n"
		str += "directions_map: " + repr(self.directions_map)
		str += "\n"
		str += "actives_map: " + repr(self.actives_map)
		str += "\n"
		str += "transforms: " + repr(self.transforms)
		str += "\n"
		str += "--------------------------------------------"

		return str

def gen_state(transforms):
	index_set = get_index_set(transforms)
	indexes_list = get_indexes_group(index_set)
	state = State(indexes_list)
	for t in transforms:
		state.transform(t)
	return state

