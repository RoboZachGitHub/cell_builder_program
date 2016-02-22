# cell_builder.py

from math import sqrt
import sys
import random

class Unit_cell:

	def __init__(self, lattice_point_list = None, alats = None, a1 = float(1.0), basis = None, crystal_type = 'simple_cubic', vacuum_list = [0.0, 0.0, 0.0], major_axes = [0.0, 0.0, 0.0]):
			self.lattice_point_list = lattice_point_list
			self.a1 = a1
			self.alats = alats
			self.basis = basis
			self.vacuum_list = vacuum_list
#			self.set_crystal_type(crystal_type)
#			self.apply_secondary_lattice_sites()
#			self.set_major_axes()


	def print_alats(self):
		print "in print_alats"
		print self.alats


	def set_a1(self, a1):
		print "in set_a1"
		self.a1 = a1

	def set_basis(self, atoms_list):
		self.basis = atoms_list


	def set_crystal_type(self, crystal_type_string, atoms_list):
		print "in set_crystal_type"
		# check if crystal_type_string is valid, if so apply, else exit
		valid_crystal_types = ['simple_cubic', 'base_centered_cubic', '110_base_centered_cubic']
		if crystal_type_string in valid_crystal_types:
			self.crystal_type = crystal_type_string
			self.set_basis(atoms_list)
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
				lattice_point.set_atoms_list(self.basis)				
	
		elif crystal_type == '110_base_centered_cubic':
			a1 = a1
			a2 = a1*sqrt(2)
			for lattice_point in self.lattice_point_list:
				list_of_coordinate_sets = []
				for point in lattice_point.secondary_matrix_coordinates:
					x = a1*point[0]
					y = a2*point[1]
					z = a2*point[2]
					list_of_coordinate_sets.append([x,y,z])
				lattice_point.set_cartesian_coordinates(list_of_coordinate_sets)
				print "110_base_centered_cubic not yet modified for basis of two different atoms"
				temporary_basis = 2*self.basis
				lattice_point.set_atoms_list(temporary_basis)
				print "checking basis"
				print lattice_point.atoms_list
		
		else:
			print "crystal type invalid or not yet fully implemented"
			sys.exit()		
	
	
	def set_major_axes(self):
		print "in set_major_axes"
		a1 = self.a1
		vacuum_list = self.vacuum_list
		x_vac = vacuum_list[0]
		y_vac = vacuum_list[1]
		z_vac = vacuum_list[2]
	
		x_max, y_max, z_max = self.return_maxes()
		
		crystal_type = self.crystal_type
	
		# a1 equal to a2 equal to a3
		a1_e_a2_e_a3 = ['simple_cubic', 'base_centered_cubic']

		if crystal_type in a1_e_a2_e_a3:
			a1 = a1
			if x_vac != 0.0:
				major_x = x_max + x_vac
			else:
				major_x = x_max + a1  
			
			if y_vac != 0.0:
				major_y = y_max + y_vac
			else:
				major_y = y_max + a1  
	
			if z_vac != 0.0:
				major_z = z_max + z_vac
			else:
				major_z = z_max + a1
	

		if crystal_type == "110_base_centered_cubic": 
			a1 = a1
			a2 = a1*sqrt(2)
			if x_vac != 0.0:
				major_x = x_max + x_vac
			else:
				major_x = x_max + a1*0.5
 
			if y_vac != 0.0:
				major_y = y_max + y_vac
			else:
				major_y = y_max + a2*0.5	

			if z_vac != 0.0:
				major_z = z_max + z_vac
			else:			
				major_z = z_max + a2*0.5				

	
		else:
			print "set_major_axis not yet defined for %s" % self.crystal_type
			sys.exit()
	
		self.major_axes = [major_x, major_y, major_z]

	
	def set_vacuum_list(self, length_list):
		print "in set_vacuum_list"
		self.vacuum_list = length_list
	
	
	def return_maxes(self):
		#print "in return_maxes"
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
		return x_max, y_max, z_max

	
