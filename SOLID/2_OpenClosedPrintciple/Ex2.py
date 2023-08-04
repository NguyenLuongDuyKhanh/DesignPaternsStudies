from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Specification:
    def is_satisfied(self, item):
        pass

    # and operator makes life easier
    def __and__(self, other):
        return AndSpecification(self, other)

# Implement a combinator in order to make Specification __add__ works
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))

class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Why dont we just put it to base class (Filter)
# -> If you decide to somehow change the logic of the way that things are filtered, you can simply inherit from the filter class and do something different
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

bf = BetterFilter()
green = ColorSpecification(Color.GREEN)
print("Green products (new): ")
for p in bf.filter(products, green):
    print(f"{p.name} is green")

"""
Green products (new): 
Apple is green
Tree is green
"""

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(products, large_blue):
    print(f' - {p.name} is large and blue')