"When piecewise object construction is complicated, provide an API for doing it succinctly"

A builder is a seperate component for building an object
Can either give builder an initializer or return it via a static function
To make builder fluent return self
Different facets of an object can be built with different builders working in tandem via a base class
