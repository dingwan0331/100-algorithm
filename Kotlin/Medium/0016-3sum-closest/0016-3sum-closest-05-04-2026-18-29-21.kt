import kotlin.math.abs

class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        // 1. 배열 정렬
        nums.sort()
        val len = nums.size
        // 첫 번째 가능한 합으로 초기화
        var closestSum = nums[0] + nums[1] + nums[2]

        for (i in 0 until len - 2) {
            var left = i + 1
            var right = len - 1

            while (left < right) {
                val currentSum = nums[i] + nums[left] + nums[right]

                // 현재 합이 target과 완벽히 일치하면 바로 반환
                if (currentSum == target) return target

                // 기존 closestSum보다 더 target에 가깝다면 업데이트
                if (abs(target - currentSum) < abs(target - closestSum)) {
                    closestSum = currentSum
                }

                // target에 가까워지기 위해 포인터 이동
                if (currentSum < target) {
                    left++
                } else {
                    right--
                }
            }
        }
        return closestSum
    }
}