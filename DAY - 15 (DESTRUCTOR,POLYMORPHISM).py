#DESTRUCTOR
class dest:
    def __init__(self,name):
        print("destructor")
        self.name = name
        print(self.name)
    def __del__(self):
        print("object deleted")
s = dest("janaa")
del s


#POLYMORPHISM:

#FUNCTION/METHOD OVERRIDING
class infantry:
    def army(self):
        print("Mountain Infantry")
        print("Scouts (Border Scouts)")
        print("Ghatak Platoons")
        print("Airborne / Paratroopers")

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

X = [armoured_corps(),special_forces(),Artillery()]
for i in X:
    i.army()



#OPERATOR OVERLOADING
class calculator:
    def add(self,a,b=0,c=0,d=0):
        print(a+b+c+d)
c = calculator()
c.add(10,20,900,789)
c.add(34,56,23)
c.add(90,122)
c.add(100)
    











    
