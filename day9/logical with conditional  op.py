#and logical operator

a=90
b=70
c=100
if a>b and c>a:
   print("both are true")

   #or operator
if a>b or a>c:
    print("atleast one condition is true")

#not operator
if not a:
    print("value of a is true")
if not (a%6==0 or a%9==o):
    print("90 is not divisible by either 6 or 9")
else:
    print("90 is divisible by either 6 or 9")