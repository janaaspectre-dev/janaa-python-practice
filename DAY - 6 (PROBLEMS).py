#problems

'''#1)Count the number of vowels in a string.
name = str(input("enter name here:"))
vowels="aeiouAEIOU"
count = sum(1 for i in name if i in vowels)
print(count)



#2)Check whether a string is palindrome or not.
word = input("enter word here:")
palidrome=word.replace("","").lower().split()
if palidrome==palidrome[::-1]:
    print("it is palidrome")
else:
    print("it is not palidrome")



#3)Reverse a string without using slicing
word = input("enter word here:")
text = ""
for i in word:
    text=i+text
print(text)



#4)Count uppercase, lowercase, digits, and
word = str(input("enter word here:"))
uppercase=0
lowercase=0
digits=0
specialcharecters=0
if word.isupper():
    uppercase+=1
elif word.islower():
    lowercase+=1
elif word.isdigit():
    digit+=1
else:
    specialcharecters+=1
print(uppercase,lowercase,digits,specialcharecters)


#5)Remove spaces from a string.
word = input("enter word here:")
text=word.strip()
print(text)



#6)Find the length of a string without using len().
count=0
word = input("enter word here:")
count = sum(1 for i in word)
print(count)



#7)Replace all spaces with -.
word = input("enter word here:")
print(word.replace(" ","-"))




#8)Convert the first character of every word to uppercase.
word = input("enter word here:")
print(word.capitalize())'''



#9)Find the frequency of each character in a string
word = input("enter word here:")
frequency = counter(word)
print(frequency)




























    
 

