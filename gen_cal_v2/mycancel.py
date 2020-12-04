#!/usr/bin/python

# python ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/cancel.py

def mycancel(expr_1, expr_2, input_type, output_type):
	from sympy import cancel, sympify, latex
	expr_1 = sympify(expr_1)
	expr_2 = sympify(expr_2)
	input_type = str(input_type)
	output_type = str(output_type)

	if input_type == 'LaTeX':
	
		print('cancel(({})/({})) = '.format(latex(expr_1), latex(expr_2))) 
	
	elif input_type == 'SymPy':
	
		print('cancel(({})/({})) = '.format(expr_1, expr_2))
	
	else: 
		print("Wrong input type") 


	if output_type == 'LaTeX':
	
		print(latex(cancel((expr_1)/(expr_2)))) 
	
	
	elif output_type == 'SymPy':
	
		print(cancel((expr_1)/(expr_2)))
	
	else: 
		print("Wrong output type") 
            






