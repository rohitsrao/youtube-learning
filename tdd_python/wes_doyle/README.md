### Named Entity Finder being built using Test Driven Development with Python

This project was coded along to Wes Doyle's excellent tutorial on TDD with Python - https://www.youtube.com/watch?v=eAPmXQ0dC7Q

It accepts a string into the input and in response we get a visualisation of Named Entities

#### Python Modules used
- selenium
- spacy (Natural Language Processing)
- flask
- pytest

### Learning

While TDD is extremely useful as a practice to write testable code and building designs, 
it isn't going to make design descisions for you. You can write bad code with TDD it is just
far less likely.

Dependency Inversion
Instead of having NamedEntityClient depend on the spacy language model say by loading the spacy
model each time an object of NamedEntityClient is created, we instead create an abstraction
and have NamedEntityClient depend on that abstraction so that it gives us freedom to change the 
dependency say if we wanted to use another language model etc
