# we can define a simple class with attributes and methodes
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def is_adulte(self):
        if (self.age >= 18):
            return True
        return False


# declar an object
p1 = Person("hatim", 12, "hatim@email.com")
p2 = Person("rhita", 20, "rhita@email.com")
print(p1.name)
print(p2.name)

# use class functions
print(p1.is_adulte())
print(p2.is_adulte())


# inheritance
class Kid(Person):
    def __init__(self, address):
        self.address = address

kid1 = Kid("fes")
kid1.name = "kid1"

print(kid1.name)
print(kid1.address)