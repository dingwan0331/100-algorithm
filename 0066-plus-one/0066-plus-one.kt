import java.math.BigInteger

class Solution {
    fun plusOne(digits: IntArray): IntArray {
        val str = StringBuilder()
        for (digit in digits){
            str.append(digit)
        }
        val a = BigInteger(str.toString()).add(BigInteger.ONE)
        val str_a = a.toString()
        val answer = mutableListOf<Int>()
        for (c in str_a){
            answer.add(c.toString().toInt())
        }
        return answer.toIntArray()
    }
}
