### Assert first and see the Test Fail

Coding along to second video in series - https://www.youtube.com/watch?v=oF5jTHSV28s

Making a DVD Library where community members can donate DVDs to the library.
When a DVD is donated, that movie needs to be added to the catalouge
Register a single rental copy so that people can borrow it. 

#### Learnings

1. Write the assertion first and work backwards to the setup so that 
you end up with the setup you need to ask the question being tested for

2. Run the test and see that it does fail which means that you'll have to 
have enough implementation to see that the test assertion fails. But only just enough

3. Do the simplest thing you can to pass the test

4. Refactor the code if needed

5. As much as possible a test should test for a single assertion so that it is clear
when a test fails what caused the issue. If a test contains multiple assertions, then it is 
extra work to figure out which of the issues that could fail a test actually failed the test

