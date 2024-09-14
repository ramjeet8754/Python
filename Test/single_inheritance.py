
#In single inheritance, a class (child) inherits from only one superclass (parent).
class Parent:
    def parent_method(self):
        print("This is the parent method")

class Child(Parent):
    def child_method(self):
        print("This is the child method")

c = Child()
c.parent_method()  # Accessing parent class method
