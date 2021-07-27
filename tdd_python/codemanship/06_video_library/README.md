### TDD in Python #6 - Scaling TDD with Stubs and Mocks
https://www.youtube.com/watch?v=L2Gtln3IokQ

#### Task
Testing the functionality of adding a movie to the movie library
where when it is added using the IMDB id, it actually looks up the
information about the movie using the IMDB API and adds that to the movie
when it is added to the library. When a new movie is added to the library,
an email has to be sent to the memebers to tell them about the new library

We don't want to write a test that connects to the actual IMDB api because
that slows us down and makes the test more complex

Hence we use a test double called a stub

A test double is an object that is used by the object
of the function that we are testing that for whatever reason
is not the real thing. Typically they are used to stand in
place for exernal dependencies like databases and web services

A test double is something that returns test data from the outside.
It looks like the real source of information but it is dummy data
for the purposes of test. We can set it to what we expect to receive
from the actual API on deploymentt

Since we pass data from the Stub into our test, this is a form of
dependency injection. 

The core idea behind the stub is that it allows us to test the logic 
of the program without directly involving external dependencies from
databases and/or web service APIs

Dummies are a related concept. Basically need to put something in a certain place
where it can't be blank. Typically None is passed if it is not being used and if
being used a Null Object is passed which typically has the interface of the object
but doesn't do anything. 

Another reason for using stub is when data is chaning as in data driven logic and 
also for random data

Another benefit is that the code to connect to an API or database has not been written yet. 
So these stubs are kinda like faking it till we make it. This allows us to break our 
code into meaningful chunks and hence can test one part before worrying about the next part.
This leads to good separation of concerns

For instance we can inject different kinds of stubs into our dependency and hence it gives
us a lot more flexibility. The stubs are not just useful for writing unit tests, they are
useful in creating clean separation of concerns for example between problem of 
adding movies to the library and the problem of fetching information from IMDB. We don't
need to know how the process of fetching information from IMDB looks like, but we know
what the data recevied from IMDB looks like and needs to be like for our code to work

In the Jigsaw analogy, we haven't gotten the actual piece yet, but we have defined the 
outline and the shape of the piece yet

There is another scenario where we might have an external dependency but no data is being
returned. For these cases the concern is on whether or not the message was sent. This
is where we need MockObjects. 

A MockObject is an object that allows us to test whether an interaction between two objects
takes place. We mock individual methods of that object, so that when that method is called, 
it will remember what parameter values it was called with so that we can assert later if it 
was called correctly

A MockObject lets us test if a method was called and if it was called correctly
This lets us design the interaction from the outside. It is an external dependency
and we define what the external dependency looks like

Stubs are used for faking queries to external dependencies
Mocks are used for testing commands to external dependencies

Design and mocks come at a price. The reduce encapsulation of internal design
when you mock and stub everything. What we are saying in our tests here is that
a library needs to speak to an inflow source or an email system. These are designs 
of the internal library. If you stub and mock every dependency then every method is exposed. 
Then your tests know too much about the design and what is talking to what etc. 
Find a healthy balance

What works is to chunk up the design into different parts like a part that sends email, 
the part that fetches information from IMDB, the part that knows who the members are,
so you modularize into bigger chunks something like internal microservices which might end 
up involving a number of classes and a bunch of methods that all interact together 
all for specific intent and that internal microservice would have its own set of tests.

When the test knows too much about the internal design which happens when testing every
single method, then changing the design is really hard without breaking the tests.

A good analogy is about detecting gas leak at home. You might know from a measurement
outside the home that there is a gas leak in the house. But from that information,
you do not know which pipe has the gas leak. Now it does not make sense to have 
measurements on every pipe in the house, but it would be nice if every room had a 
measurement so that atleast you know which room in the house has the problem 
which greatly narrows down the domain of pipes which you have to search to detect
a problem. Similary you don't want tests that are only outside the house. 

It is also really powerful when writing code to address one responsibility and one
requirement at a time. We mock and fake the other dependencies until we get to actually
coding the dependency. We just define what the interactions need to look like from the
outside. 

