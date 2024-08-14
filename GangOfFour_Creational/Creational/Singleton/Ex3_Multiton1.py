import DesignPaternsStudies.GangOfFour_Creational.Creational.Singleton.Ex3_Multiton1 as Ex3_Multiton1

class TestMultiton(metaclass=Ex3_Multiton1.MultitonMetaFactory(0, (1, lambda x: x[1]), kw_b=None) ):
    def __init__(self, a, b, kw_a=None, kw_b=None) -> None:
        self.a = a
        self.b = b
        self.kw_a = kw_a
        self.kw_b = kw_b

instance_a = TestMultiton(42, [1, 15, 42], kw_a="this is the first instance", kw_b=15)
instance_b = TestMultiton(42, [5, 15, 801], kw_a="this is the second instance", kw_b=15)
assert instance_a is instance_b
print(instance_b.kw_a)