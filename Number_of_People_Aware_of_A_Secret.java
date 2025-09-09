class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int MOD = 1_000_000_007;
        long[] dp = new long[n + 1];
        dp[1] = 1;

        for (int i = 1; i <= n ; i++) {
            for(int j = i + delay; j < Math.min(i + forget, n + 1) ; j++) {
                dp[j] = (dp[i] + dp[j]) % MOD;

            }
        }
        long ans = 0;
        for (int i = n - forget + 1; i <= n; i++) {
            if (i >= 1) ans = (ans + dp[i]) % MOD;
        }

        return (int) ans;
    }
}