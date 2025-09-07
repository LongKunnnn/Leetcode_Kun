import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); // ✅ trong Java dùng Arrays.sort, không phải nums.sort
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            // tránh trùng lặp cho nums[i]
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = n - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];

                if (total < 0) {
                    left++;
                } else if (total > 0) {
                    right--;
                } else {
                    // ✅ trong Java không có append([]), mà dùng Arrays.asList
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    // bỏ qua duplicate cho left
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    // bỏ qua duplicate cho right
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
            }
        }
        return res;
    }
}
