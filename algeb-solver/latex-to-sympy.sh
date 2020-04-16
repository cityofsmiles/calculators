#!/usr/bin/bash

# bash ~/storage/emulated/0/GNURoot/home/Scripts/fedora/calculator/latex-to-sympy.sh

str=$1
 
str=$(sed "s|\\\displaystyle||g" <<< $str)

str=$(sed 's|\\frac{|(|;s|}{|)/(|;s|}$|)|g;s|}(|))(|g' <<< $str)

str=$(sed 's|\\cdot||g' <<< $str)

str=$(sed 's|\\div|/|g' <<< $str)

str=$(sed 's|\\frac{|(|;s|}{|)/(|;s|}$|)|g;s|}(|))(|g' <<< $str)

str="${str// /}"

for letter in {a..z}
do
str="${str//"${letter}"/\*"${letter}"}"
done


#str=$(sed "s|\^{|**(|g" | sed "s|\^|**|g" | sed "s|{|(|g" | sed "s|}|)|g" | sed "s|(|*(|g" | sed "s|^\\*||g" | sed "s|-\\*|-|g" | sed "s|(\\*|(|g" | sed "s|\\+\\*|+|g" |sed "s|/\\*|/|g"| sed "s|[ ]\\*| |g" | sed "s|\\*\\*\\*|**|g" | sed "s|/\\*|/|g" | sed "s|,\\*|,|g" <<< $str)

echo $str |sed "s|\^{|**(|g" | sed "s|\^|**|g" | sed "s|{|(|g" | sed "s|}|)|g" | sed "s|(|*(|g" | sed "s|^\\*||g" | sed "s|-\\*|-|g" | sed "s|(\\*|(|g" | sed "s|\\+\\*|+|g" |sed "s|/\\*|/|g"| sed "s|[ ]\\*| |g" | sed "s|\\*\\*\\*|**|g" | sed "s|/\\*|/|g" | sed "s|,\\*|,|g" 

#str=$(echo $str |sed "s|\^{|**(|g" | sed "s|\^|**|g" | sed "s|{|(|g" | sed "s|}|)|g" | sed "s|(|*(|g" | sed "s|^\\*||g" | sed "s|-\\*|-|g" | sed "s|(\\*|(|g" | sed "s|\\+\\*|+|g" |sed "s|/\\*|/|g"| sed "s|[ ]\\*| |g" | sed "s|\\*\\*\\*|**|g" | sed "s|/\\*|/|g" | sed "s|,\\*|,|g") 

#export str

#function print_myvar() {
#echo "string = str(\"$str\")" > "sympy-string.txt"
#echo "\"$str\"" > "sympy-string.txt"
#}

#print_myvar
