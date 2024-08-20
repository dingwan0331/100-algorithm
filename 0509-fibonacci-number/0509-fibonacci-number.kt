class Solution {
    fun fib(n: Int): Int {
        if (n==0) return 0
        val m = n-1
        if (m==1 || m==0) return 1
        val tempList = IntArray(m + 1)
        tempList[0] = 1
        tempList[1] = 1
        
        for (i in 2..m){
            tempList[i] = tempList[i-1] + tempList[i-2] 
        } 
        return tempList[m]
    }
}