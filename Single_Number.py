#Cách 1:
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter:
            if counter[i] == 1:
                return i

#Cách 2(Tối ưu hơn):
def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res