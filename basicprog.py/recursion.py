def fact(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fact(n-1)+fact(n-2)
for i in range(11):
    print(fact(i))






