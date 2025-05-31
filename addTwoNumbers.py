# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy        
        addon = 0

        while l1 or l2:
            numval = (l1.val if l1 else 0) + (l2.val if l2 else 0) + addon
            addon = numval // 10  # Handles carry
            tail.next = ListNode(numval % 10)
            tail = tail.next     # Advance the tail
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there's still a carry after the loop
        if addon:
            tail.next = ListNode(addon)

        return dummy.next
