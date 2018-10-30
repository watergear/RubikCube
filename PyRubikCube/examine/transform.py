from ..base.state import *
from .examine import *

def gen_transform_state(transforms, otherwise=True):
	index_set = get_index_set_by_transform(transforms, otherwise)
	indexes_list = get_indexes_group(index_set)
	state = State(indexes_list)
	for t in transforms:
		state.transform(t)
	return state

def transform_wv(transforms, wv):
	for t in transforms:
		wv = t.transform(wv)
	return wv
