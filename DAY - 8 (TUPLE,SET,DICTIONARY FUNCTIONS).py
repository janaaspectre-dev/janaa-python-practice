#TUPLE FUNCTIONS:


#1)count():Returns the number of times a specified value appears in the tuple
num = (1,1,2,3,4,5,6,4,8,9,11,23,45)
print(num.count(23))



#2)index():Returns the index position of the first occurrence of a value
num = (10, 20, 30, 40, 50)
print(num.index(40))
print(num.index(46))






#SET FUNCTIONS:


#1)add():Adds a single element to the set.
s = {1 , 2 ,3 ,4 , 5}
s.add(6)
print(s)



#2)update():Adds multiple elements from another iterable.
s = {1,2,3,4}
s.update([5,6,7])
print(s)



#3)remove():Removes a specified element. Raises an error if the element does not exist.
s = {1,2,3,4}
s.remove(3)
print(s)



#4)discard():Removes a specified element. Does not raise an error if the element is absent.
s = {1,2,3,4}
s.discard(4)
print(s)



#5)pop():Removes and returns a random element.
s = {1,2,3,4}
s.pop()
print(s)



#6)clear():Removes all elements from the set.
s = {1,2,3,4}
s.clear()
print(s)



#7)copy():Returns a copy of the set.
s1 = {1,2,3}
s2 = s1.copy()
print("s2=",s2)



#8)union():Returns a new set containing all unique elements from both sets.
X = {1,2,3}
Y = {4,5,6}
print(X.union(Y))



#9)intersection():Returns elements common to both sets.
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.intersection(s2))



#10)difference():Returns elements present in the first set but not in the second
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.difference(s2))



#11)symmetric_difference():Returns elements that are in either set, but not in both.
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.symmetric_difference(s2))



#12)issubset():Checks whether all elements of one set exist in another
s1 = {9,10}
s2 = {9,10,11,12,13}
print(s1.issubset(s2))



#13)issuperset:Checks whether a set contains all elements of another set
s1 = {1, 2, 3, 4}
s2 = {1, 2}
print(s1.issuperset(s2))



#14)isdisjoint:Checks whether two sets have no common elements.
s1 = {1,2}
s2 = {3,4}
print(s1.isdisjoint(s2))



#15)intersection_update():Updates the set with common elements only.
s2 = {1, 2, 3}
s1 = {2, 3, 4}
s1.intersection_update(s2)
print(s1)



#16)symmetric_difference_update():Updates the set with elements not common to both sets.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference_update(s2)
print(s1)






#DICTIONARY FUNCTIONS:


#1)get():Returns the value of a specified key.
SAS = {"name":"jhon price","age":45,"role":"captain of task force 141"}
print(SAS.get("role"))



#2)keys():Returns all keys.
SAS = {"name":"jhon price","age":45,"role":"captain of task force 141"}
print(SAS.keys())



#3)values():Returns all values.
SAS = {"name":'jhon "soap" mactavish',"age":35,"role":"sniper-demolitions","status":"KIA"}
print(SAS.values())



#4)items():Returns key-value pairs as tuples.
SAS = {"name":'kyle "GAZ" garrick',"age":37,"role":"tactical specialist, interrogator"}
print(SAS.items())



#5)update():Adds or updates key-value pairs.
SAS = {"name":'simon "ghost" riley',"age":40,"role":"operations specialist and second-in-command "}
SAS.update({"age":42})
print(SAS)



#6)pop():Removes a specified key and returns its value
RANGERS = {"name":'Hershel von Shepherd III',"age":60,"role":"GENERAL","call sign":"GOLD EAGLE"}
X = RANGERS.pop("call sign")
print(X)
print(RANGERS)



#7)popitem():Removes and returns the last inserted key-value pair
RANGERS = {"name":'Hershel von Shepherd III',"age":60,"role":"GENERAL","call sign":"GOLD EAGLE"}
print(RANGERS.popitem())



#8)clear():Removes all items.
student = {"name": "John", "age": 20}
student.clear()
print(student)



#9)copy():Creates a copy of the dictionary.
SAS = {"name": "John Price"}
TF141 = SAS.copy()
print(TF141)



#10)setdefault():Returns the value of a key. If the key does not exist, inserts it.
DELTA = {"Master Sergeant":"Thomas R"}
DELTA.setdefault("call sign","SANDMAN")
print(DELTA)



#11)fromkeys():Creates a new dictionary from given keys
keys = ("a", "b", "c")
d = dict.fromkeys(keys, 0)
print(d)

