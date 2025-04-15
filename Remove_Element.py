class Solution:
    def removeElement(self, nums, val):
        i = 0  # Con trỏ i, chỉ số cho mảng đã thay đổi
        for j in range(len(nums)):  # Con trỏ j, duyệt qua mảng
            if nums[j] != val:  # Nếu phần tử không phải val, giữ lại
                nums[i] = nums[j]  # Đặt phần tử tại vị trí i
                i += 1  # Tăng i lên
        return i  # Trả về độ dài mảng mới
