"""
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

U:
  Given x-the base number and n-the exponent
  Exponential is multiplying the base number based on the exponent number
  For example: x = 3 , n = 5 -> 3^5 = 3 * 3 * 3 * 3 * 3
M: 
  Recursive
    n = 0, return 1
    n = 1, return x
    n = -1, return 1/x
    x^n = x * x * x * ... * x(n)
P:
  creating myExp function:
    base case:
      if n = 0
        return 1
      if n = 1 
        return x
      if n = -1
        return 1/x
I:
R:
E:

"""

def myExp(x,n):
  if n == 0:
    return 1
  if n == 1:
    return x
  if n <= -1:
    return 1/x*n
  result = x ** n
  print(round(result),5)
myExp(2.00000,10)
