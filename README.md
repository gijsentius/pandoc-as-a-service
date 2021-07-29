# What is pandoc-as-a-service?

This is a personal project to be able to generate a pdf from a markdown file. In the future I may modify the service to be more generic.

## Used platform

When choosing to host this service manually 

## Pandoc command used

pandoc ${input} -o ${output} -F pandoc-crossref -F pandoc-citeproc -F plantuml/plantuml.py --template eisvogel --csl=ieee.csl

pandoc /home/gijs/Projects/pandoc-as-a-service/temp/test/test.md -o /home/gijs/Projects/pandoc-as-a-service/output/test.pdf -F pandoc-crossref --citeproc -F /home/gijs/Projects/pandoc-as-a-service/resources/plantuml/plantuml.py --template eisvogel-default --csl=styles/ieee.csl

pandoc /home/gijs/Projects/pandoc-as-a-service/example.md -o /home/gijs/Projects/pandoc-as-a-service/output/example.pdf -F pandoc-crossref --citeproc -F pandoc-plantuml --template eisvogel-default --csl=styles/ieee.csl