#!/usr/bin/python 

# python /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/semser_solver/fib_seq.py

def calculate():
	prob = int(input('''
What do you want to do? 
1 Find the next terms [default]
2 Find the nth term
''') or 1) 

	print(line) 
	
	from sympy import sympify, simplify
	
	if prob == 1: 
		a_1 = str(input('''
Please type in the value of the first term: 
''')) 
		a_2 = str(input('''
Please type in the value of the second term: 
''')) 
		n = int(input('''
Please type in the number of next terms: 
''')) 
		
		def next_terms(first, second, n):
			num = int(n + 2)
			a = sympify(first)
			b = sympify(second)
			print("a_1 =", a) 
			print("a_2 =", b) 
			for i in range(3, int(num+1)):
				c = b
				b =  simplify(a + b) 
				a = c
				term = "a_" + str(i) 
				print("{} = {}".format(term, b)) 

		print(line) 
		print("Result:") 
		next_terms(a_1, a_2, n)
		print(line) 

	elif prob == 2: 
		a_1 = str(input("a_1 = ")) 
		a_2 = str(input("a_2 = ")) 
		n = int(input("n = ")) 

		def find_term(first, second, n):
			a = sympify(first)
			b = sympify(second)
			count = 1
			while (count < n):
				c = b
				b =  simplify(a + b) 
				a = c
				count = count + 1
			term = "a_" + str(count) 
			print("{} = {}".format(term, c)) 

		print(line) 
		print("Result:") 
		find_term(a_1, a_2, n)
		print(line) 

	else: 
		print(line) 
		print('''You have not typed a valid input.
Please run the program again.''')
		return
	
calculate()
	