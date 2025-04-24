class Solution:
    #Cách 1 (Sử dụng hàm có sẵn):
    def hammingWeight(self, n: int) -> int:
         binary = bin(n).count('1')
        return binary

       
    
    #Cách 2:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count 
        