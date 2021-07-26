### TDD in Python #3 - What test should we write ?
https://www.youtube.com/watch?v=Ji2KKShNKic

Focus
-----

What are meaningful tests ?!
Differnce between test driven design and design driven testing
How writing lists of tests before writing code can help guide the process

Scenario
-------
Customers can buy CDs directly from warehouse.
Record labels send batches of CDs to warehouse
Customers can only order titles in stock

Learnings
---------

1. TDD does not mean that you do not pay attention to the design

2. But paying too much attention upfront to the design can lead to design
driven testing where you end up looking at a design and asking what tests
do I need to write for this design. This is thinking it the wrong way around.
Design driven thinking looks like writing tests for constructors and every method
from the preconceived idea of what the design should be

3. With TDD, as the name suggests, we should come up with the simplest design
that passes our tests

4. Good to think about the design but not get too attached to it. 

5. Think more in useful outcomes rather than the design.
Test should be based on what things the customer or end user wants from the software.
Class methods are consequences of some useful outcomes to the customer. 
i.e Customer wants to know CD stock count so you end up with CD.getStockCount()

6. Read the requirements and think about testcases

7. As you are writing the tests, you have to consider design questions like
okay I do need a method that returns the stock count for a cd. As much as possible
let the test making the decisions about the details of the design that we need. As much as possible
let the test making the decisions about the details of the design that we need

8. For trivial test cases, it makes sense to directly write the generalised production code
instead of writing only the code that will pass the current test and then writing one more specific code
that would then generalise the production code. The judgement of when to skip comes with experience.
Important to factor in your overestimation of how simple the code is when you make this leap.

9. Does writing this test bring more value ?! Does it make sene to write a test for every constructor
and getter and setter ?!

10. Write meaningful tests that end users or customers actually care about. Good to think about 
design upfront but don't get too attached to that design. The design should emerge organically
from good test cases. Listing tests from requirements can be super helpful in writing code. 
Sometimes when the implementation is obvious, it is okay to make a leap and directly write the 
generalised code

Requirements 
-----------

Requirements are reformulated as outcomes that design must achieve
What is the software got to do. 
Don't focus too much on design when writing requirements
What the software must do gives us the test cases that we must handle

Buy a CD
* In Stock - quantity bought deducted from stock
* Insufficient stock - raise an exception

Searching for a CD
* if in catalogue - return the matching CD
* if not in catalouge - return null

Receiving batch of CDs
* Copies of 1 CD in catalouge - add copies to each CD
* Copies of CDs not in catalouge - CD added to catalouge with copies
* Batch of multiple CDs - add any missing CDs to catalouge, add copies to each CD

Once you have written down the requirements, you start thinking of a failing test 
for each requirement. 
