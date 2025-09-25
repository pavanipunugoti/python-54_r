# # 1 t0 100
# for i in range(1,11):
#     print(i)

# # 1 to 20 even mumbers;
# for i in range(2,21,2):
#     print(i)
    
# for num in range(2,21,2):
#     print(num,end=" ")
#     print()


# print odd numbers 1,20
# for num in range(1,21,2):
#     print(num,end=" ")
#     print()
# for i in range(1,21,2):
#     print(i)


# sum of numebrs form 1 to 100
# n=int(input())
# sum=o
# for i in range(1,n):
#     sum+=i
# print(sum)


# multiplication of 5 table..
# for i in range(1,11):
#     print(f"5*{i}={5*i}")
#6. Print all numbers divisible by 3 up to 50.
# for i in range(1,51):
#     if i %3==0:
#         print(i)



#7. Calculate the factorial of a number using a loop
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# v=fact(5)
# print(v)


# n=int(input())
# fact=1
# if n<0:
#   print("this is o")
# elif n==0:
#   print("ths fact of 0 is 1")
# else:
#   for i in range(1,n):
#       fact=fact*i
#   print(f"the factoial of {n} is {fact}")
    
    
    
#  Print numbers from 1 to 10 using a loop.

# for i in range(1,11):
#     print(i,end=" ")

#  Print even numbers from 1 to 20.
# for num in range(1,21):
#     if num%2==0:
#         print(num,end=" ")

# for num in range(2,21,2):
#     print(num,end=" ")

# for num in range(1,21,2):
#     print(num,end=" ")

#  Print odd numbers from 1 to 20.
# for num in range(1,20):
#     if num%2!=0:
#         print(num,end=" ")

#  Calculate the sum of numbers from 1 to 100.
# sum=0
# for num in range(1,100):
#     sum+=num
# print(sum)

#  Print multiplication table of 5.
# num=5
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

#  Print all numbers divisible by 3 up to 50.
# for num in range(1,50):
#     if num%3==0:
#         print(num,end=" ")

# 7. Calculate the factorial of a number using a loop.
# n=int(input("Enter a number"))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# num=int(input("Enter a number: "))
# fact=1
# if num<0:
#     print("fact doesn't exist")
# elif num==0:
#     print("fact is zero")
# else:
#     if num>0:
#         for i in range(1,num+1):
#             fact=fact*i
#         print(f"factorial of a {num} is {fact}")

# 8. Reverse the digits of a number using a loop.
# num=int(input("Enter a number: "))
# num1=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)
    
# Print squares of numbers from 1 to 10.
# for num in range(1,11):
#     print(f"{num**2}",end=" ")

# 10. Count the number of digits in an integer.
# int=234568578
# count=0
# while int>0:
#     digit=int%10
#     count+=1
#     int=int//10
# print(count)

# 11. Find the sum of digits of a number.
# num=3445
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)

# 12. Print powers of 2 up to 2^10.

# num=2
# for i in range(1,11):
#     print(f"{num**i}",end=" ")

# 13. Check if a number is prime using a loop.

# num=int(input("Enter a number: "))
# count=0
# if num>0:
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print("Prime")
#     else:
#         print("Not a prime")

# 14. Print first 10 natural numbers using while loop.

# num=int(input("enter a number: "))
# while num>0:
#     for i in range(1,num+1):
#         print(i,end=" ")
#     i+=1
#     break

# num=int(input("enter a num: "))
# for i in range(1,num+1):
#     print(i,end=" ")

# 15. Count down from 10 to 1 using a loop.

# num=int(input("Enter a number: "))
# while num>0:
#     for i in range(10,0,-1):
#         print(i,end=" ")
#     i+=1
#     break

# num=int(input("Enter a number: "))
# for i in range(10,0,-1):
#     print(i,end=" ")

# # 16. Find product of all numbers from 1 to 10.
# product=1
# for i in range(1,11):
#     product=product*i     #1*1=1 1*2=2 2*3=6 6*4=24
# print(f"{product}")

# 17. Print numbers from 1 to 100 in steps of 5.
# for i in range(1,101,5):
#     print(i,end=" ")

# 18. Find numbers between 1–50 divisible by both 3 and 5.
# num=int(input("enter a number: "))
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)


# 19. Print all prime numbers between 1 to 50.   ####### DOUBT #########
# for num in range(2, 51):  # start from 2 (smallest prime)
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 21. Find the smallest digit in a number.

# num=int(input('enter a number: '))
# smallest=9
# while num>0:
#     digit=num%10
#     if digit<smallest:
#         smallest=digit
#     num=num//10
# print(f"{smallest}")

# 22. Find the largest digit in a number
# num=421876
# largest=0
# while num>0:
#     digit=num%10
#     if digit>largest:
#         largest=digit
#     num=num//10
# print(largest)

