# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        while head:
            if head in seen :
                return True
            else:
                seen[head] = head.val
                head = head.next
        return False