# Strong Number Program in Python

# Step 1: Take input
num = int(input("Enter a number: "))

# Step 2: Keep original number for comparison
temp = num
sum = 0   # to store sum of factorials

# Step 3: Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# Step 4: Extract digits and calculate factorial sum
while temp > 0:
    digit = temp % 10            # get last digit
    sum = sum + factorial(digit) # add factorial of digit to sum
    temp = temp // 10            # remove last digit

# Step 5: Compare with original number
if sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")



num=int(input("Enter a number:"))
sum=0
for i in str(num):
    n=int(i)
    fact=1
    for j in range(1,n+1):
        fact=fact*j
    sum+=fact
if(sum==num):
    print("strong number:")
else:
    print("not a strong number")