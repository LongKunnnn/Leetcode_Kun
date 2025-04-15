class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # Dùng Dictionary để lưu phần tử và chỉ số của nó
        for i, num in enumerate(nums):
            complement = target - num  # Tính toán phần tử còn lại cần tìm
            if complement in hashmap:  # Nếu phần tử đó đã xuất hiện trước đó
                return [hashmap[complement], i]  # Trả về chỉ số của cặp phần tử
            hashmap[num] = i  # Lưu phần tử và chỉ số của nó vào HashMap
        return []  # Trả về một mảng rỗng nếu không tìm thấy cặp nào
