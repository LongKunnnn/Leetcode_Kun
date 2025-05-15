class Solution:
    #Cách 1:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(0, length + 1):
            if i not in nums:
                return i
    
    #Cách 2:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xor_all = 0
        xor_nums = 0
        for i in range(0 , n + 1):
            xor_all ^= i
        for i in nums:
            xor_nums ^= i
        return xor_all ^ xor_nums
