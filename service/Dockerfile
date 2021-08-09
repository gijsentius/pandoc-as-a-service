FROM ubuntu:20.04

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TERM=dumb

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install apt-utils wget xz-utils unzip git openjdk-11-jre build-essential python3-venv -y

WORKDIR /home

RUN mkdir /home/pandoc

RUN mkdir -p temp && \
    mkdir -p output && \
    mkdir -p /home/.pandoc-crossref && \
    mkdir -p /home/.pandoc/templates

RUN wget https://github.com/jgm/pandoc/releases/download/2.14.1/pandoc-2.14.1-1-amd64.deb -q --output-document=/home/pandoc.deb && dpkg -i pandoc.deb && rm pandoc.deb

RUN wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.0b/pandoc-crossref-Linux.tar.xz -q --output-document=/home/pandoc-crossref-Linux.tar.xz && tar -xf pandoc-crossref-Linux.tar.xz && rm pandoc-crossref-Linux.tar.xz

RUN wget https://github.com/citation-style-language/styles/archive/refs/heads/master.zip -q --output-document=/home/master.zip && unzip master.zip && mv styles-master/ styles/ && rm master.zip

RUN wget https://netcologne.dl.sourceforge.net/project/plantuml/plantuml.jar -q --output-document=/opt/plantuml.jar
ENV PLANTUML_JAR=/opt/plantuml.jar

RUN apt-get update -q && \
    apt-get install -qqy -o=Dpkg::Use-Pty=0 --no-install-recommends texlive-full

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python3 get-pip.py

COPY requirements.txt .

RUN pip install wheel

RUN pip install -r requirements.txt

COPY resources resources
COPY resources/crossref-config.yaml /home/.pandoc-crossref/config.yaml
COPY resources/templates/* /home/.pandoc/templates/
COPY resources/plantuml/plantuml /usr/bin/plantuml

COPY app app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]