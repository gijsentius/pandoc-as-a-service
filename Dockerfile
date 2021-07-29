FROM ubuntu:20.04

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TERM=dumb

WORKDIR /home

RUN mkdir -p /usr/share/man/man1 && \
    mkdir -p temp && \
    mkdir -p output && \
    mkdir -p $HOME/.pandoc-crossref && \
    mkdir -p $HOME/.pandoc/templates && \
    mkdir -p $HOME/.local/share/plantuml

RUN wget https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb -q --output-document=/home/pandoc.deb && dpkg -i pandoc.deb && rm pandoc.deb

RUN wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.0b/pandoc-crossref-Linux.tar.xz -q --output-document=/home/pandoc-crossref-Linux.tar.xz && tar -xf pandoc-crossref-Linux.tar.xz && rm pandoc-crossref-Linux.tar.xz

RUN wget https://github.com/citation-style-language/styles/archive/refs/heads/master.zip -q --output-document=/home/master.zip && unzip master.zip && mv styles-master/ styles/ && rm master.zip

RUN wget https://netcologne.dl.sourceforge.net/project/plantuml/plantuml.jar -q --output-document=/home/plantuml.jar
ENV PLANTUML_JAR=/home/plantuml.jar

RUN apt-get update -q && \
    apt install -qqy -o=Dpkg::Use-Pty=0 --no-install-recommends git && \
    apt install -qqy -o=Dpkg::Use-Pty=0 --no-install-recommends texlive-full && \
    apt install -qqy -o=Dpkg::Use-Pty=0 ruby poppler-utils && gem install bundler

WORKDIR /workdir
