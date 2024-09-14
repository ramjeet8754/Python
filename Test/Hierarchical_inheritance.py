
#Multiple classes inherit from the same base class.

class Parent:
    def parent_method(self):
        print("This is the parent method")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method")

c1 = Child1()
c2 = Child2()
c1.parent_method()
c2.parent_method()
