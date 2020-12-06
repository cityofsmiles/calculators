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

	from sympy import sympify, Eq, solve, latex, fraction, symbols, lcm	
	x, y = symbols("x, y")
	to_solve = sympify(eq_str) 
	eq = Eq(to_solve, 0)
	slope_int_form = solve((eq),(y))
	coef = slope_int_form[0].as_coefficients_dict()
	numer_slope, denom_slope = fraction(coef[x])
	numer_y_int, denom_y_int = fraction(coef[1])
	B = lcm(denom_slope, denom_y_int)

	if numer_slope < 0:
		A = -1*(B/denom_slope)*numer_slope
		C = (B/denom_y_int)*numer_y_int
	elif numer_slope == 0:
		A = 0
	else:
		A = (B/denom_slope)*numer_slope
		C = -1*(B/denom_y_int)*numer_y_int
	
	print(line) 
	print("Result:") 
	if numer_slope < 0:
		print("{}x + {}y = {}".format(A, B, C)) 
	else:
		print("{}x - {}y = {}".format(A, B, C)) 
	print(line) 

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









