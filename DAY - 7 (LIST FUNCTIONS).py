#LIST FUNCTIONS


#APPEND:Adds a single element to the end of the list.
allies = ["USA","UK","USSR"]
allies.append("FRANCE")
print(allies)



#EXTEND:Adds all elements from another iterable (list, tuple, string, etc.)
#to the end of the list.
whole_num = [0,1,2,3,4]
whole_num.extend([5,6,7,8])
print(whole_num)



#INSERT:Inserts an element at a specified position.
cards = ["ace","queen","jack"]
cards.insert(1, "king")
print(cards)



#REMOVE:Removes the first occurrence of a specified value.
allies = ["USA","UK","USSR","GERMANY"]
allies.remove("GERMANY")
print(allies)



#POP:Removes and returns the element at the specified index.
#If no index is given, removes the last element.
num = [10,20,30,40]
item = num.pop()
print(item)
print(num)



#CLEAR:It removes all the elements from the list.
world = ["ww1","ww2","korean war","vietnam war","chec war","indo pak","indo-sino"]
world.clear()
print(world)



#INDEX:Returns the index of the first occurrence of a specified value.
allies = ['USA', 'UK', 'USSR', 'FRANCE']
print(allies.index("USSR"))




#COUNT:Returns the number of times a value appears in a list.
num = [1,2,2,3,3,4,4,4,5,6,7,8,8,9]
print(num.count(9))




#SORT:Sort the list in ascending order by default.
num = [7, 2, 10, 4, 1, 9, 5, 3, 8, 6]
num.sort()
print(num)



#REVERSE:Reverses the order of elements in the list.
allies = ['USA', 'UK', 'USSR', 'FRANCE']
allies.reverse()
print(allies)



#COPPY:Creates a shallow copy of the list.
axis = ["germany","italy","imperial japan"]
new = axis.copy()
print(new)