#	def return_layers(self):
#		# returns all latice points ( which are sets of cartesian points or single points) that include the maximum z-value 
#		print "in return_layers"
##		print "this function assumes layers are defined by the z-axis"
#		
#		x_max, y_max, z_max = self.return_maxes()
#	
#		z_surface_points = []
#		
#		lattice_points = self.lattice_point_list
#		for lattice_point in lattice_points:
#			cartesian_sets = lattice_point.cartesian_coordinates
#			for cartesian_set in cartesian_sets:


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
		self.extra_cartesian_coordinates = []
		self.extra_atoms_list = []


	def set_matrix_coordinates(self, integer_list):
		self.matrix_coordinates = [integer_list[0], integer_list[1], integer_list[2]]

	def set_secondary_matrix_coordinates(self, list_of_coordinates):
		# the coordinates where atoms are to be placed,
		# may (and usually does) include the coordinates of the node/primary matrix point
		self.secondary_matrix_coordinates = list_of_coordinates

	def set_cartesian_coordinates(self, list_of_coordinate_sets):
		self.cartesian_coordinates = list_of_coordinate_sets

	def set_atoms_list(self, atoms_list):
		self.atoms_list = atoms_list

	def set_extra_cartesian_coordinates(self, list_of_coordinate_sets):
		#self.extra_cartesian_coordinates = list_of_coordinate_sets
		for coordinate_set in list_of_coordinate_sets:
			self.extra_cartesian_coordinates.append(coordinate_set)


	def set_extra_atoms_list(self, atoms_list):
		#self.extra_atoms_list = atoms_list
		for atom in atoms_list:
			self.extra_atoms_list.append(atom)


	def print_matrix_coordinates(self):
		m_x = self.matrix_coordinates[0]
		m_y = self.matrix_coordinates[1]
		m_z = self.matrix_coordinates[2]
		print "! unit %d %d %d" % (m_x, m_y, m_z)

	def return_cartesian_coordinates_string(self):
		
		stringer = ""		

		m_x = self.matrix_coordinates[0]
		m_y = self.matrix_coordinates[1]
		m_z = self.matrix_coordinates[2]
		stringer += "! unit %d %d %d\n" % (m_x, m_y, m_z)
		cartesian_sets = self.cartesian_coordinates
		atoms_list = self.atoms_list
		for i, cartesian_set in enumerate(cartesian_sets):
			atom_string = atoms_list[i]
			x = cartesian_set[0]
			y = cartesian_set[1]
			z = cartesian_set[2]
			stringer +=  "{:5s} {:^10.5f} {:^10.5f} {:^10.5f}\n".format(atom_string, x, y, z)
		if len(self.extra_cartesian_coordinates) > 0:
			extra_cartesian_sets = self.extra_cartesian_coordinates
			atoms_list = self.extra_atoms_list
			stringer += "\n! extra coordinates \n"
			for i, extra_cartesian_set in enumerate(extra_cartesian_sets):
				atom_string = atoms_list[i]
				x = extra_cartesian_set[0]
				y = extra_cartesian_set[1]
				z = extra_cartesian_set[2]
				stringer += "{:5s} {:^10.5f} {:^10.5f} {:^10.5f}\n".format(atom_string, x, y, z)

		return stringer

	def print_cartesian_coordinates(self):
		stringer = self.return_cartesian_coordinates_string()
		print stringer	


#class Cavity:
#	cavity_type
#	cavity_geometry_parameters


