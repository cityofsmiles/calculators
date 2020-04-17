#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/solve.py

from sympy import symbols, solve, sympify, latex

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


def mysolve(expr_1, expr_2, input_type, output_type):
	expr_1 = sympify(expr_1)
	expr_2 = sympify(expr_2)
	input_type = str(input_type)
	output_type = str(output_type)


	if input_type == 'LaTeX':
	
		print('solve({}, {}) = '.format(latex(expr_1),latex(expr_2))) 
	
	elif input_type == 'SymPy':
	
		print('solve({}, {}) = '.format(expr_1, expr_2))
	
	else: 
		print("Wrong input type") 


	if output_type == 'LaTeX':
	
		print(latex(solve((expr_1), expr_2))) 
	
	
	elif output_type == 'SymPy':
	
		print(solve((expr_1), expr_2))
	
	
	else: 
		print("Wrong output type") 
            






