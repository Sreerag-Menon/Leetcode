'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN=-2**31
        INT_MAX=2**31-1
        if x<0:
            reversed_x=-int(str(-x)[::-1])
        else:
            reversed_x=int(str(x)[::-1])
        if reversed_x<INT_MIN or reversed_x>INT_MAX:
            return 0
        return reversed_x
