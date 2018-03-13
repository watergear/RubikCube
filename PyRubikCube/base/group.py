from .index import *
from .factor import *
from .transform import *

base_factor_list_XYZ = [
	{'factor':factorX, 'clockwise':CW},
	{'factor':factorX, 'clockwise':CCW},
	{'factor':factorY, 'clockwise':CW},
	{'factor':factorY, 'clockwise':CCW},
	{'factor':factorZ, 'clockwise':CW},
	{'factor':factorZ, 'clockwise':CCW},
]

def get_indexes_group(index_set):
	indexes_group = []
	for indexX in index_set:
		for indexY in index_set:
			for indexZ in index_set:
				indexes_group.append((indexX, indexY, indexZ))
	return indexes_group

def get_transform_group(index_set, base_factor_list = base_factor_list_XYZ):
	transfrom_group = []
	for base_factor in base_factor_list:
		for index in index_set:
			transfrom_group.append(
				Transform(
					factor = base_factor['factor'],
					clockwise = base_factor['clockwise'],
					index = index)
			)
	return transfrom_group

def get_index_set(transforms):
	index_set = set()
	for t in transforms:
		index_set.add(t.index)
		index_set.add(-t.index)
	index_set.add(Index('c', 1));
	return sorted(index_set);
