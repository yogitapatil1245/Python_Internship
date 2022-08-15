#dictionary in python=english to marathi dictionary
#it is collection of key value pairs
#dict1={"key":"value","key2":"value2"}
Employee={
  "name": "shiv",
  "designation": "software",
  "experience": 3
}
print(Employee)
#print(type(Employee))
#DICTIONARY do not allow duplicate keys,if dictionary contains duplicate keys then it
#  always trys to  hold the recent value i.e. shiV
Employee={
 "name": "shiv",
  "designation": "software",
  "experience": 3,
  "name": "shiv"
}
print(Employee)

#keys with different cases are always treated as a different
#here name and Name are different
#keys in dictionary are always case sensitive
Employee={
 "name": "shiv",
  "designation": "software",
  "experience": 3,
  "Name": "shiv",
  "colors":["orange","black","red"]
  }
print(Employee)

print(len(Employee))

#accesing the dictionary items by using keys
print("colors",Employee["colors"])

#accessing dictionary items using get() method
print(Employee.get("colors"))


#obtaining using key value
employee_keys=Employee.keys()
print(employee_keys)

#obtaining all the keys using values() method
Employee_values=Employee.values()
print(Employee_values)

#changing the values 
Employee["designation"]="dangerous programmer"
print(Employee["designation"])

#retreving all the items using items() method
employee_items=Employee.items()
print(employee_items)

#CHECKING whether a key exist or not
print("name" in Employee)

#USING UPDATE() METHOD ADDING NEW KEY VALUE IN DICTIONARY
Employee.update({"join_year": 2020,"salary":1000000})
print(Employee)

#using pop() method to remove key values
Employee.pop("salary")
print(Employee)

#using popitem() method to remove the last item in dictionary
Employee.popitem()
print(Employee)

#using del keyword to remove item from dictionary
del Employee["colors"]
print(Employee)

#using clear() method for removing  all items from the dictionary 
Employee.clear()
print(Employee)

#new dictionary
student={
    "name":"rudra",
    "rollno":"12",
    "department":"computer",
    "college":"gandhi college"
}

department={
    "name":"alia",
    "yers":3,
    "subject":["java","javascript","sql"]
}
print(department)

student1=student.copy()
print(student)

student1.update(department)
print(student1)

#create dictionary of cse class nested dictionary
student3={"name":"pratu","rollno":58}
computerclass={
    "student1":{"name":"yogu","rollno":56},
     "student2":{"name":"veer","rollno":57},
     "student3":student3
}
print(computerclass)