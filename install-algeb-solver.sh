#!/data/data/com.termux/files/usr/bin/sh

cd ~

wget https://github.com/cityofsmiles/calculators/raw/master/algeb-solver.zip

unzip ./algeb-solver.zip

echo "alias algeb='bash ~/algeb-solver/algeb-solver.sh'" >> ~/.bashrc

source ~/.bashrc
