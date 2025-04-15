class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Xác định xem một số nguyên có phải là số đối xứng (palindrome) hay không
        bằng cách chuyển đổi thành chuỗi.
        
        Args:
            x: Số nguyên cần kiểm tra
            
        Returns:
            bool: True nếu x là số đối xứng, False nếu không phải
        """
        # Chuyển số thành chuỗi
        s = str(x)
        
        # So sánh chuỗi gốc với chuỗi đảo ngược
        # s[::-1] tạo ra một chuỗi mới bằng cách đảo ngược chuỗi s
        return s == s[::-1]