# cell_builder.py

import math
import sys
import random

class Unit_cell:

	def __init__(self, lattice_point_list = None, alats = None, a1 = float(1.0), basis = None, crystal_type = 'simple_cubic', vacuum_list = [0.0, 0.0, 0.0], major_axes = [0.0, 0.0, 0.0]):
			self.lattice_point_list = lattice_point_list
			self.a1 = a1
			self.alats = alats
			self.basis = basis
#			self.vacuum_list = vacuum_list
#			self.set_crystal_type(crystal_type)
#			self.apply_secondary_lattice_sites()
#			self.set_major_axes()


	def print_alats(self):
		print "in print_alats"
		print self.alats


	def set_a1(self, a1):
		print "in set_a1"
		self.a1 = a1


	def set_crystal_type(self, crystal_type_string):
		print "in set_crystal_type"
		# check if crystal_type_string is valid, if so apply, else exit
		valid_crystal_types = ['simple_cubic', 'base_centered_cubic', '110_base_centered_cubic']
		if crystal_type_string in valid_crystal_types:
			self.crystal_type = crystal_type_string
		else:
			print 'invalid crystal type'
			sys.exit()


	def apply_secondary_lattice_sites(self):
		print "in apply_secondary_lattice_sites"
		### for now; this function is doing extra work instead of just setting the secondary lattice list
		a = self.a1		
		crystal_type = self.crystal_type
		if crystal_type == 'simple_cubic':
			# for simple cubis there are no secondary lattice points, so they should just be the same as the primary ones
			# so the only thing needed is to add the cartesian information to the points
			for lattice_point in self.lattice_point_list:
				
				secondary_points_list = [lattice_point.matrix_coordinates]
				lattice_point.set_secondary_matrix_coordinates(secondary_points_list)				

				### for now; this function is doing extra work instead of just setting the secondary lattice list
				# calculate the cartesian coordinates for the lattice points and set them
				cartesian_x = lattice_point.matrix_coordinates[0]*a	
				cartesian_y = lattice_point.matrix_coordinates[1]*a	
				cartesian_z = lattice_point.matrix_coordinates[2]*a
				lattice_point.set_cartesian_coordinates(cartesian_x, cartesian_y, cartesian_z)
				
				#print info
				lattice_point.print_matrix_coordinates()
				lattice_point.print_cartesian_coordinates()

		if crystal_type == 'base_centered_cubic':
			#for each lattice point there is the primary point and the point centered in the cube region
			for lattice_point in self.lattice_point_list:

				x_1 = lattice_point.matrix_coordinates[0]
				y_1 = lattice_point.matrix_coordinates[1]
				z_1 = lattice_point.matrix_coordinates[2]

				x_2 = x_1 + 0.5
				y_2 = y_1 + 0.5
				z_2 = z_1 + 0.5

				secondary_points_list = [[x_1,y_1,z_1], [x_2,y_2,z_2]]		
				lattice_point.set_secondary_matrix_coordinates(secondary_points_list)

		if crystal_type == '110_base_centered_cubic':
			for lattice_point in self.lattice_point_list:

				x_1 = lattice_point.matrix_coordinates[0]
				y_1 = lattice_point.matrix_coordinates[1]
				z_1 = lattice_point.matrix_coordinates[2]

				x_2 = x_1 + 0.5
				y_2 = y_1 + 0.5
				z_2 = z_1 

				x_3 = x_1 
				y_3 = y_1 + 0.5
				z_3 = z_1 + 0.5
				
				x_4 = x_1 + 0.5
				y_4 = y_1 
				z_4 = z_1 + 0.5

				secondary_points_list = [[x_1,y_1,z_1], [x_2,y_2,z_2], [x_3,y_3,z_3], [x_4,y_4,z_4]]		
				lattice_point.set_secondary_matrix_coordinates(secondary_points_list)
			

	def set_cartesians(self):
		print "in set_cartesians"
		crystal_type = self.crystal_type		
		a1 = self.a1
	
		# a1 equal to a2 equal to a3
		a1_e_a2_e_a3 = ['simple_cubic', 'base_centered_cubic']
	
		if crystal_type in a1_e_a2_e_a3:	
			for lattice_point in self.lattice_point_list:
				list_of_coordinate_sets = []
				for point in lattice_point.secondary_matrix_coordinates:
					x = a1*point[0]
					y = a1*point[1]
					z = a1*point[2]
					list_of_coordinate_sets.append([x,y,z])
				lattice_point.set_cartesian_coordinates(list_of_coordinate_sets)
	
		elif crystal_type == '110_base_centered_cubic':
			a1 = a1
			a2 = a1*math.sqrt(2)
			for lattice_point in self.lattice_point_list:
				list_of_coordinate_sets = []
				for point in lattice_point.secondary_matrix_coordinates:
					x = a1*point[0]
					y = a2*point[1]
					z = a2*point[2]
					list_of_coordinate_sets.append([x,y,z])
				lattice_point.set_cartesian_coordinates(list_of_coordinate_sets)
		
		else:
			print "crystal type invalid or not yet fully implemented"
			sys.exit()		
	
	
	def set_major_axes(self):
		print "in set_major_axes"
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
		
		else:
			print "set_major_axis not yet defined for %s" % self.crystal_type
			sys.exit()
	
	
	def set_vacuum_list(self, length_list):
		print "in set_vacuum_list"
		self.vacuum_list = length_list
	
	
	def return_maxes(self):
		print "in return_maxes"
		x_max = 0.0
		y_max = 0.0
		z_max = 0.0
		for lattice_point in self.lattice_point_list:
			cartesian_sets = lattice_point.cartesian_coordinates
			for cartesian_set in cartesian_sets:
				cart_x = cartesian_set[0]
				cart_y = cartesian_set[1]
				cart_z = cartesian_set[2]
				if cart_x > x_max:
					x_max = cart_x
				if cart_y > y_max:
					y_max = cart_y
				if cart_z > z_max:
					z_max = cart_z
		print x_max
		print y_max
		print z_max
		print "(x_max, y_max, z_max): (%f, %f, %f)" % (x_max, y_max, z_max)
		return x_max, y_max, z_max

	
	def return_layers(self):
		print "in return_layers"
		x_max, y_max, z_max = self.return_maxes()
		print x_max
		print y_max
		print z_max


	def print_all_matrix_points(self):
		print "in print_all_matrix_points"
		for lattice_point in self.lattice_point_list:
			lattice_point.print_matrix_coordinates()


	def print_all_cartesian_points(self):
		print "in print_all_cartesian_points"
		for lattice_point in self.lattice_point_list:
			print "\n"
			lattice_point.print_cartesian_coordinates()


