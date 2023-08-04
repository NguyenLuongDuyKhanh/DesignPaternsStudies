"Depend upon abstractions, [not] concretions."
High level module should not depend directly on low level module. Instead it should depend on abstraction


Ex1:
Class Research is the top level of Relationships. It is using 'relations' which is a member of the lower level - Relationships. One the 'relations' change its type (into list/tuple/list of dictionary) it make Research to be change, it is not gud

Ex2:
put find_all_children_of into the lower level module: Relationships.
