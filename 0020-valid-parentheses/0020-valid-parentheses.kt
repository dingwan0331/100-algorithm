class Solution {
    fun isValid(s: String): Boolean {
        val myStack = mutableListOf<Char>()
        val braketMap =  mapOf(
            '{' to '}',
            '(' to ')',
            '[' to ']'
            )
        val openSymbolList = braketMap.keys.toList()
        for (i in s){
            if (i in openSymbolList){
                myStack.add(i)
            }
            else{
                if (braketMap[myStack.removeLastOrNull()] != i) return false
            }
        }
        return if (myStack.isEmpty()) true else false
    }
}