from ..base.transform import factorX, factorY, factorZ

class Examiner:
	def __init__(self, src_vectors, dest_vectors, locked_areas, dump_message = False):
		self.src_vectors = src_vectors
		self.dest_vectors = dest_vectors
		self.locked_areas = locked_areas
		self.dump_message = dump_message

	def test(self, state):
		ok = True
		self.same_count = 0;
		self.shift_count = 0;
		self.error_count = 0;

		transforms = state.transforms
		for indexes in sorted(state.locations_map.keys()):
			vfrom = (indexes, (factorX, factorY, factorZ))
			vto = (state.locations_map[indexes], state.orientations_map[indexes])

			if vfrom in self.src_vectors:
				vdest = self.dest_vectors[self.src_vectors.index(vfrom)]
				pass_check = vto == vdest
				self.count_result(vfrom, vto, pass_check)
				ok = ok and pass_check

				self.dump_target_line_sep()
			else:
				in_area, pass_check = self.locked_areas.check(vfrom, vto)
				if in_area:
					self.count_result(vfrom, vto, pass_check)
					ok = ok and pass_check

					self.dump_locked_line_sep()

			actives = state.actives_map[indexes]
			self.dump(vfrom, vto, actives, transforms)

		return ok

	def count_result(self, vfrom, vto, pass_check):
		if ( vfrom == vto ):
			self.same_count += 1
		else:
			self.shift_count += 1
			#print(vfrom, vto)

		if ( not pass_check ):
			self.error_count += 1
			self.dump_error_line_sep()

	def dump(self, vfrom, vto, actives, transforms):
		if ( self.dump_message ):
			self.dump_dash_line_sep()
			print("From:".ljust(15), vfrom)
			print("To:".ljust(15), vto)
			print("Active:".ljust(15), actives)
			active_transforms = [transforms[i] for i in range(len(transforms)) if actives[i]]
			print("Transforms:".ljust(15), active_transforms)
			self.dump_dash_line_sep()
			print()

	def dump_target_line_sep(self):
		if ( self.dump_message ):
			print("*********************** Target ***********************")
	def dump_locked_line_sep(self):
		if ( self.dump_message ):
			print("======================= Locked =======================")
	def dump_error_line_sep(self):
		if ( self.dump_message ):
			print("####################### Error ########################")
	def dump_dash_line_sep(self):
		if ( self.dump_message ):
			print("------------------------------------------------------")
