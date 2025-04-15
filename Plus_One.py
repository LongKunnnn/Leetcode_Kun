class Solution:
    def plusOne(self,digits):
        #Nếu mảng rỗng ta return ''
        if not digits:
            return ''
        #Tạo biến là độ dài của mảng để duyệt qua
        n = len(digits)
        #Duyệt phần tử cuối cùng
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
                #Nếu phần tử đó bằng 9 ta cần biến nó thành 0 và cộng thêm 1 cho phần tử đứng trước
            digits[i] = 0

        return [1] + digits
