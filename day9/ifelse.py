
no1=10
no2=10
no3=30
"""
if condition:
    statement
"""

if no1>no3:
     print("n01 is greater than no3")

if no2<no3:
     print("n02 is greater than no3")

#using if elif     
if no1>no2:
     print("n01 is greater than no2")
elif no2>no3:
  print("n02 is greater than no3")
elif no2==no2:
  print("n01 is equal to no2")
else:
    print("wrong output")

#using if else   
if no1>no3:
    print("n01 is greater than no3")
else:
    print("n03 is greater than no1")

#short hand if
if no3>no1:print("n03 is greater than no1")

#short if else   
print("n01 is greater than no3")if no1>no3 else print("no1 is smaller than n03")

#using and keyword_-logical operator
if no1==no2 and no1<no3:
    print("n1 and n2 both are equal,and no1 is less than no3")