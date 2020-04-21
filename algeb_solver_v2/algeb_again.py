import os
columns, rows = os.get_terminal_size(0)


line = "\n" + ("=" * columns) + "\n"


def again():
		calc_again = str(input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: NO]
''') or "N") 

		if calc_again.upper() == 'Y':
			print(line) 
			from algeb_solver_v2 import calculate
			calculate()
			
		elif calc_again.upper() == 'N':
			print(line) 
			print('Babush!')
			return
			
		else:
			print(line) 
			again()