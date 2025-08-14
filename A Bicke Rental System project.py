class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the postive value or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total prices",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=bikeShop(100)
    uc=int(input(" 1 Display \n 2 Rent a Bike \n 3 Exit"))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Qty:---"))
        obj.rentForBike(n)
    else:
        break
            
