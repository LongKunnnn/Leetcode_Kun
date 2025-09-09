class Solution {

    public boolean hasZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return true; 
            x /= 10;    
            
        }
        return false;
    }
    public int[] getNoZeroIntegers(int n) {
        for (int i = 1; i < n; i++) {
            int find = n - i;
            if (!hasZero(i) && !hasZero(find)) {
                return new int[] {i, find};
            }
        }
        return new int[]{};
    }
}