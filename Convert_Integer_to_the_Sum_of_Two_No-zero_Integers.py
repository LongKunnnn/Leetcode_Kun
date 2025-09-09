class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(x):
            return '0' in str(x)
        for i in range(n):
            find = n - i
            if not has_zero(find) and not has_zero(i):
                return [i, find]