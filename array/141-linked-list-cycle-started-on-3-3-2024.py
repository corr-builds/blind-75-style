Beats 23, 81

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast = head.next
        while head and fast and fast.next:
            if head == fast:
                return True
            head = head.next
            fast = fast.next.next
        return False 
