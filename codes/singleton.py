import uuid

class Singleton_class:
    _instance = None
    id = None
    def __new__(cls):
        if cls._instance is None:
            print("creando..")
            cls._instance = super(Singleton_class, cls).__new__(cls)
            cls.id = uuid.uuid4()
        return cls._instance

single = Singleton_class()
print( single.id )

single2 = Singleton_class()
print( single2.id )
