#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/expand.py

import sys
from sympy import *

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


expr_1 = sympify(sys.argv[1])
input_type = str(sys.argv[2])
output_type = str(sys.argv[3])

if input_type == 'LaTeX':
	print("\n") 
	print('expand({}) = '.format(latex(expr_1))) 
	
elif input_type == 'SymPy':
	print("\n") 
	print('expand({}) = '.format(expr_1))
	
else: 
	print("Wrong input type") 


if output_type == 'LaTeX':
	print("\n") 
	print(latex(expand((expr_1)))) 
	print("\n") 
	
elif output_type == 'SymPy':
	print("\n") 
	print(expand((expr_1)))
	print("\n") 
	
else: 
	print("Wrong output type") 
            






