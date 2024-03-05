# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        while head:
            if head.val in d:
                for node in d[head.val]:
                    if node==head:
                        return True
                d[head.val].append(head)
            else:
                d[head.val] = [head]
            head = head.next
        return False 
