class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonList(list):
    def append(self, *args):
        for person in args:
            if isinstance(person, Person):
                super().append(person)
            else:
                raise TypeError("Only instances of Person class can be appended to the list")

# Example usage
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person_list = PersonList()
person_list.append(person1, person2)

print(person_list)  # Output: [<__main__.Person object at 0x7f3d4b5e4a90>, <__main__.Person object at 0x7f3d4b5e4ac8>]