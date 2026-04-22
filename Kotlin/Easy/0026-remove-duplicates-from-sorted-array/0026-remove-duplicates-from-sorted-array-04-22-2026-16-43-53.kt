class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        
        if (nums.isEmpty()) return 0

        var slow = 1

        for (fast in 1 until nums.size) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast] 
                slow++ 
            }
        }
        return slow
    }
}