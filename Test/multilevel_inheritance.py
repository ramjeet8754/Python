#In multilevel inheritance, a class inherits from a class which itself inherits from another class.

class GrandParent:
    def grandparent_method(self):
        print("This is the grandparent method")

class Parent(GrandParent):
    def parent_method(self):
        print("This is the parent method")

class Child(Parent):
    def child_method(self):
        print("This is the child method")

c = Child()
c.grandparent_method()
c.parent_method()
