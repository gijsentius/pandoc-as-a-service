#!/bin/sh

sudo apt install texlive-full
sudo apt install openjdk-11-jre

wget https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb
sudo dpkg -i pandoc-2.14.1-1-amd64.deb

wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.0b/pandoc-crossref-Linux.tar.xz
tar -xf pandoc-crossref-Linux.tar.xz

wget https://github.com/citation-style-language/styles/archive/refs/heads/master.zip
unzip master.zip
mv styles-master/ styles/
rm master.zip

pip install -r req requirements.txt