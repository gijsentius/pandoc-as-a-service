# What is pandoc-as-a-service?

This is a personal project to be able to generate a pdf from a markdown file. In the future I may modify the service to be more generic.

## Used platform

When choosing to host this service manually 

## Pandoc command used

pandoc ${input} -o ${output} -F pandoc-crossref -F pandoc-citeproc -F plantuml/plantuml.py --template eisvogel --csl=ieee.csl