# random surface atom
def add_random_surface_atom(unit_cell, atom_type, sub_check = True):
	# generate random number for radius in range 1.5*a1 and random angles 
	# choose a random surface layer atom to displace from
	# sub_check defines whether to allow atoms within the entire top unit cell or only above the surface

	print "in add_random_surface_atom"
	a1 = unit_cell.a1
	
	# too_close is used later to check of atoms are within that distance to another atom
	# too_close is in units of Angstrom
	too_close = 1.25

	x_max, y_max, z_max = unit_cell.return_maxes()

	# get boundaries of unit cell in x and y direction
	major_x = unit_cell.major_axes[0]
	major_y = unit_cell.major_axes[1]
	major_z = unit_cell.major_axes[2]


	# grab a random atom contained in the surface layer (entire unit, not just max z)
	# this is the atom that will be used to perturb from
	list_of_surface_unit_lattice_points = []
	lattice_points = unit_cell.lattice_point_list
	for lattice_point in lattice_points:
		cartesian_sets = lattice_point.cartesian_coordinates
		for cartesian_set in cartesian_sets:
			z_coord = cartesian_set[2]
			if z_coord == z_max:
				list_of_surface_unit_lattice_points.append(lattice_point)

	# first choose random lattice point and keep track of it, then choose random cartesian and keep track of it
	random_lattice_point = random.choice(list_of_surface_unit_lattice_points)	
	#print "matrix coordinates of randomly chosen lattice point"
	random_lattice_point.print_matrix_coordinates()	

	if sub_check == True:
		random_cartesian_set = random.choice(random_lattice_point.cartesian_coordinates)
		#print "cartesian coordinates of randomly chosen cartesian set"
		#for coord in random_cartesian_set:
		#	print coord
	else:
		# find the true surface atoms
                z_max = 0.0
		surface_sets = []
                for cartesian_set in random_lattice_point.cartesian_coordinates:
                	cart_z = cartesian_set[2]
                        if cart_z > z_max:
                        	z_max = cart_z
                for cartesian_set in random_lattice_point.cartesian_coordinates:
			cart_z = cartesian_set[2]
			if cart_z == z_max:
				surface_sets.append(cartesian_set)
		# now, finally, we randomy choose a starting atom from the new list that contains only true surface atoms
		random_cartesian_set = random.choice(surface_sets)

	start_x = random_cartesian_set[0]
	start_y = random_cartesian_set[1]
	start_z = random_cartesian_set[2]

	# use cube + discard method
	# i.e.  generate random point in cube and discard if outside of desired sphere
	# also make sure new point is inside bounds of the unit cell
	inside_sphere = False
	any_too_close = True
	while inside_sphere == False or any_too_close == True:
		del_x = random.uniform(-a1, a1)
		del_y = random.uniform(-a1, a1)
		del_z = random.uniform(0.0, a1)
		# check if within eligible sphere	
		r = sqrt(del_x**2 + del_y**2 + del_z**2)
		if r <= (a1):
			inside_sphere = True
		else:
			# continue sends code back to the beginning of the while loop
			continue
	
		new_x = start_x + del_x		
		new_y = start_y + del_y		
		new_z = start_z + del_z	

		# if new_x or new_y coordinates are outside of the major axes, subtract to give appropriate positions
		# this should never occur for new_z, but check just in case
		if new_x > major_x:
			new_x = (new_x - major_x)				
		if new_x < 0.0:
			new_x = (major_x + new_x)
		if new_y > major_y:
			new_y = (new_y - major_y)				
		if new_y < 0.0:
			new_y = (major_y + new_y)
		if new_z > major_z:
			print "is the cell set up with a suitable vacuum? new_z is outside of cell"
			sys.exit()

		# now check whether too close to any pre-existing atoms
		# if no atoms are too close we assign too_close to false
		# if any are too close, we continue, sending code back to the beginning of the while loop
		cartesian_sets = []
		for lattice_point in list_of_surface_unit_lattice_points: 	
			for cartesian_set in lattice_point.cartesian_coordinates:
				cartesian_sets.append(cartesian_set)
			for extra_cartesian_set in lattice_point.extra_cartesian_coordinates:
				cartesian_sets.append(extra_cartesian_set)
		
		any_too_close = too_close_checker(unit_cell, cartesian_sets, [new_x, new_y, new_z], too_close)
	#	print "any_too_close: " + str(any_too_close)
		if any_too_close == True:
			continue

	# new point passed all tests, add it as an extra set of cartesians to the lattice_point that was chosen
	#print "new point passed tests"
	print "here any_too_close: " + str(any_too_close)
	#print "inside_sphere: " + str(inside_sphere)
	random_lattice_point.set_extra_cartesian_coordinates([[new_x, new_y, new_z]])
	random_lattice_point.set_extra_atoms_list([atom_type])
	
		
		
