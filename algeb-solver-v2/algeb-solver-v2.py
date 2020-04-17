#!/usr/bin/python

# python ~/algeb-solver-v2/algeb-solver-v2.py
# cp -r /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/algeb-solver-v2 ~

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
os.chdir("/data/data/com.termux/files/home/algeb-solver-v2")

global string

def calculate():
	input_output = str(input('''
Please type in the kind of input and output 
you will use:
1 for LaTeX --> LaTeX [default]
2 for LaTeX --> SymPy  
3 for SymPy --> LaTeX 
4 for SymPy --> SymPy
''') or "1") 

	if input_output == "1":
		input_type="LaTeX"
		output_type="LaTeX"
	elif input_output == "2": 
		input_type="LaTeX"
		output_type="SymPy"
	elif input_output == "3": 
		input_type="SymPy"
		output_type="LaTeX"
	elif input_output == "4": 
		input_type="SymPy"
		output_type="SymPy"
	else:
		print('You have not typed a valid operator, please run the program again.')

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

# Get inputs. 
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
		subprocess.call(["bash ~/algeb-solver-v2/latex-to-sympy.sh", expr_1])
		exec(open('sympy-string.py').read())
		expr_1 = str(string) 
		
		if expr_2 != 0:
			expr_2 = expr_2.replace('\frac', '\\frac')
			subprocess.call(["bash ~/algeb-solver-v2/latex-to-sympy.sh", expr_2])
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

	again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        print(line) 
        calculate()
    elif calc_again.upper() == 'N':
        print(line) 
        print('Babush!')
    else:
        print(line) 
        again()

calculate()
    