# bash ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/again.sh

function again { 
	read -p "Do you want to calculate again?
Please type Y for YES or N for NO.
[Default: NO]
" calc_again

calc_again=${calc_again:-"N"}

	calc_again=$(echo $calc_again | tr '[:lower:]' '[:upper:]')

	if [ $calc_again == 'Y' ]
			then
        		source ./calculate.sh
        		
    elif [ $calc_again == 'N' ]
       	then
				echo 'Babush!'
				
	else
		again
	fi
}
again
