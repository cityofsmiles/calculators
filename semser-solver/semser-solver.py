#!/usr/bin/python

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser-solver/semser-solver.py

import os
columns, rows = os.get_terminal_size(0)
from fractions import Fraction as frac

os.chdir("/storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser-solver")

line = "\n" + ("=" * columns) + "\n"

def welcome():
	print(line) 
	print('''
Welcome to the SeMSer Solver 
by Jonathan R. Bacolod  

Quickly solve Sequences, Means, and Series 
of numbers. 

Enjoy! 
''')
	print(line) 
welcome() 

def suffix(i):
	return {1:"st", 2:"nd", 3:"rd"}.get(i%10*(i%100 not in [11,12,13]), "th")

def get_prob_type():
	prob_dict = {1: 'sequence', 2: 'mean', 3: 'series'}
	prob_type_inp = int(input('''
Which of the following do you want to solve? 
1 for Sequences 
2 for Means
3 for Series 
'''))
	prob_type = prob_dict[prob_type_inp]

	if prob_type_inp == 1:
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic  
2 for Geometric 
3 for Harmonic 
4 for Fibonacci  
'''.format(prob_type)))

	elif prob_type_inp == 2:
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic  
2 for Geometric 
3 for Harmonic 
'''.format(prob_type)))

	elif prob_type_inp == 3:
		func_type_inp = int(input('''
Which type of {} do you want to solve? 
1 for Arithmetic  
2 for Finite Geometric 
3 for Infinite Geometric  
4 for Harmonic 
'''.format(prob_type)))

	else:
		print("You have not typed a valid input.Please type any integer from 1 to 3.")
		#get_prob_type()
		
	func_dict = {1: 'Arithmetic', 2: 'Geometric', 3: 'Harmonic', 4: 'Fibonacci'}
	func_type = func_dict[func_type_inp]
	problem = str(func_type + " " + prob_type) 
	
	#print(problem) 
	exec(open("arith-seq.py").read())
        
	

get_prob_type()

