#class person created as parent or base class with properites as a first name and last name
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    #Here created oject method as a printname with property like fname and lname
    def printname(self):
        print(self.firstname,self.lastname)

#here created oject or variable as a p1 and assing value as a first name and last name
p1=person("ram","jeet")
#here,calling printname and printing or object method
p1.printname()

print("\n--------------------------------------------")

class papa:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def myprint(self):
        print(self.firstname,self.lastname)
class son(papa):
    pass
p1= son("ramjeet","Paswan")
p1.myprint()

print("\n--------------------------")
class papa:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
# here created child class with first name and lastname with parents properits ans methods.
class son(papa):
    def __init__(self,fname,lname):
        papa.__init__(self,fname, lname)
p1=son("Advik","Ronak")
p1.printname() 

print("\n super() function that will make the child class inherit all the methods and properties from its parent:-------")

class papa:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
# here created child class with first name and lastname with parents properits ans methods.
class son(papa):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.bornyear= year

    #Here adding metod funcation
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the world of",self.bornyear)

#here adding properities 
p1=son("Advik","Ronak",2024)
p1.welcome()