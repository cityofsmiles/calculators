#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/arith_seq.py

def calculate():
	
	vars_dict = {'1': 'a_1', '2': 'n', '3': 'd', '4': 'a_n', '5': 'a_k', '6': 'k'}
	
	def get_input():
		global var_to_solve_key
		var_to_solve_key = str(input('''
Please type in the variable to be solved.
1 for 'a_1'
2 for 'n'
3 for 'd'
4 for 'a_n' [default]
5 for 'a_k'
6 for 'k'
''') or '4')  
	
		if int(var_to_solve_key) > 6:
			print(line) 
			print('''You have not typed a valid input.
Please choose a number from 1 to 6.
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
	
	print(line) 
	
	for x in given_dict: 
		given_dict[x] = str(input('''
Please type in the value for {}:
(Type enter if not given.)  
'''.format(x)) or "") 

	given_dict[var_to_solve] = "0"

	if given_dict["a_k"] == "" and given_dict["k"] == "" and var_to_solve != "a_1":
		given_dict["a_k"] = given_dict["a_1"] 
		given_dict["k"] = "1"
		
	for x in given_dict: 
		val = given_dict[x]
		val = '(' + val + ')'
		given_dict[x] = val
		
	formulas_dict = {
'a_1': str(given_dict["a_n"] + '-(' + given_dict["d"] + '*' + given_dict["n"] + ')+' + given_dict["d"]), 
'n': str('((' + given_dict["a_n"] + '-' + given_dict["a_k"] + ')/(' + given_dict["d"] + '))+' + given_dict["k"]), 
'd': str('(' + given_dict["a_n"] + '-' + given_dict["a_k"] + ')/(' + given_dict["n"] + '-' + given_dict["k"] + ')'), 
'a_n': str(given_dict["a_k"] + '+(' + given_dict["d"] + '*' + given_dict["n"] + ')-(' + given_dict["k"] + '*' + given_dict["d"] + ')'), 
'a_k': str(given_dict["a_n"] + '-(' + given_dict["d"] + '*' + given_dict["n"] + ')+(' + given_dict["k"] + '*' + given_dict["d"] + ')'), 
'k': str('((' + given_dict["a_k"] + '-' + given_dict["a_n"] + ')/(' + given_dict["d"] + '))+' + given_dict["n"])
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