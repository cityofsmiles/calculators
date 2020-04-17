#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/factor.py

from sympy import symbols, factor, sympify, latex

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


def myfactor(expr_1, input_type, output_type):
	expr_1 = sympify(expr_1)
	input_type = str(input_type)
	output_type = str(output_type)

	if input_type == 'LaTeX':
	
		print('factor({}) = '.format(latex(expr_1))) 
	
	elif input_type == 'SymPy':
	
		print('factor({}) = '.format(expr_1))
	
	else: 
		print("Wrong input type") 


	if output_type == 'LaTeX':
	
		print(latex(factor((expr_1)))) 
	
	
	elif output_type == 'SymPy':
	
		print(factor((expr_1)))
	
	
	else: 
		print("Wrong output type") 
            






