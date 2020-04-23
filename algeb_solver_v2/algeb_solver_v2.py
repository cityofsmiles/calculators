#!/usr/bin/python

# cd ~/algeb-solver-v2; python algeb-solver-v2.py; cd ~
# cp -r /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/algeb-solver-v2 ~
# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/algeb_solver_v2/algeb_solver_v2.py

import os
columns, rows = os.get_terminal_size(0)


line = "\n" + ("=" * columns) + "\n"


def welcome():
    print(line) 
    print('''
Welcome to SymPyTeX Algebra Solver 
by Jonathan R. Bacolod  

Solve problems on algebraic expressions 
and polynomials. 

Input and output can be written using
LaTeX or SymPy. 

Enjoy!
''')
    print(line) 

welcome()

import sys
import subprocess

cur_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, cur_dir)
	
os.chdir(cur_dir)

global string

global calculate
def calculate():
	def get_input_output():
		global input_output
		input_output = int(input('''
Please type in the kind of input and output 
you will use:
1 for LaTeX --> LaTeX [default]
2 for LaTeX --> SymPy  
3 for SymPy --> LaTeX 
4 for SymPy --> SymPy
''') or 1) 

		if input_output > 4:
			print(line) 
			print('''You have not typed a valid input.
Please choose a number from 1 to 4.
''')
			print(line) 
			get_input_output()

	get_input_output()

	input_list = [0, 0, 1, 1]
	output_list = [0, 1, 0, 1]
	type = ["LaTeX", "SymPy"]
	
	#if input_output > len(input_list):
		#print(line) 
		#print('''You have not typed a valid input.
#Please run the program again.''')
		#return
		
	for i in range(0, len(input_list)):
		k = i + 1
		if input_output == k:
			input_type = type[input_list[i]]
			output_type = type[output_list[i]]
		
	def get_operation():
		print(line) 
		global operation
		operation = int(input('''
Please type in the operation you would like 
to complete:
1 for Cancel
2 for Expand
3 for Factor
4 for Simplify
5 for Find Roots 
6 for Solve 
''')) 

		if operation > 6:
			print(line) 
			print('''You have not typed a valid input.
Please choose a number from 1 to 6.
''')
			print(line) 
			get_operation()

	get_operation()

# Get inputs. 
	print(line) 
	if operation == 1: 
		expr_1 = str(input('''
Please enter the first {} expression
(numerator):
'''.format(input_type))) 
		expr_2 = str(input('''
Please enter the second {} expression
(denominator):
'''.format(input_type))) 

	elif operation >= 2 and operation <= 4: 
		expr_1 = str(input('''
Please enter the {} expression:
'''.format(input_type))) 
		expr_2 = 0
	
	elif operation == 5 or operation == 6: 
		expr_1 = str(input('''
Please enter the {} expression to be solved:
'''.format(input_type))) 
		expr_2 = str(input('''
Please enter the variable to be solved:
''')) 

	else: 
		print('''You have not typed a valid operation.  
Please run the program again.''')

# Convert LaTeX expressions to SymPy
	if input_type == "LaTeX": 
		expr_1 = expr_1.replace('\frac', '\\frac')
		subprocess.run(["bash", "./latex-to-sympy.sh", expr_1])
		exec(open('sympy-string.py').read())
		expr_1 = str(string) 
		
		if expr_2 != 0:
			expr_2 = expr_2.replace('\frac', '\\frac')
			subprocess.run(["bash", "./latex-to-sympy.sh", expr_2])
			exec(open('sympy-string.py').read())
			expr_2 = str(string) 

# Perform the selected operation. 
	print(line) 
	print("Result:") 
	
	if operation == 1:
		from mycancel import mycancel
		mycancel(expr_1, expr_2, input_type, output_type)
		
	elif operation == 2:
		from myexpand import myexpand
		myexpand(expr_1, input_type, output_type)
	
	elif operation == 3:
		from myfactor import myfactor
		myfactor(expr_1, input_type, output_type)
		
	elif operation == 4:
		from mysimplify import mysimplify
		mysimplify(expr_1, input_type, output_type)
		
	elif operation == 5:
		from myroots import myroots
		myroots(expr_1, expr_2, input_type, output_type)
		
	elif operation == 6:
		from mysolve import mysolve
		mysolve(expr_1, expr_2, input_type, output_type)
		
	else: 
		print('''You have not typed a valid operator.  
Please run the program again.''') 
		
	print(line) 
	
	#from algeb_again import again
	again()

global again
def again():
		calc_again = str(input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N") 

		if calc_again.upper() == 'Y':
			print(line) 
			#from algeb_solver_v2 import calculate
			calculate()
			
		elif calc_again.upper() == 'N':
			print(line) 
			print('Babush!')
			return
			
		else:
			print(line) 
			again()

calculate()

	