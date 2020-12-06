#!/usr/bin/python

# python /home/jonathan/slope-solver/slope-solver.py


import os
columns, rows = os.get_terminal_size(0)

line = "\n" + ("=" * columns) + "\n"


global calculate
def calculate():
	
	print(line)
	
	a = str(input('''
Please type in the value of a: 
''')) 

	b = str(input('''
Please type in the value of b: 
''')) 

	str_to_solve = str(b + '*' + '((' + 'x' + '/' + '-' + a + ')' + '+' + '1' + ')')


	from sympy import sympify, simplify, Eq, solve, latex, fraction, symbols, lcm
	x, y = symbols("x, y")
	to_solve = sympify(str_to_solve) 
	slope_int_form = simplify(to_solve)
	coef = slope_int_form.as_coefficients_dict()
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

	if A == 1:
		A = ""

	if B == 1:
		B = ""
	elif B == -1:
		B = "-"

	print(line) 
	print("Results:") 
	print("Standard Form:")
	if numer_slope < 0:
		print("{}x + {}y = {}".format(A, B, C)) 
	else:
		print("{}x - {}y = {}".format(A, B, C)) 

	print("Slope-intercept Form:")
	latex_slope_int_form = latex(simplify(to_solve))

	print("y = {}".format(latex_slope_int_form)) 

	global again
	def again():
		calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: YES]
''') or "Y"

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