# 23. Print pattern: 1 2 3, 4 5 6, 7 8 9
# count=1
# for i in range(3):
#     for j in range(3):
#         print(count,end=" ")
#         count+=1
#     print()
# O/P:
# 1 2 3 
# 4 5 6
# 7 8 9

# 24. Print pattern of stars in triangle format.
# n=5
# for i in range(1,n+1):
#     rows=" "
#     for j in range(1,i+1):
#         rows+="*"
#     print(rows)

# 25. Print sum of even digits in a number.

# num=124222
# sum=0
# while num>0:
#     digit=num%10
#     if digit%2==0:
#         sum+=digit
#     num=num//10
# print(sum)

# 26. Print sum of odd digits in a number.
# num=1567
# sum=0
# while num>0:
#     digit=num%10
#     if digit%2!=0:
#         sum+=digit
#     num=num//10
# print(sum)

# 27. Print table of a given number.
# num=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# 28. Count how many times a digit occurs in a number.
# num=6543333
# digit_of_num=3
# count=0
# while num>0:
#     digit=num%10
#     if digit==digit_of_num:
#         count+=1
#     num=num//10
# print(f"{count}")

# 29. Sum of squares of digits of a number.

# num=234
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit**2
#     num=num//10
# print(sum)


# 30. Sum of cubes of digits of a number.

# num=int(input("enter a number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit**3
#     num=num//10
# print(sum)

# 31. Count multiples of 3 between 1 and 100.

# count=0
# for i in range(1,100):
#     if i%3==0:
#         count+=1
# print(f"{count}")          #33

# 32. Print 10, 20, 30... up to 100.

# for i in range(10,101,10):
#     print(i,end=" ")    

# 33. Print reverse of a number using while loop.

# num=int(input("Enter a number: "))
# num1=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)          ####reverse
# if num1==rev:       #####palindrome
#     print("Palin")
# else:
#     print("Not")

# 34. Find if number is Armstrong number (3-digit only).

# num=int(input("enter a number: "))
# num1=num
# num2=num
# sum=0
# len=0
# while num>0:
#     digit=num%10
#     len+=1
#     num=num//10
# print(len)
# while num1>0:
#     digit=num1%10
#     sum+=digit**len
#     num1=num1//10
# print(sum)
# if sum==num2:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 35. Print Fibonacci series up to n terms.

# num=int(input("Enter a number: "))
# count=0
# a=0
# b=1
# while count<num:
#     print(a,end=" ")
#     a,b=b,a+b
#     count+=1


# num=5
# a=0
# b=1
# for i in range(num):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c


# 36. Print GCD of two numbers using loop.

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# i=1
# while i<=a and i<=b:
#     if a%i==0 and b%i==0:
#         gcd=i
#     i+=1
# print(gcd)


# 37. Print LCM of two numbers using loop.

# 38. Display all even digits in a number.
# num=int(input("enter a number: "))
# while num>0:
#     digit=num%10
#     if digit%2==0:
#         print(digit,end=" ")
#     num=num//10

# # 39. Display all odd digits in a number.
# num=int(input("Enter a number: "))
# while num>0:
#     digit=num%10
#     if digit%2!=0:
#         print(digit,end=" ")
#     num=num//10

# 40. Print the ASCII values from 65 to 90.
# for i in range(65,91):
#     print(chr(i),end=" ")
# O/P:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 


###Print from -1 to -10
# for i in range(-1,-11,-1):
#     print(i,end=" ")
# O/P:
# -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 



##########  MEDIUM PROBLEMS  ###########

# 41. Check if a number is palindrome using loop.

# num=int(input("Enter a number: "))
# num1=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)
# if rev==num1:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 42. Print multiplication tables from 1 to 10.

# num=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")


# QUESTION   Factors of a number

# num=int(input("Enter a number: "))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i,end=" ")
#     i+=1

# # 43. Display the sum of factorials from 1 to 5. 

# sum=0
# for num in range(1,6):   # from 1 to 5
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     sum+=fact
# print(sum)    #153

###  Factorial
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

##factors##


# 44. Check if a number is perfect number using loop. 6=1+2+3  # if we add the factors of that ni is ..the no is == that numebr ..

# num=int(input("Enter a number: "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
#     i+=1
# print(sum)
# if sum==num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")


# 45. Print all factors of a number.

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if i<=n:
#         if n%i==0:
#             print(i,end=" ")
#         i+=1

# 46. Find HCF of two numbers.

# # 47. Find the count of digits divisible by 3.

# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     digit=num%10
#     if digit%3==0:
#         count+=1
#     num=num//10
# print(count)

# 48. Count the number of trailing zeroes in a factorial.


# # 49. Print pattern: 1, 12, 123, ... up to n lines.

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     row=0
#     for j in range(1,i+1):
#         row=row*10+j
#     print(row)
# O/P:
# Enter a number: 5
# 1
# 12
# 123
# 1234
# 12345