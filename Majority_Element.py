#Cách 1 (Sử dụng Counter):
from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq > len(nums) / 2:
                return num


#Cách 2 (Sử dụng hash_map):
class Solution:
    def majorityElement(self, nums : List[int]) -> int:
        hash_map = {}
        majority = len(nums) / 2
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] > majority:
                return num


        