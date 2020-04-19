#!/usr/bin/python 

# cd /storage/emulated/0/GNURoot/home/Scripts/termux/calculators; python gen_cal.py
# ln -s /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/gen_cal.py /data/data/com.termux/files/usr/bin/gcal

import os
columns, rows = os.get_terminal_size(0)

global line
line = "\n" + ("=" * columns) + "\n"

def welcome():
    print(line) 
    print('''
Welcome to the General Calculator  
by Jonathan R. Bacolod  

Solve problems on algebraic expressions, linear equations, and polynomials. 

Enjoy!
''')
    print(line) 
welcome() 

import subprocess

cur_dir = os.path.dirname(os.path.abspath(__file__))
	
os.chdir(cur_dir)

def choose_calc():
	calc_type = str(input('''
Please type in the calculator you want to use:
	
1 for SymPyTeX Algebra Solver [default]
2 for Synthetic Division Calculator 
3 for System of Linear Equations Solver 
''') or "1") 

	if calc_type == "1":
		dir = cur_dir + "/" + 'algeb-solver-v2'
		os.chdir(dir)
		exec(open('algeb-solver-v2.py').read())
		os.chdir(cur_dir)
	elif calc_type == "2": 
		dir = cur_dir + "/" + 'synthetic-calc'
		os.chdir(dir)
		exec(open('synthetic-calc.py').read())
		os.chdir(cur_dir)
	elif calc_type == "3": 
		dir = cur_dir + "/" + 'systems-solver'
		os.chdir(dir)
		exec(open('systems-solver.py').read())
		os.chdir(cur_dir)
	else:
		print('''You have not typed a valid input.
Please run the program again.''')

	def choose_again():
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
			print('Babush!')
             
		else:
			print(line) 
			choose_again()

	choose_again()

choose_calc()