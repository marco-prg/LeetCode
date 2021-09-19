# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

#     F(0) = 0, F(1) = 1
#     F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n
        
        the_old = 1
        the_one = 1
        
        for i in range(2, n):
            the_one, the_old = the_old + the_one, the_one
            
        return the_one