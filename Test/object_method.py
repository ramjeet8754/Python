class emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    # object method created with name of myfunc with properites .
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1= emp("ramjeet",21)
p1.myfunc()
