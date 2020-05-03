# Calculators and Solvers for Math Teachers 

This repo is a collection of calculators and solvers for high school Math teachers like me. 

## Installation 
First, the Termux app must be installed in your Android phone. Learning some basic Linux commands such as ```pkg``` and ```cd``` is good but not required. 

### Algebra Solver 
To install the algebra solver: 
1. Copy and paste each line to Termux: 

```
cd ~

pkg upgrade

pkg install -y wget

wget https://cityofsmiles.github.io/install-algeb-solver-v2.sh

bash install-algeb-solver-v2.sh
```

2. Wait for it to finish, then restart Termux. 

3. After restarting, type
```algeb```
and hit Enter. 

That's it! 

To uninstall, copy and paste each line to Termux: 
```
cd ~

bash uninstall-algeb-solver-v2.sh
```

### Synthetic Calculator 
To install the synthetic calculator: 
1. Copy and paste each line to Termux: 

```
cd ~

pkg upgrade

pkg install -y wget

wget https://cityofsmiles.github.io/install-synthetic-calc.sh

bash install-synthetic-calc.sh
```

2. Wait for it to finish, then restart Termux. 

3. After restarting, type
```synth```
and hit Enter. 

To uninstall, copy and paste each line to Termux: 
```
cd ~

bash uninstall-synthetic-calc.sh
```

### Systems Solver 
To install the systems solver: 
1. Copy and paste each line to Termux: 

```
cd ~

pkg upgrade

pkg install -y wget

wget https://cityofsmiles.github.io/install-systems-solver.sh

bash install-systems-solver.sh
```

2. Wait for it to finish, then restart Termux. 

3. After restarting, type
```syst```
and hit Enter. 

To uninstall, copy and paste each line to Termux: 
```
cd ~

bash uninstall-systems-solver.sh
```

### Series Solver 
To install the Series solver: 
1. Copy and paste each line to Termux: 

```
cd ~

pkg upgrade

pkg install -y wget

wget https://cityofsmiles.github.io/install-semser-solver.sh

bash install-semser-solver.sh
```

2. Wait for it to finish, then restart Termux. 

3. After restarting, type
```semser```
and hit Enter. 

To uninstall, copy and paste each line to Termux: 
```
cd ~

bash uninstall-semser-solver.sh
```

### General Calculator
The General Calculator will install the four calculators. To install the General Calculator:  
1. Copy and paste each line to Termux: 

```
cd ~

pkg upgrade

pkg install -y wget

wget https://cityofsmiles.github.io/install-gen-cal.sh

bash install-gen-cal.sh
```

2. Wait for it to finish, then restart Termux. 

3. After restarting, type
```gcal```
and hit Enter. 

To uninstall, copy and paste each line to Termux: 
```
cd ~

bash uninstall-gen-cal.sh
```

## User's Manual
To use the algebra solver, the user must have a basic knowledge of representing the following in terms of LaTeX and/or SymPy: 

1. Fractions 
2. The four basic operations 
3. Exponentiation 

For example, to input the fraction 1/2, write: 
```\frac{1}{2}``` for LaTeX or
```1/2``` for SymPy. 

The user is highly encouraged to learn from various tutorials in the internet. The following links may help: 
- [SymPy](https://docs.sympy.org/latest/tutorial/index.html?fbclid=IwAR1FcACiWE5-2euNo5zEWuEZXWz7WeCQgt1h4aN9ymFlb55_vCspf_LpdzI#tutorial) 
- [LaTeX](https://www.overleaf.com/learn/latex/Fractions_and_Binomials) 
- [LaTeX Math Wiki](https://en.m.wikibooks.org/wiki/LaTeX/Mathematics) 
- [LaTeX Math Symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols) 


To use the series solver, the input must be in SymPy. 

To use the systems solver and the synthetic calculator, just follow the instructions. The prompts are pretty straight forward. 


## For Fedora Users
You may install the General calculator through: 
```
cd ~

wget https://cityofsmiles.github.io/fedora/install-gen-cal.sh

bash install-gen-cal.sh
```
To uninstall: 
```
cd ~

bash uninstall-gen-cal.sh
```


## Contact info
E-mail me at cityofsmiles at gmail dot com. 



