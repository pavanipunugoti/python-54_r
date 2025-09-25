
#print the sunny number..
"""
num=int(input("Enter a umner:"))
newNum=num+1
#print(newNum)
#here we are doing squaroot newNum 
ptsq=newNum**(1/2)
#print(ptsq)
if ptsq==int(ptsq):
    print(num,'is a sunny number')
else:
    print("It is not a sunny")
    
"""
    

# check number is neon or not  ..neon number(sum of digits if its square is equal to its number..)
  # eg..9*9=81
   #8+1=9 SO like 


# num=int(input("Enter a number:"))     #Remainder===%..o reaminder vachiddii..mext digit lo store chesam...and next sum tho add chesam
# square=num*num                    # 0+that value..ext floor divison(//) quoter(8). neon = 8.,,,[8%10..(8)] mallli reaminder 8 ey vastdhii..next
# sum=0
# while square>0:              digits lo 8 undi..and next sum lo  add chesakaa compare chestam """

"""
num=int(input("enter a number:"))
sum=0
neon=num**2
print(neon)
while neon>1:
    digit=neon%10         # last digit ni acces chesthunnam   Next execution(# 8%10=8)
    sum=sum+digit        # danilo last digit ni add chesthunnam ante 8..   # add chesthunnam
    neon=neon//10      #aa tesukunna no tesesam. neon value 8.next loop run avuthundi ..//chestehe..1 kante takkuva vastdhii so while loop execte avdhu.
#print(num)            # inka afi poyiddi loop nct of daggriki velli condtion check chesi print ayiddi..5

if sum==num:
    print("It is a neon number")
else:
    print("it is not neon number")
    
"""

# fact of a number ki steps;
# number=5
# fact=1
# we will take loop in  range from number to 1:
# fact=5*4*3*2*1
# print(fact())


#Factors of a given number.
num=int(input("Ener a number:"))
print("Factors of",num,"are:")
i=1
while i<=num:
    if num%i == 0:
        print(i)
    i+=1 


#Check number is Perfect Number or not.
num=int(input("Enter a number:"))
sum=0
#find divisors using a loop
for i in range(1,num):
    if num % i==0:
        sum+=i
#check if sum of divisors equals the number
if sum==num:
    print(num,"is a Perfect Number")
else:
    print(num,"is not a Perfect Number")
    


#to check perfect square or not.
num=int(input("Ente a number:"))
#initialise i
i=1
square=False
#loop to check perfect square
while i*i<=num:
    if i*i==num:
        square=True
        break
    i+=1
#Print the result
if square:
    print(num,"is perfect Square")
else:
    print(num,"is Not Perfect square")
    
    
    
# to check neon or not  
num=int(input("enter a number:"))
sum=0
neon=num**2
print(neon)
while neon>1:
    digit=neon%10
    sum=sum+digit  
    neon=neon//10 
if sum==num:
    print("It is a neon number")
else:
    print("it is not neon number")
    
    
# to check a factorial of number.
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5))



#to print fibanacii series

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

 ## Print palindorm eor not..
 
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

#..Print prime number or not..  
num = 15
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")
  
# to print the is armstrong or not..

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
    
#(((ORR))

    
num = int(input("Enter a number: "))
num1 = num   # Copy of the original number
length = 0   # To store number of digits
total = 0    # To store sum of powered digits

# : Count the number of digits
temp = num
while temp > 0:
    length += 1
    temp //= 10

# : Calculate sum of each digit raised to 'length'
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp //= 10

# : Check Armstrong condition
#print("Sum of powered digits:", total)
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")









    




