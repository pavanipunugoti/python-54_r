def is_subsequence(s,t):
    s_index = 0
    t_index = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index  += 1
    return s_index == len(s)
s = "ace"
t = "abcde"
if is_subsequence(s,t):
    print(f" '{s}' is subsequence of '{t}'.")
else:
    print(f" '{s}' is not a subsequence of '{t}'.")
s = "aec"
if is_subsequence(s,t):
    print(f" '{s}' is a subsequence of '{t}'.")
else:
    print(f" '{s}' is not a subsequence of '{t}'.")
    
    
    
a,b = 5,10
a,b = b,a
print(a,b)  


def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1): # range(2,7**1/2) ,,+1 means,if manaki given value kuda include undali ante then we use 1
        if n % i == 0:               # range(2,3)
            return False
    return True
print(is_prime(7))
print(is_prime(10))


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5))
    
    
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("Hello"))


def fibonacci(n):
    a,b = 0 , 1
    for i in range(n):
        print(a,end="")
        a,b = b,a+b
fibonacci(5)


def second_largest(arr):
    unique_sorted= sorted(set(arr),reverse = True)
    return unique_sorted[1] if len(unique_sorted)>1 else None
arr = [10,20,4,45,99]
print(second_largest(arr))



def count_vowels(s):
    return sum (1 for char in s.lower() if char in "aeiou")
print(count_vowels("Hello World"))



def second_largest(arr):
    unique_sorted = sorted (set(arr),reverse = True)
    return unique_sorted[1] if len(unique_sorted)>1 else None
arr = [10,20,4,45,99]
print(second_largest(arr))


def first_non_repeating_char(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
        for char in s:
            if char_count[char]==1:
                return char
            return None
print(first_non_repeating_char("pavani"))


def rotate_array(nums,k):
    k %=len(nums)
    nums[:] = nums[-k:]+nums[:-k]
nums = [1,2,4,5]
rotate_array(nums,2)
print(nums)



def are_anagrams(s1,s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen","silent"))



def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n+1)//2
    actual_sum = sum(nums)
    return total_sum-actual_sum
print(find_missing_number([1,2,4,5]))


def fibonacci(n):
    fib_sequence = [0,1]
    while fib_sequence[-1]<n:
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])    
    return fib_sequence[::-1]
print(fibonacci(50))



def checkevenorodd(num):
    if num % 2 == 0:
        print("Given Number is Even")
    else:
        print("Given Number is odd")
d = int(input("Enter any Number:"))
print(checkevenorodd(d))
    



