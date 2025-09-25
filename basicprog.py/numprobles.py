# to print the is armstrong or not..
"""
num = int(input("Enter a Number:"))
sum = 0 
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10
if num == sum:
    print(num,"is an Armstrong Number ")
else:
    print(num,
    "is not an Armstrong Number")
    
    
    
    
    
num=int(input("enter a number:"))
num1=num
len=0
sum=0
while num>0:
    digit=num%10
    len+=1
    num=num//10
#print(len)
while num1>0:
    digit=num1%10
    sum+=digit**len
    num1=num1//10
print(sum)

    """
  
#to print the even or odd
"""  
n = 1
while n < 25:
  if n % 2 == 0:
      print("This is Even.",n)
  else:
      print("This is Odd..",n)
  n+=1
 
num = int(input("Enter  a value :"))
if num % 2==0:
   print("Given Number is Even ")
else:
   print("Given Number is Odd ")   
"""
#to print fibanacii series
"""
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b   
        a = b
        b = c
        print(c)
fib(5)
"""

#print the largest among three numbers.
"""
num1 = int(input("Enter number 1 here:"))
num2 = int(input("Enter Number 2 here:"))
num3 = int(input("Enter Number 3 here:"))
if (num1>num2) and (num1>num3):
   print(num1,"is a greater number")
elif (num2>num1) and (num2>num3):
    print(num2,"is a greater number")
else:
    print(num3,"is greater number")
    """
#palindrome or not.
"""
s = input("Enter the value..")
reverse = s[::-1]
if (s == reverse):
    print("Yes, It is Palindrome ")
else:
    print("NO, It is not Palindrome")
-------

num=25452
num1=num  # here we use this for.. ante last lo 0 ayidii number so..ila numb tesukunte aa number lo value adhe untahdi kaada so..
rev=0
while(num>0):
    ld=num%10    # 9,8,7,4,5
    rev=rev*10+ld  #0*10+9==9, 9*10+8=98, 98*10+7=987,987*10+4=9874,,9874*10+5=98475.
    num=num//10  #5478, 547,54,5,0
print(rev) 
if num1==rev:    
    print("It is a palindorme")
else:
    print("it not palindrome")
"""
#to print the prime or not..
"""
num = 7
for i in range(2,num):
    if num % i == 0:
       print("Not a Prime ")
       break
else:
    print("prime ")
"""


#to print the reverse the string
"""
n = "orange"
def string(n):
   str=""
   for i in n:
       str = i+str
   print(str)
print("/n")
string(n)

s=input("Enter a string:")
for word in s.split():
    print(word[::-1],end="")

s=input("Enter something to print:")
output=" "
i = len(s)-1                                                                                                                                                                                                                                                                                                                                                                                                    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa AAAAAAA
while i >=0:
    output=output+s[i]
    i = i-1
print(output)
    
"""
# to print swapping numbers.
"""
a = 10
b = 20
print("Before swapping values")
print("a:",a)
print("b:",b)
a = a+b
b = a-b
a = a-b
print("After Swappping valuees")
print("a:",a)
print("b:",b)
"""

# sum of arrays..
"""
def sum1(arr):
  if len(arr) == 1:
      return arr[0]
  else:
      return arr[0] + sum1(arr[1:])
  
arr = [12, 3, 4, 15]
print(sum1(arr))
"""

# to know the income tax...
income = int(input("Enter your income: "))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.10
else:
    tax = (250000 * 0.05) + (500000 * 0.10) + (income - 1000000) * 0.20

print(f"Total tax to be paid is ₹{tax}")


    




 