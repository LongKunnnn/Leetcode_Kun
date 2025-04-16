from typing import List, Optional
# Định nghĩa lớp TreeNode để tạo một nút cây nhị phân

class Solution:
    def sortedArrayToBST(self, nums:List[int]) -> Optional[TreeNode]:
        # Hàm đệ quy để tạo cây nhị phân từ mảng đã sắp xếp
        if not nums:  # Nếu mảng trống, trả về None
            return None
        
        # Chọn phần tử giữa mảng làm gốc của cây
        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # Tạo nút gốc với phần tử giữa mảng
        
        # Đệ quy cho cây con trái và cây con phải
        root.left = self.sortedArrayToBST(nums[:mid])  # Cây con trái
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # Cây con phải
        
        return root  # Trả về gốc cây đã tạo
