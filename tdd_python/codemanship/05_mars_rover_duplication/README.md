### TDD in Python #5 - Part 1 - Inside Out TDD
https://www.youtube.com/watch?v=FerGg9E3p1w

Inside Out TDD refers to tests driving the parts of our design.
Then the parts are put together like a jigsaw in the last step

One danger with this approach is that all the individual tests might
pass but you might overlook something when putting it all together

Using the inside out approach means it is great for pointing out
issues specifically so you do not spend too much time in the debugger

Draw back is that you might end up with the wrong pieces for you jigsaw
and you end up with test code that knows a lot about the internal design
so it makes it harder to refactor the code

### TDD in Python #5 - Part 2 - Outside In TDD

The outside in approach is about starting with the entry point and then
discovering behaviours and extractions.

The analogy would be to start with the overall picture and then cut up
the jigsaw pieces. This way the pieces of the jigsaw are guaranteed
to be fitting as they are cut from the whole rather than trying to 
fit them in as in the case of Inside In approach. Hence the pices are
guaranteed to fit together

Here the test only knows about the single entry point method instead 
of all the parts and hence it is much easier to refactor the code. Internal 
design is encapsulated and test code is more loosely coupled from production code

The drawback is that when something fails, you have to look a little further
to figure out which part of the design is going wrong. When large call stacks are
present in complex code, it can be disadvantageous to only have test running at the 
outermost level
