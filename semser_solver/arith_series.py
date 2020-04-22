#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/arith_series.py

def calculate():
	
	vars_dict = {'1': 'S_n', '2': 'a_1', '3': 'n', '4': 'd', '5': 'a_n'}
	
	var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'S_n' [default]
2 for 'a_1'
3 for 'n'
4 for 'd'
5 for 'a_n' 
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

	given_dict[var_to_solve] = "0"
	given_dict['n-1'] = int(given_dict['n']) - 1
	given_dict['n-1'] = str(given_dict['n-1']) 
	
	for x in given_dict: 
		val = given_dict[x]
		val = '(' + val + ')'
		given_dict[x] = val
	
# Choose formula for n. 
	if given_dict["d"] == "()":
		n_formula = str('2*' + given_dict["S_n"] + '/(' + given_dict["a_1"] + '+' + given_dict["a_n"] + ')') 
	elif given_dict["S_n"] == "()":
		n_formula = str('((' + given_dict["a_n"] + '-' + given_dict["a_1"] + ')/' + given_dict["d"] + ')+1') 
	else: 
		n_formula = "()"

	formulas_dict = {
'S_n': str('(' + given_dict["n"] + '/2)' + '*(2*' + given_dict["a_1"] + '+' + given_dict["n-1"] + '*' + given_dict["d"] + ')'), 
'a_1': str('(' + given_dict["S_n"] + '/' + given_dict["n"] + ')' + '-' + '(' + given_dict["n-1"] + '*' + given_dict["d"] + '/2)'), 
'n': n_formula, 
'd': str('(' + given_dict["a_n"] + '-' + given_dict["a_1"] + ')/' + given_dict["n-1"]), 
'a_n': str('(2*' + given_dict["S_n"] + '-' + given_dict["n"] + '*' + given_dict["a_1"] + ')/' + given_dict["n"]) 
}
	str_to_solve = formulas_dict[var_to_solve]
	
	from sympy import sympify
	to_solve = sympify(str_to_solve) 
	
	print(line) 
	print("Result:") 
	from sympy import simplify
	result = simplify(to_solve)
	print("{} = {}".format(var_to_solve, result)) 
	print(line) 

calculate()




