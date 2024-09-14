#order,unchangeable or immutable, allowduple,square bracket
#multiple value store in a single variable.
#list are ordered,mutable or changeable and allow duplicate value
#using square bracket
list=[1,5,2,3,3]
print("\n",list)

my_list=["string","char","int"]
for x in my_list:
    print("\n",x)


#accessing list index start from 0,1,2,always:
list =[1,5,2,3,3]
print([2])

#accessing the index in list
my_list=["string","char","int"]
#for x in my_list:

#change in list:
my_list[2]="ramjeet"

#insert in list
my_list.insert(2,"kumar")

#add in list
my_list.append("Aadvik")

#remove in list
my_list.remove("kumar")

#remove specifid index (0) in list
my_list.pop(1)

#loop in list
#my_list=["string","char","int"]
#for x in my_list:


#sort or asscending order in list
my_list = ["string","char","int"]

my_list.sort()

#join in list:
my_list = ["string","char","int"]
my_list2=[1,2,3]
my_list3=my_list+my_list2

#join usint for loop:

my_list = ["string","char","int"]
my_list2=[1,2,3]
for x in my_list2:
    my_list.append(x)



print(my_list)




