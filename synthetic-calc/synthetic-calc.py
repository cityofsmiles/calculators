#!/usr/bin/python

# python /storage/emulated/0/GNURoot/home/Scripts/termux/synthetic-calc/synthetic-calc.py

import os
columns, rows = os.get_terminal_size(0)

global line
line = "\n" + ("=" * columns) + "\n"

def welcome():
    print(line) 
    print('''
Welcome to Synth-Div Calc
by Jonathan R. Bacolod  

Quickly solve polynomials using the 
synthetic division method.

Take note that the polynomials should be
in standard form. 

Enjoy! 
''')
    print(line) 
welcome() 


def get_coefficients():
    global firstRow
    global num_elements
    coefficients = str(input('''
Please type in the numerical coefficients of 
the polynomial separated by comma: 
''')) 
    firstRow = list(coefficients.split(","))
    firstRow = [int(i) for i in firstRow]
    num_elements = len(firstRow)

get_coefficients()

def calculate():
	from fractions import Fraction as frac
	divisor = input('''
Please type in the constant divisor: 
''')
	global thirdRow
	divisor = frac(divisor) 
	secondRow = list()
	thirdRow = list()
	secondRow.insert(0, 0)
	thirdRow.insert(0, firstRow[0])
	for x in range(1, num_elements):
		y = x - 1
		product = divisor * float(thirdRow[y]) 
		product = float(product) 
		secondRow.insert(x, product)
		sum = float(firstRow[x])  + float(secondRow[x]) 
		#sum = frac(sum) 
		thirdRow.insert(x, sum)

# Print results. 
	hori_line = str("-" * ((5 * num_elements) + 4)) 
	result_1 = [firstRow, secondRow]
	result_2 = [thirdRow]
	print(line) 
	print("Result:") 
	print(divisor) 
	print('\n'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in result_1]))
	print(hori_line) 
	print('\n'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in result_2]))
	print(line) 
	

calculate()

def again():
    calc_again = input('''
What do you want to do next?
1 Try another constant divisor [default]
2 Continue dividing
3 Enter new numerical coefficients 
4 Quit computing 
''') or "1"

    if calc_again == '1':
        calculate()
    elif calc_again == '2':
        global firstRow
        global num_elements
        if thirdRow[-1] == 0: del thirdRow[-1] 
        firstRow = thirdRow
        num_elements = len(firstRow)
        calculate()
    elif calc_again == '3':
        get_coefficients()
        calculate()
    elif calc_again == '4':
        print(line) 
        print('Babush!')
    else:
        print(line) 
        again()

again()