class Lattice_point:

	def __init__(self, matrix_coordinates = None, cartesian_coordinates = None, secondary_matrix_coordinates = None):
#			self.set_matrix_coordinates = self.set_matrix_coordinates(matrix_coordinates)
		self.matrix_coordinates = matrix_coordinates

	def set_matrix_coordinates(self, integer_list):
		self.matrix_coordinates = [integer_list[0], integer_list[1], integer_list[2]]

	def set_secondary_matrix_coordinates(self, list_of_coordinates):
		# the coordinates where atoms are to be placed,
		# may (and usually does) include the coordinates of the node/primary matrix point
		self.secondary_matrix_coordinates = list_of_coordinates

	def set_cartesian_coordinates(self, list_of_coordinate_sets):
		self.cartesian_coordinates = list_of_coordinate_sets

	def set_extra_cartesian_coordinates(self, list_of_coordinate_sets):
		self.extra_cartesian_coordinates = list_of_coordinate_sets

	def print_matrix_coordinates(self):
		m_x = self.matrix_coordinates[0]
		m_y = self.matrix_coordinates[1]
		m_z = self.matrix_coordinates[2]
		print "! unit %d %d %d" % (m_x, m_y, m_z)

	def print_cartesian_coordinates(self):
		m_x = self.matrix_coordinates[0]
		m_y = self.matrix_coordinates[1]
		m_z = self.matrix_coordinates[2]
		print "! unit %d %d %d" % (m_x, m_y, m_z)
		for point in self.cartesian_coordinates:
			x = point[0]
			y = point[1]
			z = point[2]
			print "{:^10.5f} {:^10.5f} {:^10.5f}".format(x, y, z)
	
	

#class Cavity:
#	cavity_type
#	cavity_geometry_parameters


# random surface atom
def add_random_surface_atom(unit_cell):
	# generate random number for radius in range 1.5*a1 and random angles 
	# choose a random surface layer atom to displace from
	a1 = unit_cell.a1

	
	


	# use cube + discard method
	# i.e.  generate random point in cube and discard if outside of desired sphere
	# also make sure new point is inside bounds of the unit cell
	inside_sphere = False
	inside_bounds = False
	while not inside_sphere and not inside_bounds:
		del_x = random.uniform(-1.5*a1, 1.5*a1)
		del_y = random.uniform(-1.5*a1, 1.5*a1)
		del_z = random.uniform(0.0, 1.5*a1)
	



# kick atoms
def kick_atoms(unit_cell, layers_list):
	a1 = unit_cell.a1
	pass		


def main():
	# number of lattice points (number of sub_cells)
	x = 4
	y = 4
	z = 2
	lattice_sites = []
	for i in range(x):
		for j in range(y):
			for k in range(z):
				new_lattice_point = Lattice_point([i, j, k])
				lattice_sites.append(new_lattice_point)

	#for point in lattice_sites:	
	#	point.print_matrix_coordinates()


	new_unit_cell = Unit_cell(lattice_sites)
	new_unit_cell.set_crystal_type('110_base_centered_cubic')
	new_unit_cell.set_a1(3.1870)
#	new_unit_cell.set_vacuum_list([0.0, 0.0, 0.0])
	new_unit_cell.apply_secondary_lattice_sites()
	new_unit_cell.set_cartesians()
	new_unit_cell.return_maxes()
#	new_unit_cell.return_layers()
#	new_unit_cell.print_all_cartesian_points()
#	new_unit_cell.print_all_matrix_points()
#	new_unit_cell.set_vacuum_list([0.0, 0.0, 20.0])
#	new_unit_cell.set_major_axes()



main()

