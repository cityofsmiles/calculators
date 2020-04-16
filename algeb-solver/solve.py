#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/solve.py

import sys
from sympy import *

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


expr_1 = sympify(sys.argv[1])
expr_2 = sympify(sys.argv[2])
input_type = str(sys.argv[3])
output_type = str(sys.argv[4])

if input_type == 'LaTeX':
	print("\n") 
	print('solve({}, {}) = '.format(latex(expr_1),latex(expr_2))) 
	
elif input_type == 'SymPy':
	print("\n") 
	print('solve({}, {}) = '.format(expr_1, expr_2))
	
else: 
	print("Wrong input type") 


if output_type == 'LaTeX':
	print("\n") 
	print(latex(solve((expr_1), expr_2))) 
	print("\n") 
	
elif output_type == 'SymPy':
	print("\n") 
	print(solve((expr_1), expr_2))
	print("\n") 
	
else: 
	print("Wrong output type") 
            






