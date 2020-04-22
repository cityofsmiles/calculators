#!/usr/bin/python

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/semser_solver.py

import os
columns, rows = os.get_terminal_size(0)
from fractions import Fraction as frac

cur_dir = os.path.dirname(os.path.abspath(__file__))
	
os.chdir(cur_dir)

import sys
sys.path.insert(0, cur_dir)

global line
line = "\n" + ("=" * columns) + "\n"

def welcome():
	print(line) 
	print('''
Welcome to the SeMSer Solver 
by Jonathan R. Bacolod  

Quickly solve Sequences, Means, and 
Series of numbers. 

Take note that the input must be in SymPy. 

Enjoy! 
''')
	print(line) 
welcome() 

def get_prob_type():
	prob_dict = {1: 'sequence', 2: 'mean', 3: 'series'}
	prob_type_inp = int(input('''
Which of the following do you want to solve? 
1 for Sequences [default]
2 for Means
3 for Series 
''') or 1)
	prob_type = prob_dict[prob_type_inp]

	if prob_type_inp == 1:
		func_dict = {1: 'Arithmetic', 2: 'Geometric', 3: 'Harmonic', 4: 'Fibonacci'}
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic [default]
2 for Geometric 
3 for Harmonic 
4 for Fibonacci  
'''.format(prob_type)) or 1)

	elif prob_type_inp == 2:
		func_dict = {1: 'Arithmetic', 2: 'Geometric', 3: 'Harmonic'}
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic [default]
2 for Geometric 
3 for Harmonic 
'''.format(prob_type)) or 1)

	elif prob_type_inp == 3:
		func_dict = {1: 'Arithmetic', 2: 'Finite Geometric', 3: 'Infinite Geometric'}
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic [default]
2 for Finite Geometric 
3 for Infinite Geometric  
'''.format(prob_type)) or 1)

	else:
		print("You have not typed a valid input.Please type any integer from 1 to 3.")
		
	
	func_type = func_dict[func_type_inp]
	problem = str(func_type + " " + prob_type) 
	
	problem_dict = {
"Arithmetic sequence": "arith_seq.py", 
"Arithmetic mean": "arith_mean.py", 
"Arithmetic series": "arith_series.py", 
"Geometric sequence": "geom_seq.py", 
"Geometric mean": "geom_mean.py", 
"Finite Geometric series": "fin_geom_series.py", 
"Infinite Geometric series": "inf_geom_series.py", 
"Harmonic sequence": "harm_seq.py", 
"Harmonic mean": "harm_mean.py", 
"Fibonacci sequence": "fib_seq.py"
}
	print(line) 
	
	file = problem_dict[problem]
	exec(open(file).read())
	
	again()
      
        
def again():
		calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N"

		if calc_again.upper() == 'Y':
			print(line) 
			get_prob_type()
            
		elif calc_again.upper() == 'N':
			print(line) 
			print('Babush!')
            
		else:
			print(line) 
			again()

	


get_prob_type()

