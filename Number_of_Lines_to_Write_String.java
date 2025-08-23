class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int lines = 1, cur = 0;
        for (char ch : s.toCharArray()) {
            int w = widths[ch - 'a'];
            if (cur + w > 100) {
                lines += 1;
                cur = w;
            }
            else {
                cur += w;
            } 
        }
        return new int[] {lines, cur};
    }
}