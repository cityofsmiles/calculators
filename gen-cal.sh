#!/usr/bin/env bash
# bash /storage/emulated/0/GNURoot/home/Scripts/termux/calculators/gen-cal.sh

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app

#arg1="${1:-}"

cd $__dir 

function hori_line { 
printf "\n"
printf '=%.0s' $(seq 1 $(tput cols))
printf "\n"
}


function welcome { 
hori_line

echo "
Welcome to the General Calculator  
by Jonathan R. Bacolod  

Solve problems on algebraic expressions, linear equations, and polynomials. 

Enjoy!
"
hori_line
}
welcome

sleep 2

source ./choose_calc.sh

