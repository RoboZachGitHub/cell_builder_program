# cell_builder.py

import sys

class Unit_cell:

	def __init__(self, lattice_point_list = None, alats = None, a1 = float(1.0), basis = None, crystal_type = 'simple_cubic', vacuum_list = [0.0, 0.0, 0.0], major_axes = [0.0, 0.0, 0.0]):
			self.lattice_point_list = lattice_point_list
			self.a1 = a1
			self.alats = alats
			self.basis = basis
			self.vacuum_list = vacuum_list
			self.set_crystal_type(crystal_type)
			self.apply_secondary_lattice_sites()
			self.set_major_axes()


	def print_alats(self):
			print self.alats

	def set_crystal_type(self, crystal_type_string):
			# check if crystal_type_string is valid, if so apply, else exit
			valid_crystal_types = ['simple_cubic', 'base_centered_cubic']
			if crystal_type_string in valid_crystal_types:
				self.crystal_type = crystal_type_string
			else:
					print 'invalid crystal type'
					sys.exit()

	def apply_secondary_lattice_sites(self):
			a = self.a1		
			crystal_type = self.crystal_type
			if crystal_type == 'simple_cubic':
				# for simple cubis there are no secondary lattice points,
				# so the only thing needed is to add the cartesian information to the points
				for lattice_point in self.lattice_point_list:
					# calculate the cartesian coordinates for the lattice points and set them
					cartesian_x = lattice_point.matrix_coordinates[0]*a	
					cartesian_y = lattice_point.matrix_coordinates[1]*a	
					cartesian_z = lattice_point.matrix_coordinates[2]*a
					lattice_point.set_cartesian_coordinates(cartesian_x, cartesian_y, cartesian_z)
					
					#print info
					lattice_point.print_matrix_coordinates()
					lattice_point.print_cartesian_coordinates()
	
			if crystal_type == 'base_centered_cubic':
					#for each lattice point attach the secondary lattice points
					pass

	def set_major_axes(self):
		a = self.a1
		vacuum_list = self.vacuum_list
		x_vac = vacuum_list[0]
		y_vac = vacuum_list[1]
		z_vac = vacuum_list[2]

		x_max, y_max, z_max = self.return_maxes()
		
		crystal_type = self.crystal_type
		if crystal_type == 'simple_cubic':
			if x_vac != 0.0:
				major_x = x_max + x_vac
			else:
				major_x = x_max + a  
			
			if y_vac != 0.0:
				major_y = y_max + y_vac
			else:
				major_y = y_max + a  

			if z_vac != 0.0:
				major_z = z_max + z_vac
			else:
				major_z = z_max + a

			self.major_axes = [major_x, major_y, major_z]
			print self.major_axes


	def set_vacuum(self, length):
		self.vacuum == length



	def return_maxes(self):
		x_max = 0.0
		y_max = 0.0
		z_max = 0.0
		for lattice_point in self.lattice_point_list:
			cart_x = lattice_point.cartesian_coordinates[0]
			cart_y = lattice_point.cartesian_coordinates[1]
			cart_z = lattice_point.cartesian_coordinates[2]
			if cart_x > x_max:
				x_max = cart_x
			if cart_y > y_max:
				y_max = cart_y
			if cart_z > z_max:
				z_max = cart_z
		print "(x_max, y_max, z_max): (%f, %f, %f)" % (x_max, y_max, z_max)
		return x_max, y_max, z_max






class Lattice_point:

	def __init__(self, matrix_coordinates = None, cartesian_coordinates = None):
#			self.set_matrix_coordinates = self.set_matrix_coordinates(matrix_coordinates)
		self.matrix_coordinates = matrix_coordinates
	
	def set_matrix_coordinates(self, integer_list):
		self.matrix_coordinates = [integer_list[0], integer_list[1], integer_list[2]]

	def set_cartesian_coordinates(self, float_x, float_y, float_z):
		self.cartesian_coordinates = [float_x, float_y, float_z]

	def print_matrix_coordinates(self):
		print self.matrix_coordinates

	def print_cartesian_coordinates(self):
		print self.cartesian_coordinates
	

#class Cavity:
#	cavity_type
#	cavity_geometry_parameters




def main():
	print "here"
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
	

	# apply basis
	#unit_type = raw_input("scc or bcc: ")
	#surface_type = raw_input("100 or 110: ")

	# for bcc 100
	#for site in lattice_sites:

main()
