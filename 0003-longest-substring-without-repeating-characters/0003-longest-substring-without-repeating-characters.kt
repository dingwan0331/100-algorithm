class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
    val charMap = mutableMapOf<Char, Int>()
    var maxLength = 0
    var start = 0

    for (end in s.indices) {
        val currentChar = s[end]

        if (charMap.containsKey(currentChar)) {
            start = maxOf(start, charMap[currentChar]!! + 1)
        }

        charMap[currentChar] = end
        maxLength = maxOf(maxLength, end - start + 1)
    }

    return maxLength
    }
}