#loop/iterative/repetition control:
fruits = ["apple , banana ,cherry"]
for x in fruits:
    print(x)



#patterns:
#1)
print("*")


#2)
x=5
for i in range(x):
    print("*")

for i in range(x):
    print("*",end="")

n=5
for i in range(n):
    for j in range(n):
        print("*",end="")

n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#five star squar:
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


#increasing triangle patt:
n=5
for i in range(n):
     for j in range(i+1):
         print("*",end=" ")
     print()


#decreasing triangle patt:
n=5
for i in range(n):
    for j in range(i ,n):
        print("*",end=" ")
    print()



#right triangle:
n=5
for i in range(n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()




#right upside triangle:
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

#hill triangle
n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


#reverse hill patt:
n=5
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()


#diamond pattern:
rows = 5

# Upper half
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

# Lower half
for i in range(rows - 1):
    print(" " * (i + 1) + "* " * (rows - i - 1))





    

    


