#!/usr/bin/python

# python /home/jonathan/slope-solver/slope-solver.py


import os
columns, rows = os.get_terminal_size(0)

line = "\n" + ("=" * columns) + "\n"


global calculate
def calculate():
	
	print(line)
	
	eq_str = str(input('''
Please type in the linear expression to convert: 
''')) 

	var = str(input('''
Please type in the variable to solve: 
''')) 

	from sympy import sympify, Eq, solve, latex	
	to_solve = sympify(eq_str) 
	var = sympify(var)
	eq = Eq(to_solve, 0)
	sol = solve((eq),(var))

	print(line) 
	print("Result:") 
	result = latex(sol[0])

	print("{} = {}".format(var, result)) 

	global again
	def again():
		calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N"

		if calc_again.upper() == 'Y':
			print(line) 
			calculate()
            
		elif calc_again.upper() == 'N':
			print(line) 
			print('Babush!')
            
		else:
			print(line) 
			again()

	again()

calculate()









