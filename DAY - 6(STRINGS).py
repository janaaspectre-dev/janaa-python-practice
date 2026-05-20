
#String Methods


#1)capitalize(): Converts the first character of the string to capital letter
name = "janaa"
print(name.capitalize())


#2)count(): returns occurrences of substring in string, count(substring, start=.., end=..).
#The start is a starting indexing for counting and end is the last index to count.
me="the greatest of all time"
print(me.count("t"))
print(me.count("a"))
print(me.count("s"))
print(me.count("g"))


#3)endswith(): Checks if a string ends with a specified ending
email = "janaa@gmail.com"
print(email.endswith(".com"))

challenge = 'thirty days of python'
print(challenge.endswith('on'))   
print(challenge.endswith('tion'))



#4)expandtabs(): Replaces tab character with spaces, default tab size is 8.
#It takes tab size argument
me = "the\tgreatest\tof\tall\ttime"
print(me.expandtabs())
print(me.expandtabs(10))



#5)find(): Returns the index of the first occurrence of a substring,
#if not found returns -1
me = "Greatest of all time"
print(me.find('m'))
print(me.find("z"))



#6)format(): formats string into a nicer output
first_name = "Winston"
second_name = "Churchil"
age = 67
job = "war minister"
country = "United Kingdom"
sentence = "i am {}{}. of age {} years old. i am the {}. of the nation of {}.".format(first_name,second_name,age,job,country)
print(sentence)


radius = 10
pi = 3.14
area = pi * radius ** 2
result = "the area of circle with radius {} is {}".format(radius,area)
print(result)



#7)index(): Returns the highest index of a substring,
#additional arguments indicate starting and ending index (default 0 and string length - 1)
me = "Greatest of all time"
print(me.index("r"))
print(me.index("z"))




#8)isalnum(): Checks alphanumeric character
me = "Greatestofalltime"
print(me.isalnum())

me = "77thegreatestofalltime"
print(me.isalnum())

me = "the greatest of all time"
print(me.isalnum())    # False, space is not an alphanumeric character

me = "77 the greatest of all time"
print(me.isalnum())



#9)isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
me = "the greatest of all time"
print(me.isalpha())    # False, space is once again excluded


me = "77thegreatestofalltime"
print(me.isalpha())


num = '123'
print(num.isalpha())


me = "Greatestofalltime"
print(me.isalpha())



#10)isdecimal(): Checks if all characters in a string are decimal (0-9)
me = "the greatest of all time"
print(me.isdecimal())


num = '123'
print(num.isdecimal())


challenge = '12 3'
print(challenge.isdecimal())   # False, space not allowed



#11)isdigit(): Checks if all characters in a string are numbers
#(0-9 and some other unicode characters for numbers)
num = "thirty"
print(num.isdigit())

num = "30"
print(num.isdigit())



#12)isnumeric(): Checks if all characters in a string are numbers or number related
#(just like isdigit(), just accepts more symbols, like ½)
num = "10"
print(num.isnumeric())

num = "10.5"
print(num.isnumeric())



#13)isidentifier(): Checks for a valid identifier
#- it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())



#14)islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())

challenge = 'Thirty days of python'
print(challenge.islower())



#15)isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper())

challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())



#16)join(): Returns a concatenated string
aviation_corporations = ["sukhoi","lockhead martin","mikoyan","northrop grunmann","HAL"]
result = '#'.join(aviation_corporations)
print(result)


#17)strip(): Removes all given characters starting from the beginning and end of the string
me="   janaa@77  "
print(me.strip())


#18)replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))



#19)split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())

challenge = 'thirty, days, of, python'
print(challenge.split(', '))


#20)title(): Returns a title cased string
me = "========Greatest of all time========"
print(me.title())



#21)swapcase(): Converts all uppercase characters to lowercase and
#all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())

challenge = 'Thirty Days Of Python'
print(challenge.swapcase())


#22)startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) 

challenge = '30 days of python'
print(challenge.startswith('thirty'))






















      
