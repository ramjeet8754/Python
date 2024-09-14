
#collection of data,ordered, changeable ,no duplicate
#key and vaules will work here
dic={
    "name":"ramjeet",
    "age":34,
    "address":"daulatpur",
    "age":34
}
print("\n",dic)

#accessing 
var=dic["age"]
print(var)


# creating class with oject
# here created class name with emp
class emp:
    def __init__(self,name,id):
     self.name=name
     self.id=id

#createing obj name with p1
p1= emp("ramjeet",21)
print(p1.name)
print(p1.id)

#-------
#function



#uncatin defination and declaration 
def add(a ,b):
   return a+b

# calling function

val=add(5,3)
print(val)