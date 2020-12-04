 #!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/fin_geom_series.py

def calculate():
	vars_dict = {'1': 'S_n', '2': 'a_1', '3': 'r', '4': 'n', '5': 'a_n'}
	
	def get_input():
		global var_to_solve_key
		var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'S_n' [default]
2 for 'a_1'
3 for 'r'
4 for 'n'
5 for 'a_n' 
''') or '1') 

		if int(var_to_solve_key) > 5:
			print(line) 
			print('''You have not typed a valid input.
Please choose a number from 1 to 5.
''')
			print(line) 
			get_input()

	get_input()

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
	
	given_dict['r^n'] = simplify(sympify((given_dict['r']))**(sympify(given_dict['n']))) 
	given_dict['r^n'] = str(given_dict['r^n']) 
	
	for x in given_dict: 
		val = given_dict[x]
		val = '(' + val + ')'
		given_dict[x] = val
	
	formulas_dict = {
'S_n': str('(' + given_dict["a_1"] + '-' + given_dict["a_1"] + '*' + given_dict['r^n'] + ')/' + given_dict['1-r']), 
'a_1': str(given_dict["S_n"] + '*' + given_dict['1-r'] + '/(1-' + given_dict['r^n'] + ')'), 
'r': str('(' + given_dict["S_n"] + '-' + given_dict["a_1"] + ')/(' + given_dict["S_n"] + '-' + given_dict["a_n"] + ')'), 
'n': str('log((' + given_dict["a_1"] + '-' + given_dict["S_n"] + '*' + given_dict['1-r'] + ')/' + given_dict["a_1"] + ', (' + given_dict["r"] + '))'), 
'a_n': str('(' + given_dict["a_1"] + '-' + given_dict["S_n"] + '*' + given_dict['1-r'] + ')/(' + given_dict["r"] + ')') 
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