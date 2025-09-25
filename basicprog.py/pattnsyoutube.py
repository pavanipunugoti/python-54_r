# patterns from youtube..All patterns..########

# to print the right angled traingle..
"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 

"""
# print the pattern
"""

num=int(input("Enter a number:"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()
    
Enter a number:5
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * * 
"""
"""
n c
    
    
    
*                     * 
* *                 * * 
* * *             * * * 
* * * *         * * * * 
* * * * *     * * * * * 
* * * * * * * * * * * * 

"""

"""
n=5
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    for j in range(0,n-i):
        print(end="    ")
    for j in range(0,i):
        print("*",end=" ")
        
    print()

for i in range(n-1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    for j in range(0,n-i):
        print(end="    ")
    for j in range(0,i):
        print("*",end=" ")
    print()
    
                       
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

"""
n=5
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    for j in range(0,n-i):
        print(end="    ")
    for j in range(0,i):
        print("*",end=" ")
        
    print()

for i in range(n-1,0,-1):
    for j in range(0,
                   i):
        print("*",end=" ")
    for j in range(0,n-i):
        print(end="    ")
    for j in range(0,i):
        print("*",end=" ")
    print()
