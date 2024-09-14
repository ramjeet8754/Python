#A class can inherit from more than one base class.

class Parent1:
    def method_parent1(self):
        print("This is Parent1 method")

class Parent2:
    def method_parent2(self):
        print("This is Parent2 method")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method")

c = Child()
c.method_parent1()
c.method_parent2()
