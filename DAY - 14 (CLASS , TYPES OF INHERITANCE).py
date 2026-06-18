#CLASS and object
class tf141:
    def __init__(self,name,role,rank):
        self.name = name
        self.role = role
        self.rank = rank
    def status(self):
        print("stand by for further orders")
price = tf141("jhon price"," Field Commander","Captain")
MacTavish = tf141("John 'Soap' MacTavish","Demolitions/sniper","2nd in command")
Ghost = tf141(" Simon 'Ghost' Riley","Pointman, Interrogator, and Marksman","Lieutenant")
GAZ = tf141("Kyle 'Gaz' Garrick","CQB Specialist","Sergeant")
Roach = tf141("Gary 'Roach' Sanderson","Recon and Intel Specialist","Sergeant")
print(price.)
print(MacTavish.)
print(Ghost.)
print(GAZ.)
print(Roach.)


#INHERITENCE

#TYPES
#SINGLE:
class army:
    def infantry(self):
        print("Mountain Infantry")
        print("Scouts (Border Scouts)")
        print("Ghatak Platoons")
        print("Airborne / Paratroopers")

class armoured_corps(army):
    def heavy_and_light_armoured(self):
            print("Arjun MK-1")
            print("Arjun MK-2")
            print("T-90")
            print("T-72")
            print("ZORVAR LBT")
            print("BMP-1")
            print("BMP-2(SARATH)")
A = armoured_corps()
A.heavy_and_light_armoured()


#MULTILEVEL
class army:
    def infantry(self):
        print("Mountain Infantry")
        print("Scouts (Border Scouts)")
        print("Ghatak Platoons")
        print("Airborne / Paratroopers")

class armoured_corps(army):
    def heavy_and_light_armoured(self):
            print("Arjun MK-1")
            print("Arjun MK-2")
            print("T-90")
            print("T-72")
            print("ZORVAR LBT")
            print("BMP-1")
            print("BMP-2(SARATH)")

class special_forces(armoured_corps):
    def commandos_and_covert(self):
        print("NSG")
        print("BAHIRAV")
        print("MARCOS")
        print("PARA SF")
        print("Garud Commando Force")
s = special_forces()
s.commandos_and_covert()


#HIRECHIAL
class army:
    def infantry(self):
        print("Mountain Infantry")
        print("Scouts (Border Scouts)")
        print("Ghatak Platoons")
        print("Airborne / Paratroopers")
class Artillery(army):
    def long_short_ranges(self):
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
class armoured_corps(army):
    def heavy_and_light_armoured(self):
            print("Arjun MK-1")
            print("Arjun MK-2")
            print("T-90")
            print("T-72")
            print("ZORVAR LBT")
            print("BMP-1")
            print("BMP-2(SARATH)")
A = armoured_corps()
a = Artillery()
A.
a.


#MULTIPLE
class fieldmedic:
    def medic(self):
        print("Army Medical Corps (AMC)")
        print("Paratrooper Medic (Para AMC)")
        print("High-Altitude / Siachen Medic")
        print("Combat Aviation Medic")

class fieldengineer:
    def engineer(self):
        print("Corps of Engineers")
        print("Combat Engineers (Sapppers)")
        print("Military Engineer Services (MES)")
        print("Border Roads Organisation (BRO)")
        print("Marrine Accommodation Project (MAP)")

class army:
    def infantry(fieldmedic,fieldengineer):
        print("Mountain Infantry")
        print("Scouts (Border Scouts)")
        print("Ghatak Platoons")
        print("Airborne / Paratroopers")
A = army()







#HYBRID
class AR15:
    def base_traits(self):
        print("Using standard AR-15 charging handle and body frame")


class M4carbine(AR15):
    def compact_size(self):
        print("Lightweight and easy to move around with")


class HK416(AR15):
    def piston_system(self):
        print("Reliable gas piston system that reduces jammed rounds")


class M27IAR(M4carbine,HK416):
    def heavy_barrel(self):
        print("thick barrel made for continuous automatic firing")

r = M27IAR()


    




        
          
        









    
        



        
        
    


    
    

        
        

    
