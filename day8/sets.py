
set1={"apple","mango","banana","apple",10,20.5}
print(set1)

print(len(set1))

#set constructor
set_constructor=set(("pink","black","white"))
print(set_constructor)

print("pink" in set_constructor)

#for loop
for color in set_constructor:
    print(color)

 #add() method
set_constructor.add("yellow")
print(set_constructor)

#set_constructor.add("purple","blue","sky")

set2={10,20,30,40,50}

set_constructor.update(set2)
print(set_constructor)
list1=[2,4,6,8,10]
set_constructor.update(list1)
print(set_constructor)

#using remove() method
set_constructor.remove(2)
set_constructor.remove("yellow")
#set_constructor.remove("yellow") #it  will throw error
print(set_constructor)

set_constructor.discard("yellow") #it will not throw error
print(set_constructor)

#remove last element of the set
films={"tiger","liger","new  york","zero"}
print(films.pop())
print(films)

films.clear()
print(films)

del films
#print(films)

#union method
numbers={233,453,673,893,993}
strings={"katrina","vicky","ranbir","katrina",233,453}
combine_set=numbers.union(strings)
print(combine_set)

numbers.intersection_update(strings)
print(numbers)

duplicate_values=numbers.intersection(strings)
print(duplicate_values)


