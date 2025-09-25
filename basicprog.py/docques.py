#Atm calculation..
"""
deposit=int(input("Your deposit amount:"))
account=deposit
print(account)
withdrawl = int(input("your withdrawl anount: "))
if withdrawl > account:
    print(" insufficient")
elif withdrawl < account:
    if withdrawl %100==0:
         account = account-withdrawl
         print(f" Your balance is {account}")
         print(" Your withdrawl succeful")
    else:
        print(" withdrawl amount only multiples of 100")
"""

# to know the skills
"""
user_knows=input("Enter the skills:")
if user_knows=="Frontend":
    print(" User become a Frontend Developer..")
elif user_knows=="Backend":
    print("User become a Backend Developer..")
elif user_knows=="Database":
    print("User become a Data base develepoer..")
elif user_knows=="Full stack":
    print(" User become a Full stcak Developer..")
else:
    print("Go and learn the skills...")
"""

##conditionals Statemens..problems..

#Given number is even or odd
"""
number=int(input("Enter the number:"))
if num%2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

"""
    

## Divisible  by 5 not by 10
"""
num=int(input("Enter a number:"))
if num%5==0:
    print("Satisfy")
elif num%10!=0:
    print("Not satisfy")
else:
    print("Enter the valid number")
"""


#Biggest among two number..
"""
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print(f "Greater number is {num2}")
else:
    print(f" Smallest number is {num1}")
"""


#smallest among two numbers..
"""
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
if a<b:
    print(f"Smallest number is {a}")    
else:
    print(f" Greater number is {b}")

"""

#Divisible by 2,3,6
"""
num = int(input("Enter the number:"))
if num%2==0 and num%3==0:
    print("Satisy")
else:
    print("Please enter the satisfy number..")
"""

# Eligible to vote or not..
"""
age=int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote..")
else:
    print("Not eligible to vote..")
"""

#Student Pass/Fail Based on All Subjects
"""
Maths=40
Physics=36
Chemistry=30
marks= int(input("Enter the students marks "))
if marks >=35:
    print("Pass")
else:
    print("Fail")
"""

# student pass only one subject.
"""
marks=int(input("Enter the marks:"))
if marks >= 35:
    print("Pass")
else:
    print("Fail")
"""


# student pass only in two subjects..
"""
marks=int(input("Enter the marks:"))
if marks >=35 or marks >= 20:
    print(" Pass")
else:
    print("fail")
"""

#Biggest Among Three Numbers
"""
num1 = int(input(" Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is Greatest Number ")
elif num2>num1 and num2>num3:
    print(f"{num2} is Greatest Number ")
elif num3>num1 and num3>num2:
    print(f"{num3} is Greatest Number ")
else:
    print("Enter the greatest Number ")
"""

#Smallest Among Three Numbers
"""
a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=int(input("Enter the c value:"))
if a<b and a<c:
    print(f" Smallest number is {a}")
elif b<a and b<c:
    print(f" Smallest number is {b}")
elif c<a and c<b:
    print(f"Smallest number is {c}")
else:
    print("Enter the correct number")
"""

"""
n = int(input("Enter the num 1 ... 4:"))
a = int(input("Enter the value :"))
b = int(input("Enter the value :"))
if n == 1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    print(a%b)
else:
    print("Nothing")
"""
    
# write a progam to display the weeks of the days based on the number(1 for sunday, 2 monday)
"""
value=int(input("Enter the number:"))
if value == 1:
    print("Sunday")
elif value == 2:
    print("Monday")
elif value == 3:
    print("Tuesday")
else:
    print("Enter the correct number")
        
"""

#Write a program to classify enter by the user by vowel , constant or either..
"""
value=input("Enter the string:")
vowels=" a,e,i,o,u"
consonents=" b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
if value == vowels:
    print(" These are vowels")
elif value == consonents:
    print("These are consonents")
else:
    print("Neither")
"""

# check the no is within 100.
"""
num=int(input("Enter the number:"))
if num<=1:
    print('the number is within 100')
elif num <= 100:
    print("The number is within 100")
else:
    print(" The number is not within 100")
"""



## functions ,,write a code to find the greatest number in funcitons..
def greater(a,b,c):
    if a >= b and a>= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(greater(5,6,7))


