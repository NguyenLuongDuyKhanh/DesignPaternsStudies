"Clients should not be forced to depend upon interfaces that they do not use."[9][4]

Ex1:
OldFashionedPrinter cannot fax and scan. if somebody initialize an instance of OldFashionedprinter they see fax() and scan() in its properties, when they were called they do nothing, or worse, raise error -> crashed the application

=> instead of create the big interface: machine, keep things simple. Split Machine to parts: printer, scanner

Ex2:
Implement priter, scanner seperately

Conclusion: making interfaces which feature too many element is not a good idea. Because you are forcing your client to define method in this cases, which they might not even need