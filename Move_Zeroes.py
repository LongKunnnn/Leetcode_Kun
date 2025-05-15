class Solution:
    #Cách 1(Sử dụng con trỏ):
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
    
    #Cách 2(Tạo mảng mới):
    def moveZeroes(self, nums: List[int]) -> None:
        new = [int(i) for i in nums if i != 0]
        nums[:] = new + [0] * (len(nums) - len(new))