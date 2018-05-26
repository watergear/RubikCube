from .index import Index,NumericIndex
from .transform import *

def get_index_set_by_transform(transforms, otherwise=True):
	index_set = set()
	for t in transforms:
		index_set.add(t.index)
		index_set.add(-t.index)
	if otherwise:
		index_set.add(Index('c', 1));
	return sorted(index_set);

def get_index_set_by_n(n, odd):
	index_set = set()
	for i in range(1,n+1):
		index_set.add(NumericIndex(i))
		index_set.add(NumericIndex(-i))
	if odd:
		index_set.add(NumericIndex(0))
	return sorted(index_set)
	
def get_indexes_group(index_set):
	indexes_group = []
	for indexX in index_set:
		for indexY in index_set:
			for indexZ in index_set:
				indexes_group.append((indexX, indexY, indexZ))
	return indexes_group

base_factorXYZ_list = [
	{'factor':factorX, 'clockwise':CW},
	{'factor':factorX, 'clockwise':CCW},
	{'factor':factorY, 'clockwise':CW},
	{'factor':factorY, 'clockwise':CCW},
	{'factor':factorZ, 'clockwise':CW},
	{'factor':factorZ, 'clockwise':CCW},
]

def get_transform_group(index_set, base_factor_list = base_factorXYZ_list):
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
