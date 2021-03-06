from .transform import factorX, factorY, factorZ
from .group import *

class State:
	def __init__(self, indexes_list):
		self.locations_map = {}
		self.orientations_map = {}
		self.actives_map = {}

		for indexes in indexes_list:
			self.locations_map[indexes] = indexes
			self.orientations_map[indexes] = (factorX, factorY, factorZ)
			self.actives_map[indexes] = []

		self.transforms = []

	def transform(self, t):
		for key in self.locations_map.keys():
			if t.is_active(self.locations_map[key]):
				self.locations_map[key], self.orientations_map[key] = \
					t.transform((self.locations_map[key], self.orientations_map[key]))
				self.actives_map[key].append(1)
			else:
				self.actives_map[key].append(0)
		self.transforms.append(t)

	def __repr__(self):
		str = ""
		str += "--------------------------------------------"
		str += "\n"
		str += "locations_map: " + repr(self.locations_map)
		str += "\n"
		str += "orientations_map: " + repr(self.orientations_map)
		str += "\n"
		str += "actives_map: " + repr(self.actives_map)
		str += "\n"
		str += "transforms: " + repr(self.transforms)
		str += "\n"
		str += "--------------------------------------------"

		return str

def gen_original_state(n, odd):
	index_set = get_index_set_by_n(n, odd)
	indexes_list = get_indexes_group(index_set)
	return State(indexes_list)
