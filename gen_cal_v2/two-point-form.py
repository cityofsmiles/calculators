#!/usr/bin/python

# python /home/jonathan/slope-solver/slope-solver.py


import os
columns, rows = os.get_terminal_size(0)

line = "\n" + ("=" * columns) + "\n"


global calculate
def calculate():
	
	print(line)
	
	x_1 = str(input('''
Please type in the value of x_1: 
''')) 

	y_1 = str(input('''
Please type in the value of y_1: 
''')) 

	x_2 = str(input('''
Please type in the value of x_2: 
''')) 

	y_2 = str(input('''
Please type in the value of y_2: 
''')) 

	str_to_solve = str('((' + y_2 + '-' + y_1 + ')/(' + x_2 + '-' + x_1 + '))' + '*' + '(' + 'x' + '-' + x_1 + ')' + '+' + y_1)

	from sympy import sympify, simplify, latex
	to_solve = sympify(str_to_solve) 

	print(line) 
	print("Result:") 
	result = latex(simplify(to_solve))

	print("y = {}".format(result)) 

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









