class Solution {
    fun lengthOfLastWord(s: String): Int {
        val la = s.split(" ")
        for (i in la.count()-1 downTo 0){
            if (la[i] != ""){
                return la[i].length
            }
        }
        return 0
    }
}