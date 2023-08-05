Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.
This is a special object that converts the interface of one object so that another object can understand it.

# Approaches to implement an adapter

## In term of class structure

### Uses inheritance
- The adapter inherits interfaces from both objects at the same time. 
- Note that this approach can only be implemented in programming languages that support multiple inheritance, such as C++.
- The Class Adapter doesn’t need to wrap any objects because it inherits behaviors from both the client and the service. The adaptation happens within the overridden methods.

### Uses the object composition principle
- The adapter implements the interface of one objectand wraps the other one. It can be implemented in all popular programming languages.

## In term of data catching

### No catching
- **Cons**: The adapter actually generates temporary objects because in order to adapt an objectA to an objectB, it has to generate lots of temporary things. Why do we have to keep doing it over and over again?! How to customize this problem, prevent regeneration of stuff.

### With catching
- **Pros**: Intermediate representations could no longer pile up by utilizing this optimization.