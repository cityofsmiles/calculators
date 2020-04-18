function hori_line { 
printf "\n"
printf '=%.0s' $(seq 1 $(tput cols))
printf "\n"
}

function choose_again { 

__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd $__dir 

	hori_line
	
	read -p "Do you want to use another calculator?
Please type Y for YES or N for NO.
[Default: NO]
" choose_again

choose_again=${choose_again:-"N"}

	choose_again=$(echo $choose_again | tr '[:lower:]' '[:upper:]')

	if [ $choose_again == 'Y' ]
			then
				hori_line
				cd $__dir 
        		source ./choose_calc.sh
        		
    elif [ $choose_again == 'N' ]
       	then
				hori_line
				echo 'Babush!'
				
	else
		hori_line
		choose_again
	fi
}

choose_again

