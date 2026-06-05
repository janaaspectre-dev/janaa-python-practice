#MODULE (BUILT IN)


"""#MATH
import math



#1. Square Root – sqrt()
print(math.sqrt(25))


#2. Power – pow()
print(math.pow(2,3))


#3. Ceiling – ceil():Rounds a number up to the nearest integer.
print(math.ceil(4.2))


#4. Floor – floor():Rounds a number down to the nearest integer.
print(math.floor(4.8))


#5. Factorial – factorial()
print(math.factorial(5))


#6. Absolute Value – fabs():Absolute value
print(math.fabs(-10))


#7. Greatest Common Divisor – gcd()
print(math.gcd(12,18))


#8. Trigonometric Functions
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))


#9. Logarithm – log()
print(math.log(10))


#10. Exponential – exp()
print(math.exp(2))


#Important Constants
print(math.pi)
print(math.e)



#SCIPY
from scipy import integrate,optimize,stats


#1. integrate.quad():Calculates the definite integral of a function.
from scipy import integrate
result, error = integrate.quad(lambda x: x**2, 0, 3)
print(result)


#2. optimize.root():Finds the root (solution) of an equation.
from scipy import optimize
result = optimize.root(lambda x: x**2 - 4, 2)
print(result.x)



#TIME MODULE

#1. time.time():Returns the current time in seconds since January 1, 1970 (Unix timestamp).
import time as t
print(t.time())


#2. time.sleep(seconds):Pauses the program for a specified number of seconds.
print("start")
t.sleep(3)
print("end")


#3. time.ctime():Converts a timestamp into a readable date and time.
print(t.ctime())


#4. time.localtime():Returns the current local time as a structured object.
x = t.localtime()
print(x)


#5. time.strftime():Formats date and time according to a specified format.
print(t.strftime("%d-%m-%y"))


#6. time.gmtime():Returns the current UTC (Greenwich Mean Time).
print(t.gmtime())


#7. time.asctime():Converts a time tuple into a readable string.
x = t.localtime()
print(t.asctime(x))


#8. time.perf_counter():Returns a high-precision timer for measuring execution time.
start = t.perf_counter()
for i in range(806):
    pass
end = t.perf_counter()
print(end-start)



#CALENDAR MODULE

import calendar as c

#1. calendar.calendar(year):Displays the whole calendar for a year.
print(c.calendar(1))


#2. calendar.month(year, month):Displays a specific month's calendar.
print(c.month(2026,6))


#3. calendar.isleap(year):Checks whether a year is a leap year.
print(c.isleap(2024))


#4. calendar.leapdays(y1, y2):Counts leap years between two years.
print(c.leapdays(2000,2026))


#5. calendar.weekday(year, month, day):Returns the day of the week.
print(c.weekday(2026,6,4))


#6. calendar.monthrange(year, month):Returns the first weekday and number of days in a month.
print(c.monthrange(2016,12))


#7. calendar.month_name:Returns month names.
print(c.month_name[6])


#8. calendar.day_name:Returns weekday names.
print(c.day_name[3])


#9. calendar.firstweekday():Returns the current first weekday setting.
print(c.firstweekday())


#10. calendar.setfirstweekday():Sets the first day of the week.
c.setfirstweekday(c.SUNDAY)
print(c.month(2026,6))



#DATE TIME MODULE:
from datetime import datetime as dt



#1. datetime.now():Gets the current date and time.
print(dt.now())


#2. datetime.today():Gets today's date and time.
print(dt.today())


#3. Creating a Date
x = dt(2026,6,5)
print(x)


#4. Access Date Components
v = dt.now()
print(v.year)
print(v.month)
print(v.day)


#5. Access Time Components
b = dt.now()
print(b.hour)
print(b.minute)
print(b.second)


#6. strftime():Formats date and time as a string.
f = dt.now()
print(f.strftime("%d-%m-%y"))


#7. strptime():Converts a string into a date.
e = dt.strptime("05-06-2026", "%d-%m-%Y")
print(e)


#8. date.today():Gets today's date only.
print(dt.today())


#9. timedelta():Adds or subtracts days.
from datetime import datetime,timedelta

tod = dt.now()
future = tod + timedelta(days=7)
print(future)


#10. Date Difference

d1from dt import date
d1 = date(2026, 6, 5)
d2 = date(2026, 6, 1)

print(d1 - d2)



#RANDOM
import random as r
#1. random.random():Returns a random decimal number between 0 and 1.
print(r.random())


#2. random.randint(a, b):Returns a random integer between a and b (inclusive).
print(r.randint(1,10))


#3. random.randrange():Returns a random number from a specified range.
print(r.randrange(0,20,2))


#4. random.choice():Selects one random item from a sequence.
tf141 = ["jhon price","simon'ghost'rielly","jhon 'soap' mactavish","garrick 'gaz'"]
print(r.choice(tf141))


#5. random.choices():Selects multiple random items.
tf141 = ["jhon price","simon'ghost'rielly","jhon 'soap' mactavish","garrick 'gaz'"]
print(r.choices(tf141,k=2))


#6. random.shuffle():Shuffles a list in place.
tf141 = ["jhon price","simon'ghost'rielly","jhon 'soap' mactavish","garrick 'gaz'"]
r.shuffle(tf141)
print(tf141)


#7. random.sample():Returns unique random elements from a sequence.
tf141 = ["jhon price","simon'ghost'rielly","jhon 'soap' mactavish","garrick 'gaz'"]
print(r.sample(tf141,3))


#8. random.uniform(a, b):Returns a random decimal number between a and b.
print(r.uniform(1, 10))"""



#PYWHATKIT
import pywhatkit as pk

#1. sendwhatmsg():Sends a WhatsApp message at a specified time.
#pk.sendwhatmsg("+919442281160","hi!!!!",17,45)


#2. sendwhatmsg_instantly():Sends a WhatsApp message immediately.
#pk.sendwhatmsg_instantly("+919994499412","hi i wrote this from python")


#3. playonyt():Plays a video on YouTube.
#pk.playonyt("tf141 edit")


#search():Performs a Google search.
#pk.search("tf141")


#5. info():Gets a summary about a topic.
pk.info("sas" , lines = 2)









