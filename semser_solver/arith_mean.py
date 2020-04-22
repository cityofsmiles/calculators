#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/arith_mean.py

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
	
	str_to_solve = str('((' + a_n + '-' + a_1 + ')/(' + str(n) + '-' + "1" + '))') 
	
	from sympy import sympify
	to_solve = sympify(str_to_solve) 
	
	print(line) 
	print("Result:") 
	from sympy import simplify 
	result = simplify(to_solve)
			
	print("d = {}".format(result)) 
	
	def next_term(first, difference, n):
		for i in range(1, int(n+1)):
			val = sympify(first) + (sympify(difference) * sympify(i)) - sympify(difference) 
			val = simplify(sympify(val)) 
			term = "a_" + str(i) 
			print("{} = {}".format(term, val)) 
			
	next_term(a_1, result, n)
	print(line) 
	
	

calculate()






