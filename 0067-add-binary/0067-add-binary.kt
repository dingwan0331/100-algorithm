class Solution {
    fun addBinary(a: String, b: String): String {
        val intA = BigInteger(a,2)
        val intB = BigInteger(b,2)
        val combine = intA + intB
        return combine.toString(2)
    }
}