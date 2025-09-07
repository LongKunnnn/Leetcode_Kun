class Solution {
    public int maxArea(int[] height) {
        int i = 0, j = height.length - 1;
        int max_area = 0;

        while (i < j) {
            int h;
            int area;

            h = Math.min(height[i], height[j]);
            area = h * (j - i);

            if (area > max_area) {
                max_area = area;
            }

            if (height[i] < height[j]) {
                i += 1;
            } else {
                j -= 1;
            }

        }
        return max_area;
    }
}