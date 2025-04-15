class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # Trường hợp needle rỗng, trả về 0
        if m == 0:
            return 0

        # Duyệt từ vị trí 0 đến n - m (vì sau đó không đủ độ dài để so sánh nữa)
        for i in range(n - m + 1):
            # So sánh từng chuỗi con có độ dài bằng needle
            if haystack[i:i + m] == needle:
                return i  # Tìm thấy needle, trả về vị trí

        return -1  # Không tìm thấy needle
