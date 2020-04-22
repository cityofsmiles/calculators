#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/geom_seq.py

def calculate():
	vars_dict = {'1': 'a_1', '2': 'r', '3': 'n', '4': 'a_n', '5': 'a_k', '6': 'k'}
	
	var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'a_1'
2 for 'r'
3 for 'n'
4 for 'a_n' [default]
''') or '4') 

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

	given_dict[var_to_solve] = "0"
	given_dict['n-1'] = int(given_dict['n']) - 1
	given_dict['n-1'] = str(given_dict['n-1']) 
	
	if given_dict["a_k"] == "" and given_dict["k"] == "" and var_to_solve != "a_1":
		given_dict["a_k"] = given_dict["a_1"] 
		given_dict["k"] = "1"
	
	for x in given_dict: 
		val = given_dict[x]
		val = '(' + val + ')'
		given_dict[x] = val
		
	formulas_dict = {
'a_1': str(given_dict["a_n"] + '/(' + given_dict["r"] + ')**' + given_dict['n-1']), 
'r': str('(' + given_dict["a_n"] + '/' + given_dict["a_k"] + ')' + '**(1/' + '(' + given_dict["n"] + '-' + given_dict["k"] + '))'), 
'n': str('log((' + given_dict["a_n"] + '*' + given_dict["r"] + '/' + given_dict["a_1"] + ')' + ', ' + given_dict["r"] + ')'), 
'a_n': str(given_dict["a_1"] + '*(' + given_dict["r"] + ')**' + given_dict['n-1']) 
}

	str_to_solve = formulas_dict[var_to_solve]
	
	from sympy import sympify
	from math import log
	to_solve = sympify(str_to_solve) 
	
	print(line) 
	print("Result:") 
	from sympy import simplify
	result = simplify(to_solve)
	print("{} = {}".format(var_to_solve, result)) 
	print(line) 








	
	
	
	
	
	
	
	
calculate()