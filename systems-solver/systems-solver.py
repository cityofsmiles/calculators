#!/usr/bin/python

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/systems-solver/systems-solver.py


import os
columns, rows = os.get_terminal_size(0)

line = "\n" + ("=" * columns) + "\n"

def welcome():
	print(line) 
	print('''
Welcome to the SoLE Solver 
by Jonathan R. Bacolod  

Quickly solve Systems of Linear Equations 
using the Matrix Solution. 

Take note that the equations must
be written in standard form. 

Enjoy! 
''')
	print(line) 
welcome() 

import numpy as np
from fractions import Fraction as frac

def suffix(i):
	return {1:"st", 2:"nd", 3:"rd"}.get(i%10*(i%100 not in [11,12,13]), "th")
	
def calculate():
	num_equations = int(input('''
Please type in the number of equations
in the system: [default=2]
''') or 2)

# Get the coefficients. 
	coefficients_list = list() 

	for i in range(0, num_equations):
		num_equations_suffix = str(i+1) + suffix(i+1)
		coefficients_str = str(input('''
Please type in the numerical coefficients of 
the {} equation separated by comma: 
'''.format(num_equations_suffix))) 
		row = list(coefficients_str.split(","))
		row = [int(x) for x in row]
		coefficients_list.insert(i, row)
	
# Get the constant terms. 
	constants_str = str(input('''
Please type in the constant terms of 
the equations separated by comma:  
''')) 
	constants = list(constants_str.split(","))
	constants = [int(x) for x in constants]

# Convert to arrays then solve. 
	coefficients_array = np.array(coefficients_list) 
	constants_array = np.array(constants) 
	result = np.linalg.solve(coefficients_array, constants_array)
	result = [frac(x) for x in result]

# Print results. 
	print(line) 
	print("Results:") 
	for i in range(0, num_equations):
		num_equations_suffix = str(i+1) + suffix(i+1)
		print("Value of {} variable = {}".format(num_equations_suffix, result[i])) 
	print(line) 
	again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''') or "N"

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Babush!')
    else:
        again()

calculate()










