class Solution:
    #Cách 1:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    #Cách 2(Tối ưu hơn):
    import re
    def isPalindrome(self, s : str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]+' , '', s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    