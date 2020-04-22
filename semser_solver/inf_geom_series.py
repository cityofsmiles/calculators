 #!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/inf_geom_series.py

def calculate():
	vars_dict = {'1': 'S', '2': 'a_1', '3': 'r'}
	
	var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'S' [default]
2 for 'a_1'
3 for 'r'
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

	from sympy import sympify, simplify
	given_dict[var_to_solve] = "0"
	given_dict['1-r'] = simplify(1- sympify(given_dict['r'])) 
	given_dict['1-r'] = str(given_dict['1-r']) 
	
	for x in given_dict: 
		val = given_dict[x]
		val = '(' + val + ')'
		given_dict[x] = val
	
	formulas_dict = {
'S': str('(' + given_dict["a_1"] + ')/' + given_dict['1-r']), 
'a_1': str(given_dict["S"] + '*' + given_dict['1-r']), 
'r': str('(' + given_dict["S"] + '-' + given_dict["a_1"] + ')/' + given_dict["S"])
}

	str_to_solve = formulas_dict[var_to_solve]
	
	to_solve = sympify(str_to_solve) 
	from math import log
	print(line) 
	print("Result:") 
	result = simplify(to_solve)
	print("{} = {}".format(var_to_solve, result)) 
	print(line) 


calculate()