# # to print the all square patterns:
# n=int(input("Enter the Number:"))
# for rows in range(1,n+1):
#     for cols in range(1,n+1):
#         print("*",end=" ")
#     print()
    
# # to print the right angles traingled 
# n=int(input("Enter the Number:"))
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print("*",end=" ")
#     print()
    
# n=5
# for row in range(1,n+1):
#     rows=""
#     for cols in range(1,row+1):
#         rows+="*"
#     print(rows)
    
# # To print the right reverse 
# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,i):
# #         print(end="  ")
# #     for j in range(1,n-i+2):
# #         print("*",end=" ")
# #     print()
        
        
        
# """
# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for j in range(n-i,0,-1):
#         print("*",end=" ")
#     print()
    
# * * * * 
#   * * * 
#     * * 
#       * 
      
# """
    
# """
# n=int(input("Enter a numberr:"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(end=" ")
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     print()
    
# Enter a numberr:5
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
    
# """ 


# """
# n=5
# for i in range(1,n-1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()
    
# * * * * * 
# * * * * * 
# * * * * * 

# """


# """

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-1):
#         print("*",end=" ")
#     print()
    
# * * * 
# * * * 
# * * * 
# * * * 
# * * * 

# """     

# """

# n=int(input("enter the value"))
# for i in range(1,n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i):
#         print("*",end=" ")
#     print()
    
# for i in range(n):
#     for k in range(i):
#         print(" ",end=" ")
#     for j in range(2*(n-i)):
#         print("*",end=" ")
#     print()
    
#     """
    
# """
# n=int(input("Enter a number:"))
# for i in range(2,n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
    
# * * * * * 
# * * * * * 
# * * * * * 
# """
 
n = 6
for i in range(1, n+1):
    for j in range(1, n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(1, n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
    