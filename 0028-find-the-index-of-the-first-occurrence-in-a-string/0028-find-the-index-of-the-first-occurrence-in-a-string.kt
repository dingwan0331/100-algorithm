class Solution {
    fun strStr(haystack: String, needle: String): Int {
        for (i in 0..haystack.length){
            if (i+needle.length > haystack.length){
                break
            }
            if (haystack.substring(i..i+needle.length-1)==needle){
                return i
            }
        }
        return -1
    }
}