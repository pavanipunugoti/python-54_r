# Check if a number is palindrome using loops
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print(num, "is a Palindrome number")
else:
    print(num, "is Not a Palindrome number")
