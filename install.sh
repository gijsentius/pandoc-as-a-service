#!/bin/sh

sudo apt update

sudo apt install texlive-full -y
sudo apt install openjdk-11-jre -y
sudo apt install build-essential -y
sudo apt install npm -y
sudo apt install python3-venv -y

npm install -g npm@latest

wget https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb
sudo dpkg -i pandoc-2.14.1-1-amd64.deb

wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.0b/pandoc-crossref-Linux.tar.xz
tar -xf pandoc-crossref-Linux.tar.xz

wget https://github.com/citation-style-language/styles/archive/refs/heads/master.zip
unzip master.zip
mv styles-master/ styles/
rm master.zip

python3 -m venv venv
shopt -s expand_aliases
alias python='venv/bin/python3'
alias pip='venv/bin/pip'
pip install -r req requirements.txt

mkdir temp
mkdir output
mkdir $HOME/.pandoc-crossref

cp resources/crossref-config.yaml $HOME/.pandoc-crossref/config.yaml