def too_close_checker(unit_cell, cartesian_sets, cartesian_set_to_check, dist):
	x1 = cartesian_set_to_check[0] 	
	y1 = cartesian_set_to_check[1] 	
	z1 = cartesian_set_to_check[2]
 	
	for cartesian_set in cartesian_sets:
		x2 = cartesian_set[0] 	
		y2 = cartesian_set[1] 	
		z2 = cartesian_set[2]

		del_x = x1 - x2 	
		del_y = y1 - y2 	
		del_z = z1 - z2 	

		r = sqrt(del_x**2 + del_y**2 + del_z**2)
		#print "r is: " + str(r)	
		if r < dist:
			#print "too close!"
			return True
		# if any values, x2 y2 z2 are zero; must also check the edge of the unit cell
		elif x2 == 0.0 or y2 == 0.0 or z2 == 0.0:
			if x2 == 0.0:
				x2 = unit_cell.major_axes[0]		
			if y2 == 0.0:
				y2 = unit_cell.major_axes[1]		
			if z2 == 0.0:
				z2 = unit_cell.major_axes[2]
	
			del_x = x1 - x2 	
			del_y = y1 - y2 	
			del_z = z1 - z2 	
		
			r = sqrt(del_x**2 + del_y**2 + del_z**2)
			#print "r is: " + str(r)	
			if r < dist:
				#print "too close!"
				return True
		else:
			continue

	# returns False if made it through the list
	return False


# kick atoms
def kick_atoms(unit_cell, layers_list):
	a1 = unit_cell.a1
	pass		

def shift_coords(unit_cell, all_or_z):
	# shifts all coordinates in x y and z direction by 0.1 angstrom
	# useful for quantum espresso input/ visualization
	lattice_points = unit_cell.lattice_point_list
	for lattice_point in lattice_points:
		new_cartesian_sets = []
		for cartesian_set in lattice_point.cartesian_coordinates:			
			x = cartesian_set[0]
			y = cartesian_set[1]
			z = cartesian_set[2]
				
			shifted_x = x + 0.1
			shifted_y = y + 0.1
			shifted_z = z + 0.1

			if all_or_z == "all":
				new_cartesian_sets.append([shifted_x, shifted_y, shifted_z])
			elif all_or_z == "z":
				new_cartesian_sets.append([x, y, shifted_z])

		lattice_point.set_cartesian_coordinates(new_cartesian_sets)

		

def output_cell(unit_cell, filename):
	outFile = open(filename + ".xyz", 'w')
	out_string = ""

	lattice_points = unit_cell.lattice_point_list
	for lattice_point in lattice_points:
		out_string += lattice_point.return_cartesian_coordinates_string()
		out_string += "\n"	

	outFile.write(out_string)
	outFile.close()


def main():
	# number of lattice points (number of sub_cells)
	x = 1 
	y = 1
	z = 3
	lattice_sites = []
	for i in range(x):
		for j in range(y):
			for k in range(z):
				new_lattice_point = Lattice_point([i, j, k])
				lattice_sites.append(new_lattice_point)

	#for point in lattice_sites:	
	#	point.print_matrix_coordinates()


	out_string = 'w_1x1_h20_surf_1' 	
	out_string_2 = 'w_2X2_h2_1'
	new_unit_cell = Unit_cell(lattice_sites)
	new_unit_cell.set_crystal_type('110_base_centered_cubic', ['W', 'W'])
	new_unit_cell.set_a1(3.1870)
	new_unit_cell.set_vacuum_list([0.0, 0.0, 20.0])
	new_unit_cell.apply_secondary_lattice_sites()
	new_unit_cell.set_cartesians()
	new_unit_cell.return_maxes()
	new_unit_cell.set_major_axes()
		
	shift_coords(new_unit_cell, "z")
	for i in range(20):
		add_random_surface_atom(new_unit_cell, 'H', sub_check = False)


	output_cell(new_unit_cell, out_string)
	#	new_unit_cell.return_layers()
	#	new_unit_cell.print_all_cartesian_points()
	#	new_unit_cell.print_all_matrix_points()
	#	new_unit_cell.set_vacuum_list([0.0, 0.0, 20.0])
	#	new_unit_cell.set_major_axes()



main()

