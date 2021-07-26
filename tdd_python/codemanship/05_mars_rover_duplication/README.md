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

