#!/usr/bin/env bash

# bash ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/calculator.sh 
# bash ~/storage/emulated/0/GNURoot/home/Scripts/termux/algeb-solver/algeb-solver.sh 

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

#echo $__dir

cd $__dir

function welcome { 
printf '=%.0s' $(seq 1 $(tput cols))
echo "
Welcome to SymPyTeX Algebra Solver 
by Jonathan R. Bacolod  

Solve problems on algebraic expressions 
and polynomials. 

Input and output can be written using
LaTeX or SymPy. 

Enjoy!
"
printf '=%.0s' $(seq 1 $(tput cols))
}
welcome

sleep 2

source ./calculate.sh