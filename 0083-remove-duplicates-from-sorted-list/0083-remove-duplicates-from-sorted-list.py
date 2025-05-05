# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        current = head
        compare = -2000
        while current:
            if compare != current.val:
                compare = current.val
                list1.append(current.val)
            current = current.next
        result = None
        for i in list1[::-1]:
            result = ListNode(i,result)
        return result