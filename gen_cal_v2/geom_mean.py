#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/geom_mean.py

def calculate():
	a_1 = str(input('''
Please type in the value of the first term: 
''')) 
	a_n = str(input('''
Please type in the value of the last term: 
''')) 
	m = int(input('''
Please type in the number of terms to insert: 
''')) 
	n = m + 2
	n_minus_1 = n - 1
	n_minus_1 = str(n_minus_1)
	
# Find r
	r_formula = str('(' + a_n + '/' + a_1 + ')' + '**(1/' + n_minus_1 + ')')
	
	from sympy import sympify
	r_formula = sympify(r_formula) 
	
	print(line) 
	print("Result:") 
	from sympy import simplify 
	r_value = simplify(r_formula)
	
	def next_term(first, ratio, n):
		for i in range(1, int(n+1)):
			val = str(first) + '*' + '(' + str(ratio) + ')' + '**(' + str(i-1) + ')'
			val = simplify(sympify(val)) 
			term = "a_" + str(i) 
			print("{} = {}".format(term, val)) 
			
	if (int(n_minus_1) % 2) == 0:
		r_plus = r_value
		r_minus = simplify(-1 * r_value) 
		print("r = {} or {}".format(r_plus, r_minus))
		next_term(a_1, r_plus, n)
		print('or') 
		next_term(a_1, r_minus, n)
	else:
		print("r = {}".format(r_value)) 
		next_term(a_1, r_value, n)
	
	print(line) 
	
	
calculate()
	
	
	
	
	