### TDD in Python #4 - Duplication & The rule of three
https://www.youtube.com/watch?v=f6KHs4aMPpU

Scenario
-------
Complete scenario can be found at https://kata-log.rocks/mars-rover-kata

Learning
--------

1. Eliminating duplication lends itself to figuring out generalisations 
and abstractions in our code. The design emerges from elimnating duplication

2. There is a danger in refactoring duplciation too early and that is 
that we end up introducing a wrong abstraction

3. The Rule of Three is a guideline that on average wait to see at least 3 duplications
before refactoring the code

4. Naturally the longer you wait to refactor the more time it takes to refactor
and hence you tend to not do it

5. Test code needs to be maintained just like source code

6. parameterized.expand takes an array of tuples with each tuple containing test
data for each test case

When is duplication not removed ?
--------------------------------

Avoid overloading a testcase with multiple behaviours. 
Each behaviour should have separate test.
Haing one test for more than one behaviour can make it difficult to maintain and follow
as code grows larger

If after eliminating duplication the refactored code is hard to read,
then you go back and leave the duplication in
