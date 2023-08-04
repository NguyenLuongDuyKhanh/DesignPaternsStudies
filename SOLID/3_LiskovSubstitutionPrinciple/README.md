"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."[8] See also design by contract.[8]

Take Ex1_lsp.py as an example, we are gonna make a class represent for rectangle and it is able to calculate area of its instances.
Class Square is inherite from class Rectangle because squares are special Rectangle with width=height
Function use_it take an object (aka pointers or references) of Rectangle, which is base class, works well with Rectangle but does not work with Square objects, look at width and height properties.
=> It violates LSP.

Solution: dont use two seperated classes
