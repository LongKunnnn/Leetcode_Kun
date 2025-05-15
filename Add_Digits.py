class Solution:
    #Cách 1:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(i) for i in str(num))

        return num
        
    #Cách 2(Dùng công thức toán học):
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num - 1) % 9        
        