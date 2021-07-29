---
title: "Example title"
subtitle: "Example subtitle" 
date: \today

author: Gijs Entius

lang: nl-NL

titlepage: true
titlepage-rule-height: 0
titlepage-background: "backgrounds/example1.pdf"
titlepage-text-color: "FFFFFF" 
titlepage-rule-color: "FFFFFF"

informationpage: titelpage.tex

doublesided: true
toc: true
toc-depth: 3
toc-own-page: true
numbersections: true

listings: true
---

# Lorem Ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras elit tortor, pellentesque eu dictum ac, aliquet hendrerit justo. Quisque eget dolor enim. Fusce non hendrerit ipsum. Maecenas volutpat tortor sit amet ante facilisis fermentum. Curabitur vitae euismod tortor. Vivamus aliquam felis diam, vel rhoncus tortor laoreet ac. Aliquam erat volutpat. Nulla facilisi. Quisque et magna augue. Nam sed elit sagittis, scelerisque magna sagittis, placerat orci. Praesent sit amet suscipit eros. Morbi eget mollis leo. Maecenas metus tellus, suscipit nec blandit eget, volutpat vitae felis. Nam id purus nec nulla luctus ullamcorper. Proin lobortis urna dolor, et vulputate libero blandit eget. Nam sit amet lectus at odio ultricies mollis.  [@reference].

![Image description](image.jpg){#fig:image_reference}

# Chapter {#sec:chapter_example}

Aenean egestas tincidunt mi vitae viverra. Nulla ut fringilla felis, non finibus sapien. Suspendisse sed egestas diam, vitae pulvinar nibh. Donec purus erat, ornare non nunc id, bibendum mattis justo. Ut egestas euismod blandit. Etiam suscipit nulla nec elit tristique, quis accumsan ante auctor. Ut bibendum bibendum erat, sit amet efficitur ligula faucibus quis.

## Paragraph

Integer vel est id velit convallis sodales sed at turpis. In hac habitasse platea dictumst. Cras eleifend eleifend orci bibendum varius. Pellentesque nibh justo, pellentesque a auctor eget, lobortis quis nisl. Vestibulum ac sapien at tellus convallis ultricies. Vestibulum in volutpat felis. Quisque egestas ipsum congue luctus aliquam. Donec in fermentum metus, nec blandit dui. Nunc vehicula in est id lacinia. Donec a luctus mi. [website](https://www.example.com).

# PlantUML

```{.plantuml #fig:plantuml_fig caption="caption of plantuml fig" width=95%}
@startuml

@enduml
```

# Table

| Example | Column |
|-----------|----------|
| Example 1 | Column 1 |
| Example 2 | Column 2 |
| Example 3 | Column 3 |

Table: Example table caption. {#tbl:table reference}
