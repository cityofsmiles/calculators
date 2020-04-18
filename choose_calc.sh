function choose_calc { 

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd $__dir 

read -p "
Please type in the calculator you want to use:
1 for SymPyTeX Algebra Solver [default]
2 for Synthetic Division Calculator 
3 for System of Linear Equations Solver 
"  calc_type

calc_type=${calc_type:-1}

if [ $calc_type -eq "1" ]
	then
		cd ./algeb-solver-v2
		python algeb-solver-v2.py
		
	elif [ $calc_type -eq "2" ]
	then
		cd ./synthetic-calc
		python synthetic-calc.py
		
	elif [ $calc_type -eq "3" ]
	then
		cd ./systems-solver
		python systems-solver.py
		
	else
		echo "You have not typed a valid input.
Please run the program again."
		exit 1
fi

cd $__dir 

source ./choose_again.sh
}

choose_calc