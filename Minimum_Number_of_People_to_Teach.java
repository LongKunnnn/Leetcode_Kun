import java.util.*;

class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        // B1: Chuyển danh sách ngôn ngữ của mỗi người sang Set để tiện so sánh
        List<Set<Integer>> userLang = new ArrayList<>();
        for (int i = 0; i < languages.length; i++) {
            Set<Integer> set = new HashSet<>();
            for (int lang : languages[i]) {
                set.add(lang);
            }
            userLang.add(set);
        }

        // B2: Tìm tập problematic (những người không thể giao tiếp với bạn bè)
        Set<Integer> problematic = new HashSet<>();
        for (int[] f : friendships) {
            int u = f[0] - 1; // đổi về 0-index
            int v = f[1] - 1;
            if (!canCommunicate(userLang.get(u), userLang.get(v))) {
                problematic.add(u);
                problematic.add(v);
            }
        }

        if (problematic.isEmpty()) return 0;

        // B3: Đếm ngôn ngữ đã biết trong tập problematic
        int[] cnt = new int[n + 1]; // cnt[i] = số người biết ngôn ngữ i
        for (int u : problematic) {
            for (int lang : userLang.get(u)) {
                cnt[lang]++;
            }
        }

        // B4: Tìm ngôn ngữ phổ biến nhất
        int maxKnown = 0;
        for (int i = 1; i <= n; i++) {
            maxKnown = Math.max(maxKnown, cnt[i]);
        }

        return problematic.size() - maxKnown;
    }

    // Hàm kiểm tra 2 người có ngôn ngữ chung không
    private boolean canCommunicate(Set<Integer> a, Set<Integer> b) {
        for (int lang : a) {
            if (b.contains(lang)) return true;
        }
        return false;
    }
}
