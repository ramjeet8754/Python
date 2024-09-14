
class cars:
    def __init__(self,brand,model):
        self.brand = brand
        self.model= model
    def move(self):
        print("drive\t"+ self.brand ,"\t"+ self.model)

class boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model =model
    def move(self):
        print("sliave")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model = model
    def move(self):
        print("fly!")

car1=cars("honda","abc")
boat1=boat("efg","hij")
plane1=plane("klm","nop")

for x in (car1,boat1,plane1):
    x.move()

car1.move()