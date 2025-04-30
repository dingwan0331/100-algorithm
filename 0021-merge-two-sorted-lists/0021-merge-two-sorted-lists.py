# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        result = ListNode()
        while left is not None or right is not None:
            if left is None:
                self.append_result(result,right.val)
                right = right.next
            elif right is None:
                self.append_result(result,left.val)
                left = left.next
            else:
                if left.val > right.val:
                    self.append_result(result,right.val)
                    right = right.next
                else:
                    self.append_result(result,left.val)
                    left = left.next
        return result.next
    def append_result(self,result:ListNode, val: int):
        while result.next:
            result = result.next
        result.next = ListNode(val=val)
        return result