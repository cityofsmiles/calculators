#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/expand.py

def myexpand(expr_1, input_type, output_type):
	from sympy import expand, sympify, latex
	expr_1 = sympify(expr_1)
	input_type = str(input_type)
	output_type = str(output_type)

	if input_type == 'LaTeX':
		print('expand({}) = '.format(latex(expr_1))) 
	
	elif input_type == 'SymPy':
		print('expand({}) = '.format(expr_1))
	
	else: 
		print("Wrong input type") 


	if output_type == 'LaTeX':
		print(latex(expand((expr_1)))) 
	
	elif output_type == 'SymPy':
		print(expand((expr_1)))
	
	else: 
		print("Wrong output type") 
            






