#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/harm_seq.py

def calculate():
	
	vars_dict = {'5': 'a_1', '6': 'a_2', '2': 'n', '1': 'a_n', '3': 'a_k', '4': 'k'}
	
	var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'a_n' [default]
2 for 'n'
3 for 'a_k'
''') or '1') 

	var_to_solve = vars_dict[var_to_solve_key]
	del vars_dict[var_to_solve_key]
	
	given_dict = {}
	for key in vars_dict:
		new_key = vars_dict[key]
		given_dict[new_key] = ''
			
	for x in given_dict: 
		given_dict[x] = str(input('''
Please type in the value for {}:
(Type enter if not given.)  
'''.format(x)) or "") 

	def reciprocal(n):
		return 1/n
	
	from sympy import sympify, simplify
	given_dict[var_to_solve] = "0"
	
# Compute d
	if given_dict["a_2"] != "": 
		first_term = given_dict["a_1"] 
		first_term = sympify(first_term) 
		first_term = reciprocal(first_term) 
		second_term = given_dict["a_2"] 
		second_term = sympify(second_term) 
		second_term = reciprocal(second_term) 
		given_dict["d"] = simplify((second_term) - (first_term)) 
		
	else: 
		given_dict["d"] = "1"
		given_dict["a_2"] = "xyz"

	if given_dict["a_k"] == "" and given_dict["k"] == "" and var_to_solve != "a_1":
		given_dict["a_k"] = given_dict["a_1"] 
		given_dict["k"] = "1"
		
	
	exception_list = ["n", "k", "d"]
	for x in exception_list: 
		given_dict[x] = sympify(given_dict[x]) 
		given_dict[x] = reciprocal(given_dict[x]) 
		given_dict[x] = str(given_dict[x]) 
		
		
	for x in given_dict: 
		val = given_dict[x]
		val = sympify(val) 
		val = reciprocal(val) 
		val = '(' + str(val) + ')'
		given_dict[x] = val
		
		
	if given_dict["a_2"] == "(1/x*y*z)": 
		d = str('(' + given_dict["a_n"] + '-' + given_dict["a_k"] + ')/(' + given_dict["n"] + '-' + given_dict["k"] + ')')
		d = simplify(sympify(d))
		given_dict["d"] = d
		
		
	formulas_dict = {
'n': str('((' + given_dict["a_n"] + '-' + given_dict["a_k"] + ')/(' + given_dict["d"] + '))+' + given_dict["k"]), 
'a_n': str(given_dict["a_k"] + '+(' + given_dict["d"] + '*' + given_dict["n"] + ')-(' + given_dict["k"] + '*' + given_dict["d"] + ')'), 
'a_k': str(given_dict["a_n"] + '-(' + given_dict["d"] + '*' + given_dict["n"] + ')+(' + given_dict["k"] + '*' + given_dict["d"] + ')')
}

	str_to_solve = formulas_dict[var_to_solve]
	
	to_solve = sympify(str_to_solve) 
	
	print(line) 
	print("Result:") 
	
	result = simplify(to_solve)
	
	if var_to_solve != 'n' and 'k':  
		result = reciprocal(result) 
		
	print("{} = {}".format(var_to_solve, result)) 
	print(line) 
	

calculate()
	
	
	
	
	
	
	
	
	
	