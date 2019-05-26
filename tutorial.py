# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
# a = __name__

# print("The name of the module is: ", a)

import sys
old = sys.getrecursionlimit()
print("Initial recursion depth", old)
sys.setrecursionlimit(1000000)
old = sys.getrecursionlimit()
print("new recursion limit", old)