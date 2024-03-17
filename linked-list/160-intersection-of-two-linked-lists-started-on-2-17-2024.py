"""
ideas:
traverse headA all the way to the end, storing previously encountered nodes
traverse headB until you encounter a node that is stored, then return it - if you never encounter a stored node, return null

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        while headA:
            d[headA] = 0
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            headB = headB.next
        return None

        
