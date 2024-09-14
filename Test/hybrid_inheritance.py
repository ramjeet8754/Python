#A combination of more than one type of inheritance, such as a mix of multiple and hierarchical inheritance.

class Parent:
    def parent_method(self):
        print("This is the parent method")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method")

class GrandChild(Child1, Child2):
    def grandchild_method(self):
        print("This is the grandchild method")

gc = GrandChild()
gc.parent_method()
