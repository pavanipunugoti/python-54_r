num = int(input("Enter a number: ")) 
len = 0   
total = 0    
temp = num
while temp > 0:
    len += 1
    temp //= 10
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** len
    temp //= 10
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
    
