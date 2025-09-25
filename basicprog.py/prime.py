# # Prime number using loops
# numbers = [10, 3, 5, 8, 11, 15, 17, 20]
# prime_list = []
# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             prime_list.append(num)
# print("Prime numbers:", prime_list)

#Prime numbers Using Function
def primes(numbers):
    list1 = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                list1.append(num)
    return list1
numbers = [10, 3, 5, 8, 11, 15, 17, 20]
primes_numbers = primes(numbers)
print("Prime numbers:", primes_numbers)


   