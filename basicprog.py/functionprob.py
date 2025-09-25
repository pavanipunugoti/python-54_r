def shakehands(persons):
    hs = (persons * (persons-1)/2) 
    return hs
persons = 10
output = shakehands(persons)
print(output)

#1.add  two numbers:
def add(a,b):
    return a+b
print(add(4,5))



#.2.Write a function to return the square of a number..

# Step 2: Define the function
def square_number(num):
    # Step 3: Multiply the number by itself
    result = num * num
    # Step 4: Return the result
    return result
# Step 5: Call the function with an input
number = 5  # You can change this to any number
square = square_number(number)
# Step 6: Display the result
print("The square of", number, "is", square)


#3.write a function to return the factirial of number..
def factorial(a):
    if a==0:
        return 1  # if ikkada last ki a-1 ante 0 kuda avuthundii so..apudu o == 0 ayihey...manki 0 print ayiddi.
    else:        # return 1  isthe apudu migilina value mottam 1 tho mutlple ayyi..value istadhii..
        return a * factorial(a-1)
print(factorial(5))


#4.write a funtion to greatest of two numbers.
def great(a,b):
    if a>b:
        return a
    else: 
        return b
num1= int(input("enter the first number:"))
num2=int(input("enter the second number"))
number=great(num1,num2)
print("the greatest number is",number)

#5.write the function that returns whether a number is even or odd..
def num(n):
    if n%2==0:
        print("Even")
    else:
        print("odd")
num(8)

#6.write a number to check if a number is a prime.
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
num=int(input("Enter a number:"))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number.")
    
    

#7.write a function to return the sum of first n natural numbers.

def natural_num(n):
    total=0
    for i in range(1,n+1): # here 1 we use ./to print that no also
        total += i # here we add the all avlues to total
    return total
num=int(input("Enter a number:"))
result=natural_num(num)
print(result)


#8.Write the function to return maximum of three numbers.
def max(a,b,c):
    if a>b and a>c:
       print("a is maximum")
    elif b>a and b>c:
        print("b is maximum ")
    elif c>a and c>b:
        print("c is maximum")
    else:
        print("enter a valid number")
x=int(input("Enter the a number:")) 
y=int(input("Enter the b number:"))
z=int(input("Enter the c number:"))
max(x,y,z)   # here we take the values from the user.


#9.write the function to reverse a number.

def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev *10+digit
        n=n//10
    return rev
num=int(input("Enter a number:"))
reverse_num=reverse(num)
print("Reversed Number is",reverse_num)


#10.Write a fucntion to count digits in a numberr..#11.Write a function to convert Celsius to Fahrenheit.
#12.Write a fucntion to find the power of a number(base,exponent)
#13.write a fucntion to check if a year or leaf year.
#14.write a function to whether a palindrome or not.
#15.Write a function to calculate simple interst.




