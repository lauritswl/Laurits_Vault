# Quick overview of type
#✏️Meta-Studying 

| Type     | Aliases                     |
| -------- | --------------------------- |
| note     | note, seealso               |
| abstract | abstract, summary, tldr     |
| info     | info, todo                  |
| tip      | tip, hint, important        |
| success  | success, check, done        |
| question | question, help, faq         |
| warning  | warning, caution, attention |
| failure  | failure, fail, missing      |
| danger   | danger, error               |
| bug      | bug                         |
| example  | example                     | 
| quote    | quote, cite                 |

## **Template of an admonition**
````markdown
```ad-<type> # Admonition type. See below for a list of available types.
title:                  # Admonition title.
collapse:               # Create a collapsible admonition.
icon:                   # Override the icon.
color:                  # Override the color.

!!! ad-note
    title: This admonition is nested.
    This is a nested admonition!



Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```
````

## Visualization

```ad-note
Aliases:  note, seealso 
```
```ad-abstract
Aliases:  abstract, summary, tldr 
```
```ad-info
Aliases:  info, todo  
```
```ad-tip
Aliases:  tip, hint, important  
```
```ad-success
Aliases:  success, check, done  
```
```ad-question
Aliases:  question, help, faq  
```
```ad-warning
Aliases:  warning, caution, attention
```
```ad-failure
Aliases: failure, fail, missing 
```
```ad-danger
Aliases:  danger, error
```
```ad-bug
Aliases:  bug
```
```ad-example
Aliases:  example
```
```ad-quote
Aliases:  quote, cite    
```
```ad-tip
How to nest a file using python markdown
!!! ad-note
    title: This admonition is nested.
    This is a nested admonition!

```