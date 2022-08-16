tuple1=("strawberry","cherry","blueberry",10,20,30,10.2)
print(tuple1)

#len()
print(len(tuple1))

#creating tuple using tuple() constructor
tuple2=tuple(("orange","white","green"))
print(tuple2)

#single element tuple
tuple3=("one")
print(tuple3)
#print(type(tuple4))

tuple4=("one",)
print(type(tuple4))

print(tuple1[2])

#tuple is unchangable we cant assignn the value to the tuple after creating it
#tuple4[1]="two"
#print(tuple4)

#converting tuples to list for modifyig purpose
list1=list(tuple2)
list1.insert(2,"cat")
new_tuple=tuple(list1)
print(new_tuple)

#packing of tuple
fruits=("apple","banana","cherry")

#unpacking of tuple
(fruits1,fruits2,fruits3)=fruits
print(fruits1,fruits2,fruits3)

colors=("red","black","yellow","purple")
(red,black,*others)=colors
print(red,black,others)

(red1,*others1,yellow,purple)=colors
print(red1,others1,yellow,purple)

t_colors=("black","white","red")
t_numbers=(10,20,30,40,30,30,40,30,30,40)

combine_tuple= t_colors+t_numbers
print(combine_tuple)

repeated_tuple=t_colors*3
print(repeated_tuple)

#count() number 
print(t_numbers.count(30))

#index()
print(t_numbers.index(30))

