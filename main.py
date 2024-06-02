# print name n times using recursion

# n = int(input("Enter the number "))
# count = 0
#
# def name_print(count,n):
#     if(count <= n):
#         print("AXE")
#         name_print(count+1,n)
#
#
# name_print(1,n)

# time complexity is o(n)
# space complexity is o(n)


# -----------print 1 to n---------------------
# n = int(input("Enter the number "))
# count = 0
#
# def name_print(count,n):
#     if(count <= n):
#         print(count)
#         name_print(count+1,n)
#
#
# name_print(1,n)
# time complexity is o(n)
# space complexity is o(n)

# -----------print n to 1---------------------
# n = int(input("Enter the number "))
# count = 0
#
# def name_print(n,count):
#     if(n >= count):
#         print(n)
#         name_print(n-1,count)
#
#
# name_print(n,1)
# time complexity is o(n)
# space complexity is o(n)

# --------------print 1 to n using backtrack--------------
# n = int(input("Enter the number "))
#
#
# def name_print(i,n):
#     if i<1:
#         return
#     name_print(i-1,n)
#     print(i)
#
# name_print(n,n)

# --------------print n to 1 using backtrack--------------
# n = int(input("Enter the number "))
#
#
# def name_print(i,n):
#     if i>n:
#         return
#
#     name_print(i+1,n)
#     print(i)
#
#
#
# name_print(1,n)



# --------------------sum of n number---------------
n = int(input("Enter the number "))
sum = 0
i = 0
def num_sum(i,sum):
    if i<0:
        print(sum)
        return
    num_sum(i-1,sum+i)
num_sum(n,sum)

