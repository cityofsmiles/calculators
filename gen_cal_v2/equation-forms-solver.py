#!/usr/bin/python

# python /home/jonathan/slope-solver/slope-solver.py


import os
columns, rows = os.get_terminal_size(0)

cur_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(cur_dir)

line = "\n" + ("=" * columns) + "\n"

def welcome():
	print(line) 
	print('''
Welcome to the Equation Forms Solver 
by Jonathan R. Bacolod  

Quickly find the equation of a line
based on given information. 

Enjoy! 
''')


def choose_form():
	form_type = int(input('''
Please type in the form of equation you want to use:
	
1 for Point-Slope Form [default]
2 for Two-Point Form
3 for Two-Intercept Form 
4 for Slope-Intercept Form
5 for Standard Form
''') or 1) 

	form_list = ['point-slope-form', 'two-point-form', 'two-intercept-form', 'slope-intercept-form', 'standard-form']
	
	if form_type > len(form_list):
		print(line) 
		print('''You have not typed a valid input.
Please run the program again.''')
		return
		

	for i in range(0, len(form_list)):
		k = i + 1
		if form_type == k:
			file = form_list[i] + ".py"
			exec(open(file).read())
			os.chdir(cur_dir)			
	

def choose_other_form():
		print(line) 
		choose_again = input('''
Do you want to solve another form of equation?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N"

		if choose_again.upper() == 'Y':
			print(line) 
			choose_form()
            
		elif choose_again.upper() == 'N':
			print(line) 
			print('Exiting.')
             
		else:
			print(line) 
			choose_again()


if __name__ == '__main__':
	welcome()
	choose_form()
	choose_other_form()
