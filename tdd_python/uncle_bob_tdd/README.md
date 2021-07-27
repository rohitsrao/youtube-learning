### Test Driven Development - Uncle Bob

Three Rules of Test Driven Development

1. You are not allowed to write any production code until you have first written
a test that fails because the production code does not exist

2. You are not allowed to write more of a test than is sufficient to fail and not
compiling is failing. 

3. You are not allowed to write any more production code than is sufficient to pass
the currently failing test

You already know what you are going to write. Just write a test that will fail
if you don't have what you are going to write

It might feel like you are introducing bugs into your code and you are. You are 
only writing code that passes your test and not the actual functionality.
So the question you have to now ask yourself is what test do I have to write that
shows that the current code is a bug. Write that and then modify the code to pass.

It is a good idea to not write tests directly for what you are building. 
Do not go for the gold immedialtey. Lumber around. Think up different ways
to throw the code off and then finally you'll arrive at the required code. 

Let the test guide your development! So instead of asking what should I code next,
you have to ask what should I test next! Think of intelligent tests
