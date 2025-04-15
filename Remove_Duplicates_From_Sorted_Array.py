class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Nếu mảng rỗng, trả về độ dài 0

        # Chỉ số chèn phần tử không trùng lặp
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # Trả về độ dài của mảng đã loại bỏ phần tử trùng lặp
        return i + 1
