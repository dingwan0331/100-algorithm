class Solution {
    fun climbStairs(n: Int): Int {
        if (n == 1 || n == 0) {
            return 1
        }

        val dp = IntArray(n + 1)
        dp[0] = 1
        dp[1] = 1

        for (i in 2..n) {
            dp[i] = dp[i - 1] + dp[i - 2]
        }

        return dp[n]
    }
}