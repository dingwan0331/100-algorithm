import kotlin.math.abs

class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        val len = nums.size
        var closestSum: Int? = null

        for (i in 0 until len - 2) {
            for (j in i + 1 until len - 1) {
                for (k in j + 1 until len) {
                    val currentSum = nums[i] + nums[j] + nums[k]
                    if (closestSum == null || abs(target - currentSum) < abs(target - closestSum!!)) {
                        closestSum = currentSum
                    }
                    if (currentSum == target) return target
                }
            }
        }
        return closestSum ?: 0
    }
}