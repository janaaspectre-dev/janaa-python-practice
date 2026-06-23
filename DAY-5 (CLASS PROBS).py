#DAY-5 CLASS PROBLEMS


#1)Print numbers from 1 to 100.
for i in range(1,101):
    print(i)



#2)Print even numbers from 1 to 50.
for i in range(2,51,2):
    print(i)


#3)Print multiplication table of a number.
number=int(input("enter number here:"))
for i in range(1,11):
           print(number*i)


#4)Find sum of first n natural numbers
n=int(input("enter the number:"))
total=0
for i in range(1,n+1):
    total+=i
    print(total)


#5)Find factorial of a number.
n=int(input("enter number here:"))
factorial=1
for i in range (1,n+1):
    factorial*=i
    print(factorial)


#6)Count digits in a number.
number=int(input("enter number here:"))
count=0
for i in range(1,n+1):
    number%i==0
    print("hi ")





#7)Reverse a number using loop.
for i in range(10,0,-1):
    print(i)



#8)Find whether a number is prime.
n=int(input("enter number:"))
for i in range(2,n):
    if n%i==0:
        print("number is not prime")
    else:
         print("number is prime")


#9)Print Fibonacci series
a=int(input("enter number-1:"))
b=int(input("enter number-2:"))
n=int(input("enter range:"))
for i in range(n):
    c=a+b
    d=c+b
    e=d+c
fibonacci_series=a,b,c,d,e
print(fibonacci_series)



#10)Find largest number in a list.
x=[12,34,56,67,69,21,490]
largest=max(x)
print("largest number:",largest)




#11)Count vowels in a string
word=str(input("enter word here:"))
vowels="aeiouAEIOU"
count=0
for i in word:
    if i in vowels:
        count+=1
print("number of vowels:",count)"""




#12)Find sum of digits of a number.
number=int(input("enter number here:"))












         





        
        
    
 






    
    

    
    




    
