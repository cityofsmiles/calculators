#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/factor.py

import sys
from sympy import *
import os
columns, rows = os.get_terminal_size(0)

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


expr_1 = sympify(sys.argv[1])
input_type = str(sys.argv[2])
output_type = str(sys.argv[3])

line = "\n" + ("=" * columns) + "\n"
print(line) 
print("Result:") 

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
            
print(line) 





