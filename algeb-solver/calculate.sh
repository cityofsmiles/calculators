# bash ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/calculate.sh

function calculate { 

read -p "
Please type in the kind of input and output 
you will use:
1 for LaTeX --> LaTeX [default]
2 for LaTeX --> SymPy  
3 for SymPy --> LaTeX 
4 for SymPy --> SymPy
"  input_output

input_output=${input_output:-1}


if [ $input_output -eq "1" ]
	then
		input_type="LaTeX"
		output_type="LaTeX"
	elif [ $input_output -eq "2" ]
	then
		input_type="LaTeX"
		output_type="SymPy"
	elif [ $input_output -eq "3" ]
	then
		input_type="SymPy"
		output_type="LaTeX"
	elif [ $input_output -eq "4" ]
	then
		input_type="SymPy"
		output_type="SymPy"
	else
		echo "You have not typed a valid input/output expression.  
Please run the program again."
		exit 1
fi

read -p "
Please type in the operation you would like 
to complete:
1 for Cancel
2 for Expand
3 for Factor
4 for Simplify
5 for Find Roots 
6 for Solve 
" operation

# Get inputs. 
if [ $operation -eq "1" ]
	then
		read -p "
Please enter the first $input_type expression
(numerator):
" expr_1
		read -p "
Please enter the second $input_type expression
(denominator):
" expr_2

	elif [ $operation -ge "2" -a $operation -le "4" ]; 
	then
		read -p "
Please enter the $input_type expression:
" expr_1
		expr_2="0"
	
	elif [ $operation -eq "5" -o $operation -eq "6" ]; 
	then
		read -p "
Please enter the $input_type expression to be solved:
" expr_1
		read -p "
Please enter the variable to be solved:
" expr_2

	else
		echo "You have not typed a valid operation.  
Please run the program again."
		exit 2
fi

# Convert LaTeX expressions to SymPy
if [ "$input_type" == "LaTeX" ]
	then
		expr_1=$(sed 's|frac|\\frac|g' <<< $expr_1)
		expr_1="$(bash latex-to-sympy.sh "$expr_1")"
		
		if [ $expr_2 != "0" ]
			then
				expr_2=$(sed 's|frac|\\frac|g' <<< $expr_2)
				expr_2="$(bash latex-to-sympy.sh "$expr_2")"
		fi
fi
 
# Perform the selected operation. 
if [ $operation -eq "1" ]
	then 
		python ./cancel.py "$expr_1" "$expr_2" "$input_type" "$output_type"
fi

if [ $operation -eq "2" ]
	then 
		python ./expand.py "$expr_1" "$input_type" "$output_type"
fi

if [ $operation -eq "3" ]
	then 
		python ./factor.py "$expr_1" "$input_type" "$output_type"
fi

if [ $operation -eq "4" ]
	then 
		python ./simplify.py "$expr_1" "$input_type" "$output_type"
fi

if [ $operation -eq "5" ]
	then 
		python ./roots.py "$expr_1" "$expr_2" "$input_type" "$output_type"
fi

if [ $operation -eq "6" ]
	then 
		python ./solve.py "$expr_1" "$expr_2" "$input_type" "$output_type"
fi

if [ $operation -lt "1" -o $operation -gt "6" ]; 
	then
		echo "You have not typed a valid operator.  Please run the program again."
		exit 3
fi

source ./again.sh
}
calculate

