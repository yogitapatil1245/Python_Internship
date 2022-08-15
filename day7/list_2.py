#list using constructor
fruitlist=list(("grapes","banana","apple"))
print(fruitlist)

fruitlistwithoutusingconstructor=["grapes","banana","apple"]
print(fruitlistwithoutusingconstructor)

remixlist=list(("grapes","21.5","name","0"))
print(remixlist)


#changing the elements

fruitlist[0]="strawberry"
print(fruitlist)

newfruitlist=["apple", "cherry", "orange", "kiwi", "mango"]
print(newfruitlist)

newfruitlist[1:3]=["banana","grapes","strawberry"]
print(newfruitlist)

newfruitlist=["orange", "kiwi", "mango"]
newfruitlist[1:3]=["apple"]
print(newfruitlist)


#using insert() method
newfruitlist.insert(2,"banana")
print(newfruitlist)

#using append() method to insert element at the end of the list
newfruitlist.append("kiwi")
print(newfruitlist)

#using extend() method
extendlist=newfruitlist.extend(fruitlist)
print(extendlist)

list1=["orange", "kiwi", "mango"]
list2=["grapes","banana","apple"]
tuple1=["grapes","banana","apple"]

list1.extend(list2)
print(list1)
list1.extend(tuple1)
print(list1)

#using remove() method
list1.remove("grapes")
print(list1)

#using pop() method
list1.pop(2)
print(list1)

list1.pop()
print(list1)

#using Del keyword 
del list1[0]
print(list1)

#delete complete list
del list1
#print(list1)

del tuple1
#print(tuple1)sssssssssss

#empty the list using clear() method
print("list2=",list2)
list2.clear()
print("list2=",list2)

print(len(list2))
#list2[0="orange"]
#print(list2)
list2.insert(0,"grapes")
print(list2)

#copy() method

new_list1=["apple","mango"]
new_list2=["banana","cherry"]
#new_list2=new_list1
new_list2=new_list1.copy()
print(new_list2)
new_list2.insert(2,"yogita")
print(new_list1)