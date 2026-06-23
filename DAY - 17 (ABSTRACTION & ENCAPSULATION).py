#ABSTRACTION AND ENCAPSULATION


from abc import ABC,abstractmethod


class infantry(ABC):
    @abstractmethod
    def army(self):
        pass
        

class armoured_corps(infantry):
    def army(self):
            print("Arjun MK-1")
            print("Arjun MK-2")
            print("T-90")
            print("T-72")
            print("ZORVAR LBT")
            print("BMP-1")
            print("BMP-2(SARATH)")

class special_forces(infantry):
    def army(self):
        print("NSG")
        print("BAHIRAV")
        print("MARCOS")
        print("PARA SF")
        print("Garud Commando Force")

class Artillery(infantry):
    def army(self):
        print("K9-VAJRA(155mm)")
        print("Amogh(155mm)")
        print("M777(BAE)(155mm)")
        print("D-30(122mm)")
        print("Dhanush(155mm)")
        print("FH-77(155mm)")
        print("M-46(130mm)")
        print("OFB(105mm)")
        print("ATAGMS(155mm)")
        print("MGS(155mm)")

a = armoured_corps()
s = special_forces()
A = Artillery()

a.army()
s.army()
A.army()



class cars(ABC):
    @abstractmethod
    def motor_driven(self):
        pass

class ICE(cars):
    def motor_driven(self):
        print("goes vroooom")
        print("customizable from V4 - X16")
        
class CNG(cars):
    def motor_driven(self):
        print("dual fuel system")
        print("Extremely low running costs and lower emissions")

class HEV(cars):
    def motor_driven(self):
        print("Excellent fuel economy")
        print("Seamlessly switches between gas and electric power.")

class BEV(cars):
    def motor_driven(self):
        print("no vrooooom")
        print("Zero tailpipe emissions")
        print("instant torque")


i = ICE()
c = CNG()
h = HEV()
b = BEV()


#ENCAPSULATION (bank):
class bankacc:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def show_balance(self):
        print("balance is: ", self.__balance)


b = bankacc(10000)
b.deposit(1950)
b.show_balance()
b.withdraw(950)
b.show_balance()


        

    
        

    


        









