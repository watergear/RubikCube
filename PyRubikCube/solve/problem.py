from ..base.state import gen_original_state

class Problem:
	def __init__(self, N):
		self.n = int(N/2)
		self.odd = (1 == N % 2)
		self.state = gen_original_state(self.n, self.odd)

	def scramble(self, transforms):
		for t in transforms:
			self.state.transform(t)
	