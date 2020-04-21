#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser-solver/arith-seq.py

import os
columns, rows = os.get_terminal_size(0)
from sympy import symbols, sympify

x = symbols('x')

line = "\n" + ("=" * columns) + "\n"

def calculate():
	given_dict = {"a_1":"", "n":"", "d": "", "a_n": "", "a_k":""}
	
	for x in given_dict: 
		given_dict[x] = sympify(input('''
Please type in the value for {}:
(Type 'x' if unknown.)  
'''.format(x))) 

	print(given_dict) 

calculate()