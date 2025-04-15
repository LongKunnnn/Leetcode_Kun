class Solution:
    def merge(self, nums1, m, nums2, n):
        #Tạo 3 con trỏ để duyệt qua 2 mảng
        i,j,k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            #So sánh phần tử nào lớn hơn thì insert vào vị trí k
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            #Nếu còn phần tử ở nums2 chưa được insert vào nums1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1