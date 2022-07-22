class Car ():     #class name car
    def __init__(self,modelname,yearm,price): #defining constructor
        self.modelname=modelname        # intializing objects
        self.yearm=yearm
        self.price=price

    def price_inc(self):
        self.price=int(self.price * 1.75)

honda = Car('city',2020,1000000)
tata = Car('bolt',2019,500000)

honda.cc=1500
tata.cc=1000
print(honda.price)
honda.price_inc()
print(honda.price)
