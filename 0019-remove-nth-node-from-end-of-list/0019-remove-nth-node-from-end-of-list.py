# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return []
        temp = [ListNode(head.val)]
        while head.next is not None:
            temp.append(ListNode(head.next.val))
            head = head.next
        result = None
        for i in range(len(temp)):
            if i + 1 == n:
                temp.pop()
                continue
            temp_node = temp.pop()
            temp_node.next = result
            result = temp_node
        return result