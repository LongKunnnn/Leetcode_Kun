class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Khởi tạo một set để theo dõi các phần tử đã gặp
        for num in nums:
            if num in seen:  # Nếu phần tử đã có trong set, tức là có trùng lặp
                return True
            seen.add(num)  # Nếu chưa xuất hiện, thêm phần tử vào set
        return False  # Không có phần tử trùng lặp nào
