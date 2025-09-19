from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n-1)) == 0 and (n & 0x55555555) != 0