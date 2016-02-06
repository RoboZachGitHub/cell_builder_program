# cell_builder.py

import sys

class Unit_cell:

	def __init__(self, lattice_point_list = None, alats = None, a1 = 1.0, basis = None, crystal_type = 'simple_cubic'):
			self.lattice_point_list = [lattice_point_list]
			self.a1 = a1
			self.alats = alats
			self.basis = basis
			self.set_crystal_type(crystal_type)

	def print_alats(self):
			print self.alats

	def set_crystal_type(self, crystal_type_string):
			self.crystal_type = crystal_type_string
			# check if crystal_type_string is valid, if so, apply to alats
			valid_crystal_types = ['simple_cubic', 'base_centered_cubic']
			if crystal_type_string in valid_crystal_types:
					apply_secondary_lattice_sites(self)
			else:
					print 'invalid crystal type'
					sys.exit()

	def apply_secondary_lattice_sites(self, crystal_type):
			a = self.a1		
			if crystal_type == 'simple_cubic':
					pass
			if crystal_type == 'base_centered_cubic':
					#for each lattice point attach the secondary lattice points
					pass
				


class Lattice_point:

	def __init__(self, matrix_coordinates = None):
		self.matrix_coordinates = matrix_coordinates
	
	def set_matrix_coordinates(int_x, int_y, int_z):
		# placeholder code for now
		self.matrix_coordinates = [int_x, int_y, int_z]

	def print_matrix_coordinates(self):
		print self.matrix_coordinates
		

#class Cavity:
#	cavity_type
#	cavity_geometry_parameters




def main():
	# number of lattice points (number of sub_cells)
	x = 3
	y = 3
	z = 1
	lattice_sites = []
	for i in range(x):
		for j in range(y):
			for k in range(z):
				new_lattice_point = Lattice_point([i, j, k])
				lattice_sites.append(new_lattice_point)

	for point in lattice_sites:	
		point.print_matrix_coordinates()


	new_unit_cell = Unit_cell(lattice_sites)
	new_unit_cell.print_alats()


	# apply basis
	#unit_type = raw_input("scc or bcc: ")
	#surface_type = raw_input("100 or 110: ")

	# for bcc 100
	#for site in lattice_sites:
