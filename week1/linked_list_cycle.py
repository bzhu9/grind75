# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sing, doub = head, head
        while sing and doub and doub.next:
            sing = sing.next
            doub = doub.next.next
            if sing == doub:
                return True
        return False
