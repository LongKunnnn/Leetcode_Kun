class Solution:
    def searchInsert(self,nums,target):
        left, right = 0 , len(nums) - 1 #Tạo biến left và right để chia array thành các mảng nhỏ
        while left <= right: # Điều kiện cần
            mid = left + (right - left) // 2 #Công thức này dể tránh tình trạng tràn số
            #Tìm vị trí target
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                #Trả về chỉ số cần tìm chính là left
        return left
