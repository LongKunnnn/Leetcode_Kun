class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}
        for i, num in enumerate(nums):
            if num in unique and i - unique[num] <= k:
                return True
            unique[num] = i
        return False