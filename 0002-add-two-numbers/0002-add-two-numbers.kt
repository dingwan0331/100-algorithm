/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var a = ""
        var b = ""
        
        var currentNode1 = l1
        var currentNode2 = l2
        while (currentNode1 != null){
            a += currentNode1.`val`.toString()
            currentNode1 = currentNode1.next
        }
        while (currentNode2 != null){
            b += currentNode2.`val`.toString()
            currentNode2 = currentNode2.next
        }
        var c = BigInteger(a.reversed()) + BigInteger(b.reversed())
    val digits = c.toString().reversed().map { it.toString().toInt() } // 숫자를 각 자리수별로 분리하여 리스트로 변환
    var head: ListNode? = null // 헤드 노드 생성
    var currentNode: ListNode? = null

    for (digit in digits) {
        val newNode = ListNode(digit) // 각 숫자로 새로운 노드 생성

        if (head == null) {
            head = newNode // 첫 번째 노드 설정
            currentNode = head
        } else {
            currentNode?.next = newNode // 이전 노드의 다음 노드로 새로운 노드 추가
            currentNode = newNode // 현재 노드를 새로운 노드로 이동
        }
    }

    return head
    }
}