import random
class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1,100) 
        # Even these are only one object, __init__ was called twice
        # It is not what we want
        print(id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance
        
if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 is d2)