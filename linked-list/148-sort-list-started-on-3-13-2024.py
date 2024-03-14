"""
ways to sort list - automatic python method
merge sort
bubble sort
it's probably going to be more efficient to write one of these algs but modify it for a linked list

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # why use temp here? because you're about to delete the object in question. So temp will point at the object, and the old pointer to that object will now point at None
        listTwo = head
        tmp = slow.next
        slow.next = None
        listOne = tmp

        listOne = self.sortList(listOne)
        listTwo = self.sortList(listTwo)

        # merge
        tail = dummy = ListNode()
        while listOne and listTwo:
            if listOne.val < listTwo.val:
                tail.next = listOne
                listOne = listOne.next
            else:
                tail.next = listTwo
                listTwo = listTwo.next
            tail = tail.next # why is this needed? because otherwise, we'd overwrite the most recent node we placed
        if listOne:
            tail.next = listOne
        if listTwo:
            tail.next = listTwo
        return dummy.next
        
