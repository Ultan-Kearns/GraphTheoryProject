#  3rd Year GraphTheoryProject - Ultan Kearns G00343745
## How to use this application
This project can be run as follows from the command line "python regex.py" ommitting the quotes.
The main class regex is the class which will call post.py which will convert prefix to postfix,
the other class operators.py will return to the user the result of the regex expression and how many
times it occurs in a given string.  This program will only work with an alphabet of 1s and 0s as per the 
project specification.

## Architecture
I decided to take an OOP(Object oriented programming) approch to the project and separate each of the 
functions performed into it's own class to reduce the project's complexity.

1. Regex Main Class - Base class of project, this class will be called during the initialization of the project.
2. Postfix class - This class will be called when the user enters the regex expression as input in the main class
the regex expression is passed as an argument to the function located in the postfix class.  The parse function
will return the regex string as postfix.
3. Operators Class - This class will perform operations in the regex string and then tell the user how many times it 
has matched the regex expression depending on operator for example 1 0 * meaning 0 or more ones or 0s will return 2 for string
"1 0". This class contains only one function which is called in postfix and takes the operators from postfix string as an argument.

## Bugs in project so far
+ None so far as I am aware currently

## What I learned from this project
+ The syntax for regular expressions
+ How a regex engine works
+ How to understand the internals of the engine 
+ How to break a complex problem into smaller problems
+ Different ways of thinking about the problem

## Resources for research of project
+ https://en.wikipedia.org/wiki/Regular_expression - This resource details what a regular expression is essentially
+ https://www.regular-expressions.info/engine.html - This resource breaks down the internals of a regex engine
+ https://www.princeton.edu/~mlovett/reference/Regular-Expressions.pdf
+ https://medium.com/@DmitrySoshnikov/building-a-regexp-machine-part-1-regular-grammars-d4986b585d7e - This resource goes over regular grammars
+ https://medium.com/@DmitrySoshnikov/building-a-regexp-machine-part-2-finite-automata-nfa-fragments-5a7c5c005ef0 - This is essentially part two of above resource
+ https://www.goodreads.com/book/show/388049.Introduction_to_Graph_Theory - This resource goes over the theory behind Graph theory which I thought would be useful for this module(Highly recommended book)
+ https://en.wikipedia.org/wiki/Thompson's_construction - This resource defines the implementation of thompsons construction and describes the theory behind it
+ https://en.wikipedia.org/wiki/Infix_notation - Explains what infix notation is and also how it differs from postfix
+ Course Materials