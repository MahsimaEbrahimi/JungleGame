# from Cow import Cow_class
# from Dog import Dog_class
# from Donkey import Donkey_class
# from Horse import Horse_class
# from Owl import Owl_class


def create_child_class(name,*parent_classes):
        sth= type(name, parent_classes, {})
        print(dir(sth))
        print(sth.__name__)
        return sth

# class Mate_result_class(Owl_class,Horse_class):
#     def __init__(self, name, id, category, age) -> None:
#         super().__init__(name, id, category, age)

# class Parent1:
#     def method1(self):
#         print("This is method 1 from Parent1")

# class Parent2:
#     def method2(self):
#         print("This is method 2 from Parent2")

# class Parent3:
#     def method3(self):
#         print("This is method 3 from Parent3")

# class Child(Parent1, Parent2):
#     pass

# # Create an instance of Child
# child = Child()
# child.method1()  # This will call method1 from Parent1
# child.method2()  # This will call method2 from Parent2

# # Now let's dynamically change the parent classes that Child inherits from
# Child.__bases__ = (Parent2, Parent3)

# # Now Child will inherit from Parent2 and Parent3
# child.method2()  # This will still work
# child.method3()  # This will call method3 from Parent3


# parent1 = type('Parent1', (), {})
# parent2 = type('Parent2', (), {})
# parent3 = type('Parent3', (), {})

# child1 = create_child_class(parent1, parent2)
# child2 = create_child_class(parent2, parent3)

# print(child1.__bases__)
# print(child1.__name__)  # Output: (<class '__main__.Parent1'>, <class '__main__.Parent2'>)
# print(child2.__bases__)  # Output: (<class '__main__.Parent2'>, <class '__main__.Parent3'>)