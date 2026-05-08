#arithmetic operator
a=12
print(a)
b=6
print(b)
print("addition",a+b)
print("subraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("inteager division",a//b)
print("remainder",a%b)
print("exponentiation",a**b)



#assigment operator
x=3
print(x)
x+=4
print(x)
x-=4
print(x)
x*=6
print(x)
x**=7
print(x)
x//=3
print(x)


#comparision operators
kamal=51
rajini=72
print(kamal==rajini)
print(kamal!=rajini)
print(kamal>rajini)
print(kamal<rajini)
age1=20
age2=20
print(age1>=age2)
print(age1<=age2)



#logical operators
temperature=25
if temperature>0 and temperature<30:
    print("humid day")
else:
    print("the temperature is bad")
temperature=-10
if temperature>0 and temperature<30:
    print("humid day")
else:
    print("the temperature is bad")
temperature=40
if temperature>0 or temperature<30:
    print("humid day")
else:
    print("the temperature is bad")
sunny = False
if not sunny:
    print("its cloudy outside")
else:
    print("its sunny outsie")



#special operators
    #identiy operators
a=["apple","orange","grapes"]
b=["apple","orange","grapes"]
print(a is b)
print(a is not b)
a=b
print(a is b)

    #membership operators
x=["apple","orange","grapes","watermelon","pineapple"]
if "watermelon" not in x:
    print("present")
else:
    print("absent")
    print("orange" in x)
    print("banana" in x)





#bitwise operators
a=8
b=12
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<2)
print(b>>2)






    


    

      

