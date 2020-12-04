#!/usr/bin/python 

import os
import subprocess

columns, rows = os.get_terminal_size(0)

cur_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(cur_dir)

global line
line = "\n" + ("=" * columns) + "\n"

def gen_cal_welcome():
    print(line) 
    print('''
Welcome to the General Calculator  
by Jonathan R. Bacolod  

Solve problems on algebraic expressions, 
linear equations, and polynomials. 

Enjoy!
''')
    print(line) 


def choose_calc():
	calc_type = int(input('''
Please type in the calculator you want to use:
	
1 for SymPyTeX Algebra Solver [default]
2 for Synthetic Division Calculator 
3 for System of Linear Equations Solver 
4 for Sequence, Mean, and Series Solver 
5 for Slope Solver
6 for Equation-Forms Solver
''') or 1) 

	calc_list = ['algeb_solver_v2', 'synthetic-calc', 'systems-solver', 'semser_solver', 'slope-solver', 'equation-forms-solver']
	
	if calc_type > len(calc_list):
		print(line) 
		print('''You have not typed a valid input.
Please run the program again.''')
		return
		

	for i in range(0, len(calc_list)):
		k = i + 1
		if calc_type == k:
			file = calc_list[i] + ".py"
			exec(open(file).read())
			os.chdir(cur_dir)			
	

def choose_other_calc():
		print(line) 
		choose_again = input('''
Do you want to use another calculator?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N"

		if choose_again.upper() == 'Y':
			print(line) 
			choose_calc()
            
		elif choose_again.upper() == 'N':
			print(line) 
			print('Exiting.')
             
		else:
			print(line) 
			choose_again()


if __name__ == '__main__':
	gen_cal_welcome()
	choose_calc()
	choose_other_calc()
