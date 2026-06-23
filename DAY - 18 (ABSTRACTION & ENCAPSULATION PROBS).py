"""#RIDE BOOKING APP:(ENCAPS)

class ride_booking_app:
    def current_location(self,location):
        print("your current location")

    def cal(self,distance):
        self.__fare = distance*15
        return self.__fare
    
    def show_fare(self):
        print("your fare is:",self.__fare)

distance = int(input("enter distance of location(Km):  "))
r = ride_booking_app()
r.cal(distance)
r.show_fare()



#Online Payment System: (ABSTRACTION)

from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amt):
        pass

class UPI(payment):
    def pay(self,amt):
        print("paid using UPI")

class creditcard(payment):
    def pay(self,amt):
        print("paid using credit card")

u = UPI()
c = creditcard()
u.pay(100)
c.pay(1000)"""



#Movie Ticket Booking System (abstraction & encaps)
from abc import ABC,abstractmethod

class ticket(ABC):
    def __init__(self,price):
        self.__price = price

    def show_price(self):
        return self.__price

    def set_price(self,price):
        self.price = price


    @abstractmethod
    def book_ticket(self):
        pass
         
         


class regtickets(ticket):
    print("regular tickets booked")
    print("price:",self.show_price())

class premiumtickets(ticket):
    print("premium tickets booked")
    print("Price:", self.show_price())

r = regtickets(90)
p = premiumtickets(200)

        









        
    
    
        
    







    
        
        

    
