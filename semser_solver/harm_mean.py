#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/harm_mean.py

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
	
	def reciprocal(n):
		return 1/n
	
	from sympy import sympify, simplify
	a_1 = sympify(a_1) 
	a_1 = reciprocal(a_1) 
	a_1 = '(' + str(a_1) + ')'
	
	a_n = sympify(a_n) 
	a_n = reciprocal(a_n) 
	a_n = '(' + str(a_n) + ')'
	
	str_to_solve = str('((' + a_n + '-' + a_1 + ')/(' + str(n) + '-' + "1" + '))') 
	
	to_solve = sympify(str_to_solve) 
	
	print(line) 
	print("Result:") 
	from sympy import simplify 
	result = simplify(to_solve)
			
	print("d = {}".format(result)) 
	
	def next_terms(first, difference, n):
		for i in range(1, int(n+1)):
			val = sympify(first) + (sympify(difference) * sympify(i)) - sympify(difference) 
			val = simplify(sympify(val))
			val = reciprocal(val) 
			term = "a_" + str(i) 
			print("{} = {}".format(term, val)) 
			
	next_terms(a_1, result, n)
	print(line) 
	
	

calculate()







	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	